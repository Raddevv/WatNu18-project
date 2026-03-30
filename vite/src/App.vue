<template>
  <div id="app">
    <Header />
    <main class="main-content">
      <!-- Progress banner -->
      <div class="progress-banner">
        <div class="progress-content">
          <div class="progress-text">
            <h3>Jouw 18e jaar checklist</h3>
            <p>Je bent <strong>{{ overallProgress }}% voorbereid</strong> blijf zo doorgaan!</p>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: overallProgress + '%' }"></div>
          </div>
          <div class="progress-items">
            <div v-for="(feat, idx) in features" :key="idx" class="progress-item" :class="{ done: feat.completed }">
              <span class="icon">{{ feat.completed ? '✓' : idx+1 }}</span>
              <span class="label">{{ feat.titleShort }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Hero -->
      <section class="hero">
        <div class="hero-content">
          <h1 class="hero-title">Van 17 naar 18<br><span>Alles geregeld?</span></h1>
          <p class="hero-subtitle">Studiefinanciering, OV, zorgtoeslag, huurtoeslag, WatNu18 geeft je stap voor stap duidelijkheid. Gemaakt door MBO'ers, voor MBO'ers.</p>
          <button class="cta-btn" @click="scrollToFeatures">Start je journey →</button>
        </div>
      </section>

      <!-- 5-Step Mission -->
      <section class="features" id="features">
        <div class="features-wrapper">
          <div class="section-header">
            <h2>Jouw 5‑stappen plan</h2>
            <p>Voltooi elke missie, verdien badges en word helemaal klaar voor je 18e</p>
          </div>
          <div class="features-grid">
            <div class="feature-card" v-for="(feature, index) in features" :key="index" :class="{ completed: feature.completed }">
              <div class="feature-header">
                <span class="feature-step">{{ index + 1 }}</span>
                <span class="feature-badge" v-if="feature.completed">✓ Voltooid</span>
              </div>
              <h3>{{ feature.title }}</h3>
              <p>{{ feature.description }}</p>
              <button class="feature-btn" @click="selectFeature(index)">
                {{ feature.completed ? 'Herbekijk' : 'Start missie' }}
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- Detail panel with quiz -->
      <section class="details" v-if="selectedFeature !== null">
        <div class="details-container">
          <button class="close-btn" @click="selectedFeature = null">← Terug naar overzicht</button>
          <div class="details-content">
            <h2>{{ features[selectedFeature].title }}</h2>
            <p>{{ features[selectedFeature].longDescription }}</p>
            <div class="details-quiz" v-if="features[selectedFeature].quiz">
              <h3>🧠 Check je kennis</h3>
              <div class="quiz-question">
                <p>{{ features[selectedFeature].quiz.question }}</p>
                <div class="quiz-options" v-if="!quizAttempted || !quizResult.isCorrect">
                  <button class="quiz-option" v-for="(option, i) in features[selectedFeature].quiz.options" :key="i"
                    @click="submitQuizAnswer(i)" :class="{ selected: currentQuizAnswer === i }"
                    :disabled="quizAttempted && !quizResult.isCorrect">
                    {{ option }}
                  </button>
                </div>
                <div class="quiz-result" v-if="quizAttempted && quizResult">
                  <div class="quiz-feedback" :class="quizResult.isCorrect ? 'correct' : 'incorrect'">
                    <div class="feedback-icon">{{ quizResult.isCorrect ? '🎉' : '🔄' }}</div>
                    <div class="feedback-text">
                      <h4>{{ quizResult.isCorrect ? 'Goed gedaan!' : 'Niet helemaal' }}</h4>
                      <p>{{ quizResult.explanation }}</p>
                    </div>
                  </div>
                  <button v-if="quizResult.isCorrect" class="quiz-action-btn completed" disabled>
                    ✨ Badge verdiend
                  </button>
                  <button v-else class="quiz-action-btn retry" @click="retryQuiz">
                    Opnieuw proberen
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Why WatNu18 -->
      <section class="info-section">
        <h2>Waarom WatNu18?</h2>
        <div class="info-grid">
          <div class="info-card">
            <div class="info-icon">🎯</div>
            <h3>Speciaal voor MBO</h3>
            <p>Geen overbodige info — alleen wat jij écht nodig hebt als MBO‑student.</p>
          </div>
          <div class="info-card">
            <div class="info-icon">📋</div>
            <h3>Gebaseerd op DUO & overheid</h3>
            <p>Alle informatie up‑to‑date en betrouwbaar, getoetst door experts.</p>
          </div>
          <div class="info-card">
            <div class="info-icon">🏆</div>
            <h3>Motiverend & gamified</h3>
            <p>Verdien badges, volg je voortgang en blijf gemotiveerd.</p>
          </div>
        </div>
      </section>
    </main>
    <Footer />
    <ChatWidget />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import ChatWidget from './components/ChatWidget.vue'
import { ref, computed } from 'vue'

const selectedFeature = ref(null)
const currentQuizAnswer = ref(null)
const quizResult = ref(null)
const quizAttempted = ref(false)

const features = ref([
  {
    title: 'Studiefinanciering',
    titleShort: 'DUO',
    description: 'Begrijp hoe DUO werkt en wat je kunt aanvragen.',
    longDescription: 'Studiefinanciering van DUO is financiële ondersteuning voor studenten. Je kunt aanvragen zodra je 18 bent en een erkende opleiding volgt. Het bestaat uit een prestatiebeurs (gift) en eventueel een aanvullende beurs. Vul op tijd je aanvraag in via Mijn DUO.',
    completed: true,
    quiz: {
      question: 'Wanneer kun je studiefinanciering aanvragen?',
      correctAnswer: 1,
      options: ['Vanaf 16 jaar', 'Vanaf 18 jaar', 'Vanaf 21 jaar'],
      explanation: 'Correct! Je kunt studiefinanciering aanvragen zodra je 18 jaar bent en een erkende opleiding volgt.'
    }
  },
  {
    title: 'OV-studentenkaart',
    titleShort: 'OV',
    description: 'Reis voordelig met trein, bus en metro.',
    longDescription: 'De OV-studentenkaart geeft je gratis of met korting reizen in het weekend of doordeweeks. Je kiest een product via DUO. Let op: je moet wel voldoen aan de voorwaarden (onder andere recht op studiefinanciering).',
    completed: false,
    quiz: {
      question: 'Welke keuze kun je maken voor de OV-studentenkaart?',
      correctAnswer: 0,
      options: ['Weekend vrij of doordeweeks korting', 'Altijd 40% korting', 'Alleen in de zomer'],
      explanation: 'Je kiest bij DUO of je in het weekend gratis reist (weekend vrij) of doordeweeks 40% korting krijgt.'
    }
  },
  {
    title: 'Zorgverzekering & toeslagen',
    titleShort: 'Zorg',
    description: 'Verplichte zorgverzekering + zorgtoeslag.',
    longDescription: 'In Nederland ben je verplicht een basiszorgverzekering af te sluiten. Als je 18 wordt, moet je zelf een polis regelen. Kom je in aanmerking voor zorgtoeslag? Check je inkomen en vraag het aan bij de Belastingdienst.',
    completed: false,
    quiz: {
      question: 'Is zorgtoeslag automatisch?',
      correctAnswer: 1,
      options: ['Ja, je krijgt het vanzelf', 'Nee, je moet het zelf aanvragen', 'Alleen als je werkt'],
      explanation: 'Zorgtoeslag moet je actief aanvragen bij de Belastingdienst. Doe dit op tijd!'
    }
  },
  {
    title: 'Woonkosten & huurtoeslag',
    titleShort: 'Wonen',
    description: 'Energiekosten, huur, en huurtoeslag.',
    longDescription: 'Woonkosten zijn vaak de grootste uitgave. Als je op kamers gaat of zelfstandig woont, kun je mogelijk huurtoeslag krijgen. De voorwaarden: je huurt een zelfstandige woning, bent 18+, en voldoet aan de inkomensgrens.',
    completed: false,
    quiz: {
      question: 'Kan een MBO-student huurtoeslag krijgen?',
      correctAnswer: 0,
      options: ['Ja, onder voorwaarden', 'Nee, nooit', 'Alleen als je werkt'],
      explanation: 'Ja, als je 18+ bent, een zelfstandige woning huurt en je inkomen niet te hoog is, kun je huurtoeslag krijgen.'
    }
  },
  {
    title: 'Belangrijke documenten',
    titleShort: 'Papieren',
    description: 'ID, DigiD, bankrekening en meer.',
    longDescription: 'Zorg dat je een geldig ID‑bewijs hebt, een eigen bankrekening, je DigiD activeert, en je zaken zoals je BSN goed hebt vastgelegd. Bewaar kopieën digitaal en veilig.',
    completed: false,
    quiz: {
      question: 'Welke documenten heb je minimaal nodig als je 18 wordt?',
      correctAnswer: 2,
      options: ['Alleen ID-kaart', 'Alleen DigiD', 'ID, DigiD, bankrekening en eventueel huurcontract'],
      explanation: 'Je hebt een geldig ID, een actieve DigiD, een eigen bankrekening en bij zelfstandig wonen ook een huurcontract nodig.'
    }
  }
])

const overallProgress = computed(() => {
  const completedCount = features.value.filter(f => f.completed).length
  return Math.round((completedCount / features.value.length) * 100)
})

function scrollToFeatures() {
  document.getElementById('features')?.scrollIntoView({ behavior: 'smooth' })
}

function selectFeature(index) {
  selectedFeature.value = index
  resetQuiz()
}

function submitQuizAnswer(answerIndex) {
  if (!features.value[selectedFeature.value].quiz) return
  currentQuizAnswer.value = answerIndex
  const quiz = features.value[selectedFeature.value].quiz
  const isCorrect = answerIndex === quiz.correctAnswer
  quizAttempted.value = true
  quizResult.value = { isCorrect, explanation: quiz.explanation }
  if (isCorrect) {
    features.value[selectedFeature.value].completed = true
  }
}

function resetQuiz() {
  currentQuizAnswer.value = null
  quizResult.value = null
  quizAttempted.value = false
}

function retryQuiz() {
  resetQuiz()
}
</script>

<style>
@import './styles/variables.css';

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-family-base);
  font-size: var(--font-size-base);
  line-height: var(--line-height-normal);
  color: var(--color-gray-900);
  background: var(--color-bg-lighter);
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 var(--spacing-xl);
  width: 100%;
}

.progress-banner {
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  border-radius: var(--radius-xl);
  padding: var(--spacing-xl) var(--spacing-2xl);
  margin: var(--spacing-2xl) 0;
  color: white;
  box-shadow: var(--shadow-lg);
}

.progress-text h3 {
  font-size: var(--font-size-xl);
  margin-bottom: var(--spacing-xs);
}

.progress-text p {
  opacity: 0.9;
  margin-bottom: var(--spacing-md);
}

.progress-bar {
  height: 8px;
  background: rgba(255,255,255,0.3);
  border-radius: var(--radius-full);
  overflow: hidden;
  margin-bottom: var(--spacing-lg);
}

.progress-fill {
  height: 100%;
  background: var(--color-accent);
  border-radius: var(--radius-full);
  transition: width 0.3s ease;
}

.progress-items {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-sm);
  justify-content: space-between;
}

.progress-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  background: rgba(255,255,255,0.1);
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--radius-full);
  font-size: var(--font-size-xs);
  backdrop-filter: blur(4px);
}

.progress-item.done {
  background: var(--color-success);
}

.icon {
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.2);
  border-radius: var(--radius-full);
  font-size: 12px;
}

.hero {
  padding: var(--spacing-3xl) 0 var(--spacing-4xl);
}

.hero-title {
  font-size: var(--font-size-5xl);
  font-weight: 800;
  color: var(--color-primary);
  line-height: 1.2;
  margin-bottom: var(--spacing-lg);
}

.hero-title span {
  color: var(--color-accent);
}

.hero-subtitle {
  font-size: var(--font-size-lg);
  color: var(--color-gray-600);
  max-width: 600px;
  margin-bottom: var(--spacing-2xl);
}

.cta-btn {
  background: linear-gradient(135deg, var(--color-cta), var(--color-cta-dark));
  border: none;
  padding: var(--spacing-md) var(--spacing-2xl);
  border-radius: var(--radius-full);
  font-weight: var(--font-weight-bold);
  color: white;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  font-size: var(--font-size-base);
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.features {
  padding: var(--spacing-3xl) 0;
  background: var(--color-bg-lighter);
  border-radius: var(--radius-xl);
  margin: var(--spacing-2xl) 0;
}

.section-header {
  text-align: center;
  margin-bottom: var(--spacing-3xl);
}

.section-header h2 {
  font-size: var(--font-size-3xl);
  color: var(--color-primary);
  margin-bottom: var(--spacing-sm);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: var(--spacing-xl);
}

.feature-card {
  background: var(--color-bg-lightest);
  border-radius: var(--radius-lg);
  padding: var(--spacing-xl);
  border: 0.5px inset var(--color-bg);
  transition: all 0.25s;
}

.feature-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-accent);
}

.feature-card.completed {
  border-left: 4px solid var(--color-success);
  background: linear-gradient(145deg, white, var(--color-success-light));
}

.feature-step {
  display: inline-flex;
  width: 36px;
  height: 36px;
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-full);
  align-items: center;
  justify-content: center;
  font-weight: bold;
  margin-bottom: var(--spacing-md);
}

.feature-badge {
  background: var(--color-success);
  font-size: var(--font-size-xs);
  padding: 2px 8px;
  border-radius: var(--radius-full);
  color: white;
}

.feature-card h3 {
  margin: var(--spacing-md) 0 var(--spacing-sm);
  font-size: var(--font-size-xl);
}

.feature-btn {
  width: 100%;
  margin-top: var(--spacing-md);
  background: var(--color-primary);
  color: white;
  border: none;
  padding: var(--spacing-sm);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: background 0.2s;
}

.feature-btn:hover {
  background: var(--color-primary-light);
}

.details {
  background: var(--color-bg-lighter);
  padding: var(--spacing-3xl) var(--spacing-xl);
  border-radius: var(--radius-xl);
  margin: var(--spacing-2xl) 0;
}

.details-container {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  border-radius: var(--radius-xl);
  padding: var(--spacing-2xl);
  box-shadow: var(--shadow-lg);
}

.close-btn {
  background: none;
  border: none;
  color: var(--color-accent);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-lg);
  cursor: pointer;
}

.details-quiz {
  background: var(--color-gray-200);
  padding: var(--spacing-xl);
  border-radius: var(--radius-lg);
  margin-top: var(--spacing-xl);
}

.quiz-option {
  display: block;
  width: 100%;
  text-align: left;
  background: white;
  border: 1px solid var(--color-gray-300);
  padding: var(--spacing-sm) var(--spacing-md);
  margin-bottom: var(--spacing-sm);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all 0.2s;
}

.quiz-option:hover:not(:disabled) {
  border-color: var(--color-accent);
  background: var(--color-accent-light);
}

.quiz-feedback {
  display: flex;
  gap: var(--spacing-md);
  padding: var(--spacing-md);
  border-radius: var(--radius-lg);
  margin: var(--spacing-md) 0;
}

.quiz-feedback.correct {
  background: var(--color-success-light);
  border-left: 4px solid var(--color-success);
}

.quiz-feedback.incorrect {
  background: var(--color-warning-light);
  border-left: 4px solid var(--color-warning);
}

.feedback-icon {
  font-size: 2rem;
}

.quiz-action-btn {
  width: 100%;
  padding: var(--spacing-sm);
  border: none;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
}

.quiz-action-btn.retry {
  background: var(--color-warning);
  color: white;
}

.quiz-action-btn.completed {
  background: var(--color-success);
  color: white;
  cursor: default;
}

.info-section {
  padding: var(--spacing-3xl) 0;
}

.info-section h2 {
  text-align: center;
  font-size: var(--font-size-3xl);
  margin-bottom: var(--spacing-3xl);
  color: var(--color-primary);
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--spacing-xl);
}

.info-card {
  background: white;
  border-radius: var(--radius-lg);
  padding: var(--spacing-xl);
  text-align: center;
  border: 1px solid var(--color-gray-200);
  transition: all 0.2s;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.info-icon {
  font-size: 2.5rem;
  margin-bottom: var(--spacing-md);
}

@media (max-width: 768px) {
  .main-content {
    padding: 0 var(--spacing-md);
  }
  .hero-title {
    font-size: var(--font-size-3xl);
  }
  .progress-items {
    flex-direction: column;
    align-items: stretch;
  }
  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>