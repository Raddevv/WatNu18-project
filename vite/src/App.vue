<template>
  <div id="app">
    <Header />
    
    <main class="main-content">
      <div class="progress-banner">
        <div class="progress-content">
          <div class="progress-text">
            <h3>Je voortgang</h3>
            <p>Je bent <strong>{{ overallProgress }}% voorbereid</strong> om 18 te worden</p>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: overallProgress + '%' }"></div>
          </div>
          <div class="progress-items">
            <div class="progress-item done">
              <span class="icon">✓</span>
              <span class="label">Wat weten</span>
            </div>
            <div class="progress-item">
              <span class="icon">2</span>
              <span class="label">Studiefinanciering</span>
            </div>
            <div class="progress-item">
              <span class="icon">3</span>
              <span class="label">OV-Kaart</span>
            </div>
            <div class="progress-item">
              <span class="icon">4</span>
              <span class="label">Verzekeringen</span>
            </div>
            <div class="progress-item">
              <span class="icon">5</span>
              <span class="label">Documenten</span>
            </div>
          </div>
        </div>
      </div>

      <section class="hero">
        <div class="hero-content">
          <h1 class="hero-title">
            Klaar voor je volgende stap?
          </h1>
          <p class="hero-subtitle">
            Studiefinanciering, OV-kaart, verzekeringen — alles wat je moet weten als je 18 wordt. 
            Gemaakt door MBO-studenten, voor MBO-studenten.
          </p>
          <button class="cta-btn">Start je journey</button>
        </div>
      </section>

      <section class="features">
        <div class="features-wrapper">
          <div class="section-header">
            <h2>Your 5-Step Mission</h2>
            <p>Voltooi elk onderdeel en unlock je volgende level</p>
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
                Meer info
              </button>
            </div>
          </div>
        </div>
      </section>

      <section class="details" v-if="selectedFeature !== null">
        <div class="details-container">
          <button class="close-btn" @click="selectedFeature = null">← Terug</button>
          
          <div class="details-content">
            <h2>{{ features[selectedFeature].title }}</h2>
            <p>{{ features[selectedFeature].longDescription }}</p>
            
            <div class="details-quiz" v-if="features[selectedFeature].quiz">
              <h3>Controleer je kennis</h3>
              <div class="quiz-question">
                <p>{{ features[selectedFeature].quiz.question }}</p>
                
                <div class="quiz-options" v-if="!quizAttempted || !quizResult.isCorrect">
                  <button 
                    class="quiz-option" 
                    v-for="(option, i) in features[selectedFeature].quiz.options" 
                    :key="i"
                    @click="submitQuizAnswer(i)"
                    :class="{ 
                      selected: currentQuizAnswer === i,
                      disabled: quizAttempted 
                    }"
                    :disabled="quizAttempted && !quizResult.isCorrect"
                  >
                    {{ option }}
                  </button>
                </div>
                
                <div class="quiz-result" v-if="quizAttempted && quizResult">
                  <div class="quiz-feedback" :class="quizResult.isCorrect ? 'correct' : 'incorrect'">
                    <div class="feedback-icon">
                      {{ quizResult.isCorrect ? '✓' : '✗' }}
                    </div>
                    <div class="feedback-text">
                      <h4>{{ quizResult.isCorrect ? 'Correct beantwoord!' : 'Helaas, dit is niet correct' }}</h4>
                      <p>{{ quizResult.explanation }}</p>
                    </div>
                  </div>
                  
                  <button v-if="quizResult.isCorrect" class="quiz-action-btn completed" disabled>
                    ✓ Badge Unlocked!
                  </button>
                  <button v-else class="quiz-action-btn retry" @click="retryQuiz">
                    Probeer opnieuw
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="info-section">
        <h2>Waarom WatNu18?</h2>
        <div class="info-grid">
          <div class="info-card">
            <div class="info-icon"></div>
            <h3>Gericht</h3>
            <p>Speciaal gemaakt voor MBO-studenten. Geen overbodige informatie.</p>
          </div>
          <div class="info-card">
            <div class="info-icon"></div>
            <h3>Betrouwbaar</h3>
            <p>Alle informatie gebaseerd op officiële overheids- en organisatiedata.</p>
          </div>
          <div class="info-card">
            <div class="info-icon"></div>
            <h3>Motiverend</h3>
            <p>Voltooi stappen, earn badges, voel je voorbereid.</p>
          </div>
        </div>
      </section>
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import { ref, computed } from 'vue'

const selectedFeature = ref(null)
const currentQuizAnswer = ref(null)
const quizResult = ref(null)
const quizAttempted = ref(false)

const features = ref([
  {
    title: 'Studiefinanciering',
    description: 'Begrijp hoe DUO werkt en wat je kunt aanvragen.',
    longDescription: 'Studiefinanciering van DUO is financiële ondersteuning voor studenten. Je kunt aanvragen als je 18 bent en aan een erkende onderwijsinstelling studeert. Dit kan bestaan uit gift of lening. Met studiefinanciering kun je je studiemateriaal kopen, je huisvesting betalen, en andere kosten dekken.',
    completed: true,
    quiz: {
      question: 'Wanneer kun je studiefinanciering aanvragen?',
      correctAnswer: 1,
      options: ['Als je 16 bent', 'Als je 18 bent', 'Als je 21 bent'],
      explanation: 'Correct! Je kunt studiefinanciering aanvragen wanneer je 18 bent en een erkende opleiding volgt.'
    }
  },
  {
    title: 'OV-Studentenkaart',
    description: 'Reis voordelig met openbaar vervoer.',
    longDescription: 'De OV-studentenkaart geeft je korting op je reiskosten. Perfect voor dagelijks pendelen naar school. Als fulltime student krijg je korting op je OV-reis. Controleer altijd je rechten op stoptreinen.nl.',
    completed: false,
    quiz: {
      question: 'Welke korting krijg je maximaal met de OV-studentenkaart?',
      correctAnswer: 2,
      options: ['25% korting', '30% korting', '40% korting'],
      explanation: 'Correct! Met een geldig studentenkaart krijg je maximaal 40% korting op reizen buiten de filerijden.'
    }
  },
  {
    title: 'Zorgverzekering',
    description: 'Verzeker jezelf tegen onvoorziene kosten.',
    longDescription: 'Zorgverzekering is verplicht in Nederland. Kies een passende polis en check je inkomsten. Als je inkomsten laag zijn, kun je zorgtoeslag aanvragen. Controleer jaarlijks of je verzekering nog goed voor je is.',
    completed: false,
    quiz: {
      question: 'Is zorgverzekering verplicht in Nederland?',
      correctAnswer: 0,
      options: ['Ja, iedereen moet verzekerd zijn', 'Nee, het is optioneel', 'Ja, maar alleen voor werkenden'],
      explanation: 'Correct! Zorgverzekering is verplicht voor iedereen in Nederland die hier woont of werkt.'
    }
  },
  {
    title: 'Woonkosten',
    description: 'Begrip energiekosten, huur en toeslag.',
    longDescription: 'Woonkosten zijn een groot deel van je budget. Leer hoe je dit insteelt en waar toeslag mogelijk is. Energiekosten kunnen variëren per seizoen. Met huurtoeslag kun je je huur gedeeltelijk terugkrijgen.',
    completed: false,
    quiz: {
      question: 'Kan je huurtoeslag aanvragen als student?',
      correctAnswer: 0,
      options: ['Ja, mits je voldoet aan bepaalde voorwaarden', 'Nee, alleen voor ouders', 'Ja, iedereen krijgt het'],
      explanation: 'Correct! Als student kun je huurtoeslag aanvragen als je voldoet aan de inkomsteneis en huurmin.'
    }
  },
  {
    title: 'Documenten',
    description: 'Zet alles op papier wat je nodig hebt.',
    longDescription: 'Van aanvraagformulieren tot contracten — zet alles goed op papier. Bewaar kopieën van je belangrijkste documenten. Een echte origineel document ben je altijd beter uit. Maak digitale backups van je documenten.',
    completed: false,
    quiz: {
      question: 'Welke documenten zijn essentieel wanneer je 18 bent?',
      correctAnswer: 2,
      options: ['Alleen je ID', 'Je paspoort', 'ID, huiscontract, en bankrekeninggegevens'],
      explanation: 'Correct! Je hebt je ID, een huiscontract, en bankrekeninggegevens nodig voor veel officiële zaken.'
    }
  }
])

const overallProgress = computed(() => {
  const completedCount = features.value.filter(f => f.completed).length
  return Math.round((completedCount / features.value.length) * 100)
})

function selectFeature(index) {
  selectedFeature.value = selectedFeature.value === index ? null : index
  if (selectedFeature.value === null) {
    resetQuiz()
  }
}

function submitQuizAnswer(answerIndex) {
  if (!features.value[selectedFeature.value].quiz) return
  
  currentQuizAnswer.value = answerIndex
  const quiz = features.value[selectedFeature.value].quiz
  const isCorrect = answerIndex === quiz.correctAnswer
  
  quizAttempted.value = true
  quizResult.value = {
    isCorrect,
    explanation: quiz.explanation
  }
  
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
  color: var(--color-gray-700);
  background-color: var(--color-gray-50);
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  position: relative;
}

.main-content {
  flex: 1;
  width: 100%;
}

.progress-banner {
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  color: white;
  padding: var(--spacing-2xl) var(--spacing-xl);
  box-shadow: 0 8px 24px var(--color-accent), var(--shadow-md);
  animation: bannerPulse 4s ease-in-out infinite;
}

@keyframes bannerPulse {
  0%, 100% {
    box-shadow: 0 8px 24px var(--color-accent-lighter), var(--shadow-md);
  }
  50% {
    box-shadow: 0 8px 32px var(--color-accent-light), var(--shadow-lg);
  }
}

.progress-content {
  max-width: 1200px;
  margin: 0 auto;
}

.progress-text {
  margin-bottom: var(--spacing-lg);
}

.progress-text h3 {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-medium);
  margin-bottom: var(--spacing-sm);
}

.progress-text p {
  font-size: var(--font-size-base);
  opacity: 0.95;
}

.progress-text strong {
  font-weight: var(--font-weight-bold);
}

.progress-bar {
  width: 100%;
  height: 8px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-full);
  overflow: hidden;
  margin-bottom: var(--spacing-lg);
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--color-accent) 0%, var(--color-accent-light) 100%);
  border-radius: var(--radius-full);
  transition: width var(--transition-slowest);
  box-shadow: 0 0 16px rgba(0, 0, 0, 0.4);
  position: relative;
}

.progress-fill::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-full);
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  animation: progressShine 3.5s linear infinite;
}

@keyframes progressShine {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(1000%);
  }
}

.progress-items {
  display: flex;
  gap: var(--spacing-md);
  flex-wrap: wrap;
  justify-content: space-between;
}

.progress-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  font-size: var(--font-size-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  background-color: rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-lg);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0, 0, 0, 0.2);
  transition: all var(--transition-base);
}

.progress-item:hover {
  background-color: rgba(57, 57, 57, 0.15);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px var(--color-primary);
  border-color: var(--color-accent-dark);
}

.progress-item.done {
  background-color: rgba(22, 163, 74, 0.3);
}

.progress-item .icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-full);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-bold);
}

.progress-item.done .icon {
  background-color: var(--color-success);
}

.hero {
  background: linear-gradient(135deg, var(--color-white) 0%, var(--color-gray-50) 100%);
  padding: var(--spacing-3xl) var(--spacing-xl) calc(var(--spacing-3xl) * 1.5) var(--spacing-xl);
  text-align: center;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero-title {
  font-size: var(--font-size-5xl);
  font-weight: var(--font-weight-bold);
  color: var(--color-primary);
  line-height: var(--line-height-tight);
  margin-bottom: var(--spacing-lg);
  letter-spacing: -0.5px;
  position: relative;
  padding-bottom: var(--spacing-lg);
}

.hero-subtitle {
  font-size: var(--font-size-lg);
  color: var(--color-gray-600);
  line-height: var(--line-height-relaxed);
  margin-bottom: var(--spacing-2xl);
  letter-spacing: 0.3px;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.cta-btn {
  display: inline-block;
  padding: var(--spacing-md) var(--spacing-2xl);
  background-color: var(--color-accent);
  color: white;
  border: 2px solid transparent;
  border-radius: var(--radius-lg);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: all var(--transition-base);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.4), var(--shadow-md);
  position: relative;
  overflow: hidden;
  animation: glowPulse 10s ease-in-out infinite;
}

@keyframes glowPulse {
  0%, 100% {
    box-shadow: 0 0 20px rgb(185, 185, 185), var(--shadow-md);
  }
  50% {
    box-shadow: 0 0 30px rrgb(43, 43, 43) 0 0 40px rgb(105, 105, 105), var(--shadow-lg);
  }
}

.cta-btn::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(.5deg, transparent 40%, rgba(255, 255, 255, 0.45) 50%, transparent 60%);
  border-radius: var(--radius-lg);
  animation: glintSweep 2.1s linear infinite; 
}

.cta-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 40px rgba(8, 145, 178, 0.7), 0 0 60px rgba(8, 145, 178, 0.4), var(--shadow-lg);
  border-color: white;
}

@keyframes glintSweep {
  0% {
    transform: translateX(-100%) translateY(-100%) rotate(45deg);
  }
  50% {
    transform: translateX(0) translateY(0) rotate(45deg);
  }
  100% {
    transform: translateX(100%) translateY(100%) rotate(45deg);
  }
}

.features {
  padding: calc(var(--spacing-3xl) * 1.2) var(--spacing-xl);
  background-color: var(--color-white);
  border-top: 1px solid var(--color-gray-200);
}

.features-wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: var(--spacing-3xl);
  position: relative;
  padding-bottom: var(--spacing-lg);
}

.section-header h2 {
  font-size: var(--font-size-4xl);
  color: var(--color-primary);
  margin-bottom: var(--spacing-md);
  font-weight: var(--font-weight-bold);
  letter-spacing: -0.5px;
}

.section-header p {
  font-size: var(--font-size-lg);
  color: var(--color-gray-500);
  letter-spacing: 0.3px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--spacing-xl);
}

.feature-card {
  background: white;
  border: 2px solid var(--color-gray-200);
  border-radius: var(--radius-lg);
  padding: var(--spacing-xl);
  transition: all var(--transition-base);
  position: relative;
  overflow: hidden;
}

.feature-card:hover {
  border-color: var(--color-black);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
  transform: translateY(-6px);
}

.feature-card.completed {
  border-color: var(--color-success);
  background: linear-gradient(135deg, white 0%, var(--color-success-light) 100%);
  position: relative;
}

.feature-card.completed:after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  background: linear-gradient(135deg, transparent, rgba(30, 153, 114, 0.1), transparent);
}

.feature-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--spacing-lg);
}

.feature-step {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  color: white;
  border-radius: var(--radius-full);
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-bold);
  box-shadow: 0 4px 12px rgba(44, 44, 44, 0.2);
  transition: all var(--transition-base);
}

.feature-card:hover .feature-step {
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
}

.feature-badge {
  display: inline-block;
  padding: var(--spacing-sm) var(--spacing-md);
  background-color: var(--color-success);
  color: white;
  border-radius: var(--radius-md);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-semibold);
}

.feature-card h3 {
  font-size: var(--font-size-xl);
  color: var(--color-primary);
  margin-bottom: var(--spacing-md);
  font-weight: var(--font-weight-bold);
}

.feature-card p {
  font-size: var(--font-size-base);
  color: var(--color-gray-600);
  line-height: var(--line-height-normal);
  margin-bottom: var(--spacing-lg);
}

.feature-btn {
  width: 100%;
  padding: var(--spacing-md);
  background-color: var(--color-primary);
  color: var(--color-white);
  border: 2px solid var(--color-primary);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: all var(--transition-base);
  position: relative;
  overflow: hidden;
}

.feature-btn:hover {
  background-color: var(--color-black);
  color: white;
  box-shadow: 0 4px 16px rgba(44, 44, 44, 0.25);
}

.details {
  background: linear-gradient(135deg, var(--color-primary-lighter) 0%, var(--color-accent-lighter) 100%);
  padding: var(--spacing-3xl) var(--spacing-xl);
  border-top: 4px solid var(--color-primary);
}

.details-container {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  border-radius: var(--radius-lg);
  padding: var(--spacing-2xl);
  box-shadow: 0 20px 50px rgba(41, 209, 172, 0.2);
  border: 1px solid rgba(41, 209, 172, 0.15);
  animation: slideIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.close-btn {
  background: none;
  border: none;
  color: var(--color-primary);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  margin-bottom: var(--spacing-lg);
  transition: all var(--transition-base);
}

.close-btn:hover {
  color: var(--color-primary-dark);
  transform: translateX(-4px);
}

.details-content h2 {
  font-size: var(--font-size-3xl);
  color: var(--color-primary);
  margin-bottom: var(--spacing-lg);
  letter-spacing: -0.3px;
  position: relative;
  padding-bottom: var(--spacing-md);
}

.details-content h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 2px;
  background: linear-gradient(90deg, var(--color-accent), transparent);
  border-radius: var(--radius-full);
}

.details-content p {
  font-size: var(--font-size-base);
  color: var(--color-gray-700);
  line-height: var(--line-height-relaxed);
  margin-bottom: var(--spacing-lg);
}

.details-quiz {
  background-color: var(--color-accent-lighter);
  border: 2px solid var(--color-accent);
  border-radius: var(--radius-lg);
  padding: var(--spacing-xl);
  margin-top: var(--spacing-xl);
}

.details-quiz h3 {
  font-size: var(--font-size-lg);
  color: var(--color-primary);
  margin-bottom: var(--spacing-lg);
}

.quiz-question p {
  font-size: var(--font-size-base);
  color: var(--color-gray-700);
  margin-bottom: var(--spacing-lg);
  font-weight: var(--font-weight-semibold);
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.quiz-option {
  padding: var(--spacing-md);
  background-color: white;
  border: 2px solid var(--color-gray-200);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--transition-base);
  font-size: var(--font-size-base);
  text-align: left;
  position: relative;
  overflow: hidden;
}

.quiz-option::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(41, 209, 172, 0.1), transparent);
  transition: left var(--transition-base);
}

.quiz-option:hover:not(.disabled) {
  border-color: var(--color-accent);
  background-color: rgba(41, 209, 172, 0.08);
  transform: translateX(6px);
  box-shadow: 0 4px 12px rgba(41, 209, 172, 0.15);
}

.quiz-option:hover:not(.disabled)::before {
  left: 100%;
}

.quiz-option.selected {
  border-color: var(--color-accent);
  background: linear-gradient(135deg, rgba(41, 209, 172, 0.1) 0%, rgba(41, 209, 172, 0.05) 100%);
  font-weight: var(--font-weight-semibold);
  box-shadow: 0 4px 12px rgba(41, 209, 172, 0.2);
}

.quiz-option.disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.quiz-result {
  margin-top: var(--spacing-lg);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.quiz-feedback {
  display: flex;
  gap: var(--spacing-lg);
  padding: var(--spacing-lg);
  border-radius: var(--radius-lg);
  border: 2px solid;
  background-color: var(--color-gray-50);
  margin-bottom: var(--spacing-lg);
}

.quiz-feedback.correct {
  border-color: var(--color-success);
  background: linear-gradient(135deg, white 0%, var(--color-success-light) 100%);
}

.quiz-feedback.incorrect {
  border-color: var(--color-warning);
  background: linear-gradient(135deg, white 0%, var(--color-warning-light) 100%);
}

.feedback-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 50px;
  width: 50px;
  height: 50px;
  border-radius: var(--radius-full);
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  color: white;
}

.quiz-feedback.correct .feedback-icon {
  background-color: var(--color-success);
}

.quiz-feedback.incorrect .feedback-icon {
  background-color: var(--color-warning);
}

.feedback-text h4 {
  font-size: var(--font-size-base);
  color: var(--color-gray-900);
  margin-bottom: var(--spacing-sm);
  font-weight: var(--font-weight-bold);
}

.feedback-text p {
  font-size: var(--font-size-sm);
  color: var(--color-gray-700);
  margin: 0;
}

.quiz-action-btn {
  display: block;
  width: 100%;
  padding: var(--spacing-md);
  border: none;
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: all var(--transition-base);
}

.quiz-action-btn.retry {
  background-color: var(--color-warning);
  color: white;
}

.quiz-action-btn.retry:hover {
  background-color: var(--color-warning-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.quiz-action-btn.completed {
  background: linear-gradient(135deg, var(--color-success) 0%, var(--color-success-dark) 100%);
  color: white;
  cursor: default;
}

/* Responsive Quiz */
@media (max-width: 768px) {
  .quiz-feedback {
    flex-direction: column;
    gap: var(--spacing-md);
  }

  .feedback-icon {
    min-width: 40px;
    width: 40px;
    height: 40px;
    font-size: var(--font-size-xl);
  }
}

.info-section {
  padding: var(--spacing-3xl) var(--spacing-xl);
  background-color: var(--color-gray-50);
}

.info-section h2 {
  font-size: var(--font-size-4xl);
  color: var(--color-primary);
  text-align: center;
  margin-bottom: var(--spacing-3xl);
  font-weight: var(--font-weight-bold);
}

.info-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-xl);
}

.info-card {
  background: white;
  border-radius: var(--radius-lg);
  padding: var(--spacing-sm);
  text-align: center;
  box-shadow: var(--shadow-md);
  transition: all var(--transition-base);
  border: 1px solid transparent;
  position: relative;
  overflow: hidden;
}

.info-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, transparent, rgba(255, 255, 255, 0.05), transparent);
  opacity: 0;
  transition: opacity var(--transition-base);
}

.info-card:hover {
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
  transform: translateY(-6px);
  border-color: rgba(0, 0, 0, 0.2);
}

.info-card:hover::before {
  opacity: 1;
}

.info-icon {
  font-size: var(--font-size-5xl);
  margin-bottom: var(--spacing-lg);
  display: inline-block;
  transition: transform var(--transition-base);
}

.info-card:hover .info-icon {
  transform: scale(1.15) rotate(5deg);
}

.info-card h3 {
  font-size: var(--font-size-xl);
  color: var(--color-primary);
  margin-bottom: var(--spacing-md);
  font-weight: var(--font-weight-bold);
  letter-spacing: -0.3px;
}

.info-card p {
  font-size: var(--font-size-base);
  color: var(--color-gray-600);
  line-height: var(--line-height-relaxed);
}

@media (max-width: 768px) {
  .hero-title {
    font-size: var(--font-size-3xl);
  }

  .hero-subtitle {
    font-size: var(--font-size-base);
  }

  .progress-items {
    flex-direction: column;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .section-header h2 {
    font-size: var(--font-size-2xl);
  }
}

@media (max-width: 480px) {
  .progress-banner {
    padding: var(--spacing-lg) var(--spacing-md);
  }

  .hero {
    padding: var(--spacing-2xl) var(--spacing-md);
  }

  .hero-title {
    font-size: var(--font-size-2xl);
  }

  .hero-subtitle {
    font-size: var(--font-size-sm);
  }

  .features {
    padding: var(--spacing-2xl) var(--spacing-md);
  }

  .feature-card {
    padding: var(--spacing-lg);
  }

  .details-container {
    padding: var(--spacing-lg);
  }

  .info-icon {
    font-size: var(--font-size-4xl);
  }
}
</style>
