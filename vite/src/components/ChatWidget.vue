<template>
  <div class="chat-root" :data-open="open ? 'true' : 'false'">
    <button v-if="!open" class="chat-fab" @click="openChat" aria-expanded="false">
      <span>Chat</span>
    </button>

    <div v-if="open" class="chat-panel" role="dialog" aria-label="WatNu18 Chatbot">
      <div class="chat-header">
        <div class="chat-title">
          <div class="chat-name">Noa.</div>
          <div class="chat-subtitle">Stel je vraag over studiefinanciering, OV, toeslagen, etc.</div>
        </div>
        <div class="chat-actions">
          <button class="chat-link-btn" @click="newChat" :disabled="streaming">
            New chat
          </button>
          <button class="chat-icon-btn" @click="open = false" aria-label="Sluiten">✕</button>
        </div>
      </div>

      <div class="chat-body" ref="scrollEl">
        <div v-if="topQuestions.length" class="topq">
          <div class="topq-title">Top vragen</div>
          <div class="topq-list">
            <button
              v-for="q in topQuestions"
              :key="q.id"
              class="topq-item"
              @click="askTopQuestion(q.question)"
              :title="`${q.count}× gevraagd`"
            >
              <span class="topq-q">{{ q.question }}</span>
              <span class="topq-count">{{ q.count }}×</span>
            </button>
          </div>
        </div>

        <div class="msgs">
          <div v-for="(m, idx) in messages" :key="idx" class="msg" :data-role="m.role">
            <div class="bubble">
              <div class="text" v-text="m.content"></div>
            </div>
          </div>
          <div v-if="streaming" class="msg" data-role="assistant">
            <div class="bubble">
              <div class="text">{{ draftAssistant || '...' }}</div>
            </div>
          </div>
        </div>
      </div>

      <div class="chat-footer">
        <label class="log-toggle">
          <input type="checkbox" v-model="logToFaq" />
          <span>Deze vraag anoniem toevoegen aan “Top vragen”</span>
        </label>

        <form class="composer" @submit.prevent="send">
          <input
            v-model="input"
            class="composer-input"
            type="text"
            placeholder="Typ je vraag…"
            :disabled="streaming"
            @keydown.enter.exact.prevent="send"
          />
          <button class="composer-send" type="submit" :disabled="streaming || !input.trim()">
            Verstuur
          </button>
        </form>
        <div class="hint">
          Tip: noem je opleiding/woon-situatie als dat relevant is. Deel geen BSN of privégegevens.
        </div>
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
  const l = browserLocale.value.toLowerCase()
return "Hoi! Ik ben Noa, de WatNu18 assistent. Stel mij gerust vragen over alles gerelateerd aan JOUW studiefinancering!"
}

const messages = ref([
  {
    role: 'assistant',
    content: initialGreeting()
  }
])

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
  } catch {
    // ignore
  }
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
      ...messages.value.slice(-6).map((m) => ({ role: m.role, content: m.content })),
      { role: 'user', content: userText }
    ]
  }
}

function newChat() {
  if (activeController.value) {
    try {
      activeController.value.abort()
    } catch {
      // ignore
    }
    activeController.value = null
  }
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

    if (!res.ok || !res.body) {
      const errText = await res.text().catch(() => '')
      throw new Error(errText || `HTTP ${res.status}`)
    }

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
        const eventLine = lines.find((l) => l.startsWith('event:'))
        const dataLines = lines.filter((l) => l.startsWith('data:'))
        const data = dataLines.map((l) => l.replace(/^data:\s?/, '')).join('\n')
        const event = eventLine ? eventLine.replace('event:', '').trim() : 'message'

        if (event === 'error') {
          throw new Error(data || 'Server error')
        }
        if (event === 'done') {
          // finalize
          const finalText = (draftAssistant.value || '').trim()
          if (finalText) messages.value.push({ role: 'assistant', content: finalText })
          draftAssistant.value = ''
          streaming.value = false
          activeController.value = null
          loadTopQuestions()
          await nextTick(scrollToBottom)
          return
        }
        if (event === 'logged') {
          continue
        }
        // default: token
        if (data) {
          draftAssistant.value += data
          await nextTick(scrollToBottom)
        }
      }
    }

    const finalText = (draftAssistant.value || '').trim()
    if (finalText) messages.value.push({ role: 'assistant', content: finalText })
  } catch (e) {
    if (e?.name === 'AbortError') {
      return
    }
    messages.value.push({
      role: 'assistant',
      content:
        'Sorry — ik kan nu even geen antwoord ophalen. Als dit lokaal draait: start de backend en zet je API key of kies Ollama.'
    })
  } finally {
    draftAssistant.value = ''
    streaming.value = false
    activeController.value = null
    await nextTick(scrollToBottom)
  }
}

onMounted(() => {
  detectLocale()
  if (messages.value.length === 1 && messages.value[0].role === 'assistant') {
    messages.value[0].content = initialGreeting()
  }
  loadTopQuestions()
})
</script>

<style scoped>
.chat-root {
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 9999;
  font-family: var(--font-family-base);
}

.chat-fab {
  appearance: none;
  border: none;
  cursor: pointer;
  background: linear-gradient(135deg, var(--color-accent) 0%, var(--color-accent-light) 100%);
  color: white;
  padding: 12px 16px;
  border-radius: 999px;
  font-weight: var(--font-weight-semibold);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.2);
}

.chat-panel {
  width: min(420px, calc(100vw - 32px));
  height: min(640px, calc(100vh - 120px));
  margin-bottom: 12px;
  border-radius: 16px;
  overflow: hidden;
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
}

.chat-header {
  padding: 14px 14px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 10px;
}

.chat-name {
  font-weight: var(--font-weight-bold);
  color: var(--color-primary);
}

.chat-subtitle {
  font-size: var(--font-size-sm);
  color: var(--color-gray-600);
  margin-top: 2px;
}

.chat-icon-btn {
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 18px;
  line-height: 1;
  color: var(--color-gray-600);
}

.chat-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.chat-link-btn {
  border: none;
  background: transparent;
  cursor: pointer;
  color: var(--color-primary-light);
  font-weight: var(--font-weight-semibold);
  font-size: var(--font-size-sm);
  padding: 6px 8px;
  border-radius: 10px;
}

.chat-link-btn:hover {
  background: rgba(0, 0, 0, 0.05);
}

.chat-link-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.chat-body {
  flex: 1;
  padding: 12px;
  overflow: auto;
  background: linear-gradient(180deg, rgba(248, 250, 252, 1) 0%, rgba(255, 255, 255, 1) 100%);
}

.topq {
  margin-bottom: 12px;
  padding: 10px;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.06);
  background: rgba(255, 255, 255, 0.75);
}

.topq-title {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-gray-700);
  margin-bottom: 8px;
}

.topq-list {
  display: grid;
  gap: 8px;
}

.topq-item {
  text-align: left;
  border: 1px solid rgba(0, 0, 0, 0.08);
  background: white;
  border-radius: 10px;
  padding: 10px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  gap: 10px;
  transition: transform 120ms ease, box-shadow 120ms ease;
}

.topq-item:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}

.topq-q {
  font-size: var(--font-size-sm);
  color: var(--color-gray-800);
}

.topq-count {
  font-size: var(--font-size-xs);
  color: var(--color-gray-500);
  white-space: nowrap;
}

.msgs {
  display: grid;
  gap: 10px;
}

.msg {
  display: flex;
}

.msg[data-role='user'] {
  justify-content: flex-end;
}

.bubble {
  max-width: 85%;
  border-radius: 14px;
  padding: 10px 12px;
  border: 1px solid rgba(0, 0, 0, 0.06);
  background: white;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04);
}

.msg[data-role='user'] .bubble {
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  color: white;
  border-color: rgba(255, 255, 255, 0.15);
}

.text {
  white-space: pre-wrap;
  font-size: var(--font-size-base);
  line-height: var(--line-height-normal);
}

.chat-footer {
  border-top: 1px solid rgba(0, 0, 0, 0.08);
  padding: 12px;
  display: grid;
  gap: 10px;
}

.log-toggle {
  display: flex;
  gap: 10px;
  align-items: center;
  font-size: var(--font-size-sm);
  color: var(--color-gray-700);
}

.composer {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
}

.composer-input {
  border: 1px solid rgba(0, 0, 0, 0.12);
  border-radius: 12px;
  padding: 10px 12px;
  outline: none;
  font-size: var(--font-size-base);
}

.composer-input:focus {
  border-color: rgba(8, 145, 178, 0.6);
  box-shadow: 0 0 0 4px rgba(8, 145, 178, 0.15);
}

.composer-send {
  border: none;
  cursor: pointer;
  border-radius: 12px;
  padding: 10px 12px;
  background: var(--color-accent);
  color: white;
  font-weight: var(--font-weight-semibold);
}

.composer-send:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.hint {
  font-size: var(--font-size-xs);
  color: var(--color-gray-500);
}
</style>

