<template>
  <div class="chat-root" :data-open="open ? 'true' : 'false'">
    <button v-if="!open" class="chat-fab" @click="openChat" aria-expanded="false">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
      </svg>
      <span>Vraag Noa</span>
    </button>
    <div v-if="open" class="chat-panel" role="dialog" aria-label="WatNu18 chatbot">
      <div class="chat-header">
        <div class="chat-title">
          <div class="chat-name">Noa<span class="badge">assistent</span></div>
          <div class="chat-subtitle">Vraag alles over studiefinanciering, OV & toeslagen</div>
        </div>
        <div class="chat-actions">
          <button class="chat-icon-btn" @click="newChat" :disabled="streaming" title="Nieuw gesprek">⟳</button>
          <button class="chat-icon-btn" @click="open = false" aria-label="Sluiten">✕</button>
        </div>
      </div>
      <div class="chat-body" ref="scrollEl">
        <div v-if="topQuestions.length" class="topq">
          <div class="topq-title">Populaire vragen</div>
          <div class="topq-list">
            <button v-for="q in topQuestions" :key="q.id" class="topq-item" @click="askTopQuestion(q.question)">
              <span class="topq-q">{{ q.question }}</span>
              <span class="topq-count">{{ q.count }}×</span>
            </button>
          </div>
        </div>
        <div class="msgs">
          <div v-for="(m, idx) in messages" :key="idx" class="msg" :data-role="m.role">
            <div class="bubble">
              <div class="text" v-html="formatMessage(m.content)"></div>
              <div v-if="extractSources(m.content)" class="sources">
                <div v-html="extractSources(m.content)"></div>
              </div>
            </div>
          </div>
          <div v-if="streaming" class="msg" data-role="assistant">
            <div class="bubble typing">
              <div class="text">{{ draftAssistant || '⏳ Noa denkt na...' }}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="chat-footer">
        <label class="log-toggle">
          <input type="checkbox" v-model="logToFaq" />
          <span>Anoniem toevoegen aan populaire vragen</span>
        </label>
        <form class="composer" @submit.prevent="send">
          <input v-model="input" class="composer-input" type="text" placeholder="Typ je vraag…" :disabled="streaming" />
          <button class="composer-send" type="submit" :disabled="streaming || !input.trim()">Verstuur</button>
        </form>
        <div class="hint">Tip: vermeld je opleiding of situatie. Deel nooit persoonlijke gegevens.</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { nextTick, onMounted, ref } from 'vue'

const open = ref(false)
const input = ref('')
const streaming = ref(false)
const draftAssistant = ref('')
const logToFaq = ref(false)
const browserLocale = ref('nl-NL')

function detectLocale() {
  if (typeof window === 'undefined') return
  const nav = window.navigator
  const lang = (nav.language || (nav.languages && nav.languages[0]) || 'nl-NL').toString()
  browserLocale.value = lang
}

function initialGreeting() {
  return "Hoi! Ik ben Noa, jouw persoonlijke gids voor studiefinanciering, OV en alle regelingen als je 18 wordt. Stel me gerust alles!"
}

const messages = ref([{ role: 'assistant', content: initialGreeting() }])
const topQuestions = ref([])
const scrollEl = ref(null)
const activeController = ref(null)

function openChat() {
  if (open.value) return
  open.value = true
  loadTopQuestions()
  nextTick(scrollToBottom)
}

function scrollToBottom() {
  if (!scrollEl.value) return
  scrollEl.value.scrollTop = scrollEl.value.scrollHeight
}

async function loadTopQuestions() {
  try {
    const res = await fetch('/api/top-questions?limit=10')
    if (!res.ok) return
    const data = await res.json()
    topQuestions.value = data.items || []
  } catch { /* silent fail */ }
}

function askTopQuestion(q) {
  input.value = q
  send()
}

function buildPayload(userText) {
  return {
    locale: browserLocale.value || 'nl-NL',
    log_to_faq: !!logToFaq.value,
    messages: [
      ...messages.value.slice(-6).map(m => ({ role: m.role, content: m.content })),
      { role: 'user', content: userText }
    ]
  }
}

function newChat() {
  if (activeController.value) activeController.value.abort()
  streaming.value = false
  draftAssistant.value = ''
  input.value = ''
  logToFaq.value = false
  messages.value = [{ role: 'assistant', content: initialGreeting() }]
  nextTick(scrollToBottom)
}

async function send() {
  const text = input.value.trim()
  if (!text || streaming.value) return
  input.value = ''
  draftAssistant.value = ''
  streaming.value = true
  messages.value.push({ role: 'user', content: text })
  await nextTick(scrollToBottom)

  try {
    const controller = new AbortController()
    activeController.value = controller
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(buildPayload(text)),
      signal: controller.signal
    })
    if (!res.ok || !res.body) throw new Error(`HTTP ${res.status}`)

    const reader = res.body.getReader()
    const decoder = new TextDecoder('utf-8')
    let buffer = ''
    while (true) {
      const { value, done } = await reader.read()
      if (done) break
      buffer += decoder.decode(value, { stream: true })
      const parts = buffer.split('\n\n')
      buffer = parts.pop() || ''
      for (const part of parts) {
        const lines = part.split('\n')
        const eventLine = lines.find(l => l.startsWith('event:'))
        const dataLines = lines.filter(l => l.startsWith('data:'))
        const data = dataLines.map(l => l.replace(/^data:\s?/, '')).join('\n')
        const event = eventLine ? eventLine.replace('event:', '').trim() : 'message'
        if (event === 'error') throw new Error(data || 'Server error')
        if (event === 'done') {
          const finalText = (draftAssistant.value || '').trim()
          if (finalText) messages.value.push({ role: 'assistant', content: finalText })
          draftAssistant.value = ''
          streaming.value = false
          activeController.value = null
          loadTopQuestions()
          await nextTick(scrollToBottom)
          return
        }
        if (event === 'logged') continue
        if (data) {
          draftAssistant.value += data
          await nextTick(scrollToBottom)
        }
      }
    }
    const finalText = (draftAssistant.value || '').trim()
    if (finalText) messages.value.push({ role: 'assistant', content: finalText })
  } catch (e) {
    if (e?.name === 'AbortError') return
    messages.value.push({ role: 'assistant', content: '❌ Sorry, er ging iets mis. Probeer het later opnieuw.' })
  } finally {
    draftAssistant.value = ''
    streaming.value = false
    activeController.value = null
    await nextTick(scrollToBottom)
  }
}

onMounted(() => {
  detectLocale()
  loadTopQuestions()
})

function formatMarkdown(text) {
  // Parse markdown-achtige syntax: **bold**, *italic*, ***bold+italic***
  // Zorg ervoor dat we ***bold+italic*** voor ***italic+bold*** doen
  let result = text
  
  // Bold + Italic: ***text*** (drie sterretjes)
  result = result.replace(/\*\*\*([^*]+)\*\*\*/g, '<strong><em>$1</em></strong>')
  
  // Bold: **text** (twee sterretjes)
  result = result.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
  
  // Italic: *text* (één sterretje)
  result = result.replace(/\*([^*]+)\*/g, '<em>$1</em>')
  
  return result
}

function extractSources(content) {
  // Zoek naar "Sources:" of "Bronnen:" in het bericht
  const sourcesMatch = content.match(/(?:Sources:|Bronnen:)([\s\S]*?)$/i)
  if (!sourcesMatch) return null
  
  const sourcesText = sourcesMatch[1].trim()
  if (!sourcesText) return null
  
  // Format de sources met markdown support
  const formatted = formatMarkdown(sourcesText)
  return `<div class="sources-text">${formatted}</div>`
}

function formatMessage(content) {
  // Verwijder sources uit het bericht voor display
  const cleanContent = content.replace(/\n*(?:Sources:|Bronnen:)[\s\S]*$/i, '').trim()
  
  // Apply markdown formatting
  return formatMarkdown(cleanContent)
}
</script>

<style scoped>
@import '../styles/variables.css';

.chat-root {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: var(--z-fixed);
  font-family: var(--font-family-base);
}

.chat-fab {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  background: linear-gradient(135deg, var(--color-accent) 0%, var(--color-accent-dark) 100%);
  border: none;
  padding: var(--spacing-sm) var(--spacing-lg);
  border-radius: var(--radius-full);
  font-weight: var(--font-weight-semibold);
  color: white;
  box-shadow: var(--shadow-lg);
  cursor: pointer;
  transition: all var(--transition-base);
}

.chat-fab:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-xl);
  background: var(--color-accent-dark);
}

.chat-panel {
  width: min(420px, calc(100vw - 32px));
  height: min(620px, calc(100vh - 100px));
  background: var(--color-bg-lightest);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid var(--color-black);
}

.chat-header {
  background: var(--color-primary-dark);
  padding: var(--spacing-lg);
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--color-bg-lightest);
}

.chat-name {
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-lg);
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
}

.badge {
  background: rgba(255,255,255,0.2);
  font-size: var(--font-size-xs);
  padding: 2px 8px;
  border-radius: var(--radius-full);
  font-weight: normal;
}

.chat-subtitle {
  font-size: var(--font-size-xs);
  color: var(--color-gray-300);
  margin-top: 2px;
}

.chat-actions {
  display: flex;
  gap: var(--spacing-sm);
}

.chat-icon-btn {
  background: none;
  border: none;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  opacity: 0.8;
  transition: opacity var(--transition-fast);
}

.chat-icon-btn:hover {
  opacity: 1;
}

.chat-body {
  flex: 1;
  overflow-y: auto;
  padding: var(--spacing-md);
  background: var(--color-bg-lightest);
}

.topq {
  background: white;
  border-radius: var(--radius-lg);
  padding: var(--spacing-md);
  margin-bottom: var(--spacing-md);
  border: 1px solid var(--color-gray-200);
}

.topq-title {
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-sm);
  font-size: var(--font-size-sm);
}

.topq-list {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.topq-item {
  text-align: left;
  background: var(--color-gray-50);
  border: none;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  display: flex;
  justify-content: space-between;
  gap: var(--spacing-sm);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.topq-item:hover {
  background: var(--color-gray-200);
  transform: translateX(2px);
}

.msgs {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.msg[data-role='user'] {
  display: flex;
  justify-content: flex-end;
}

.bubble {
  max-width: 85%;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: 20px;
  background: var(--color-gray-700);
  box-shadow: var(--shadow-xs);
  border: 1px solid var(--color-gray-200);
}

.msg[data-role='user'] .bubble {
  background: var(--color-primary-dark);
  color: white;
  border: none;
}

.text {
  font-size: var(--font-size-sm);
  line-height: var(--line-height-normal);
  white-space: pre-wrap;
}

.text strong {
  font-weight: var(--font-weight-bold);
}

.text em {
  font-style: italic;
}

.sources {
  margin-top: var(--spacing-md);
  padding-top: var(--spacing-md);
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.sources-text {
  font-size: var(--font-size-xs);
  color: var(--color-gray-600);
  line-height: var(--line-height-normal);
}

.msg[data-role='user'] .sources-text {
  color: rgba(255, 255, 255, 0.8);
}

.chat-footer {
  padding: var(--spacing-md);
  border-top: 1px solid var(--color-gray-200);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.log-toggle {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  font-size: var(--font-size-xs);
  color: var(--color-gray-900);
}

.composer {
  display: flex;
  gap: var(--spacing-sm);
}

.composer-input {
  flex: 1;
  padding: var(--spacing-sm) var(--spacing-md);
  border: 1px solid var(--color-gray-300);
  border-radius: var(--radius-full);
  font-size: var(--font-size-sm);
  outline: none;
  transition: border var(--transition-fast);
}

.composer-input:focus {
  border-color: var(--color-accent);
  box-shadow: 0 0 0 2px rgba(16,185,129,0.2);
}

.composer-send {
  background: var(--color-accent-alt);
  border: none;
  padding: var(--spacing-sm) var(--spacing-lg);
  border-radius: var(--radius-full);
  color: white;
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: background var(--transition-fast);
}

.composer-send:hover:not(:disabled) {
  background: var(--color-accent-dark);
}

.hint {
  font-size: var(--font-size-xs);
  color: var(--color-accent-alt-1);
  text-align: center;
}
</style>