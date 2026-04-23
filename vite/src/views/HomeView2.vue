<template>
  <main class="main-content">
    <div class="progress-banner">
      <div class="progress-content">
        <div class="progress-text">
          <h3>Jouw 18e jaar checklist</h3>
          <p>
            Je bent <strong>{{ overallProgress }}% voorbereid</strong> — blijf
            zo doorgaan!
          </p>
        </div>
        <div class="progress-bar">
          <div
            class="progress-fill"
            :style="{ width: overallProgress + '%' }"
          ></div>
        </div>
        <div class="progress-items">
          <div
            v-for="(feat, idx) in features"
            :key="idx"
            class="progress-item"
            :class="{ done: feat.completed }"
          >
            <span class="icon">{{ feat.completed ? "✓" : idx + 1 }}</span>
            <span class="label">{{ feat.titleShort }}</span>
          </div>
        </div>
      </div>
    </div>

    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">
          Van 17 naar 18<br /><span>Alles geregeld?</span>
        </h1>
        <p class="hero-subtitle">
          Studiefinanciering, OV, zorgtoeslag, huurtoeslag — WatNu18 geeft je
          stap voor stap duidelijkheid. Gemaakt door MBO'ers, voor MBO'ers.
        </p>
        <button class="cta-btn" @click="scrollToFeatures">
          Start je journey →
        </button>
      </div>
    </section>

    <section class="features" id="features">
      <div class="features-wrapper">
        <div class="section-header">
          <h2>Jouw 5‑stappen plan</h2>
          <p>Voltooi elke missie, verdien badges en word klaar voor je 18e</p>
        </div>
        <div class="features-grid">
          <div
            class="feature-card"
            v-for="(feature, index) in features"
            :key="index"
            :class="{ completed: feature.completed }"
          >
            <div class="feature-header">
              <span class="feature-step">{{ index + 1 }}</span>
              <span class="feature-badge" v-if="feature.completed"
                >✓ Voltooid</span
              >
            </div>
            <h3>{{ feature.title }}</h3>
            <p>{{ feature.description }}</p>
            <button class="feature-btn" @click="selectFeature(index)">
              {{ feature.completed ? "Herbekijk" : "Start missie" }}
            </button>
          </div>
        </div>
      </div>
    </section>

    <section class="details" v-if="selectedFeature !== null">
      <div class="details-container">
        <button class="close-btn" @click="selectedFeature = null">
          ← Terug naar overzicht
        </button>
        <div class="details-content">
          <h2>{{ features[selectedFeature].title }}</h2>
          <p>{{ features[selectedFeature].longDescription }}</p>
          <div class="details-quiz" v-if="features[selectedFeature].quiz">
            <h3>🧠 Check je kennis</h3>
            <p>{{ features[selectedFeature].quiz.question }}</p>
            <div class="quiz-options">
              <button
                v-for="(option, i) in features[selectedFeature].quiz.options"
                :key="i"
                @click="submitQuizAnswer(i)"
                :class="{ selected: currentQuizAnswer === i }"
                :disabled="quizAttempted && !quizResult.isCorrect"
              >
                {{ option }}
              </button>
            </div>
            <div v-if="quizAttempted && quizResult" class="quiz-result">
              <p :class="quizResult.isCorrect ? 'correct' : 'incorrect'">
                {{ quizResult.isCorrect ? "Goed gedaan!" : "Niet helemaal" }}
              </p>
              <p>{{ quizResult.explanation }}</p>
            </div>
            <button
              v-if="quizResult?.isCorrect"
              class="quiz-action-btn completed"
              disabled
            >
              ✨ Badge verdiend
            </button>
            <button v-else class="quiz-action-btn retry" @click="retryQuiz">
              Opnieuw proberen
            </button>
          </div>
        </div>
      </div>
    </section>

    <section class="info-section">
      <h2>Waarom WatNu18?</h2>
      <div class="info-grid">
        <div class="info-card">
          <h3>Speciaal voor MBO</h3>
          <p>Geen overbodige info — alleen wat jij echt nodig hebt.</p>
        </div>
        <div class="info-card">
          <h3>Gebaseerd op DUO & overheid</h3>
          <p>Betrouwbare en actuele informatie.</p>
        </div>
        <div class="info-card">
          <h3>Motiverend & gamified</h3>
          <p>Verdien badges en blijf gemotiveerd.</p>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, computed } from "vue";

const selectedFeature = ref(null);
const currentQuizAnswer = ref(null);
const quizResult = ref(null);
const quizAttempted = ref(false);

const features = ref([
  {
    title: "Studiefinanciering",
    titleShort: "DUO",
    description: "Begrijp hoe DUO werkt en wat je kunt aanvragen.",
    longDescription: "Alles over studiefinanciering en terugbetaling.",
    completed: false,
    quiz: {
      question: "Welk document heb je nodig voor DUO?",
      options: ["Paspoort", "BSN", "Telefoon"],
      answerIndex: 1,
      explanation: "Je BSN is nodig om je bij DUO te identificeren.",
    },
  },
  {
    title: "Zorgverzekering",
    titleShort: "Zorg",
    description: "Regel je zorgverzekering en toeslagen.",
    longDescription: "Je bent verplicht een basisverzekering te hebben.",
    completed: false,
    quiz: {
      question: "Is zorgtoeslag automatisch?",
      options: ["Ja", "Nee", "Soms"],
      answerIndex: 1,
      explanation: "Je moet zorgtoeslag zelf aanvragen.",
    },
  },
]);

const overallProgress = computed(() =>
  Math.round(
    (features.value.filter((f) => f.completed).length / features.value.length) *
      100,
  ),
);

function scrollToFeatures() {
  document.getElementById("features")?.scrollIntoView({ behavior: "smooth" });
}

function selectFeature(index) {
  selectedFeature.value = index;
  currentQuizAnswer.value = null;
  quizResult.value = null;
  quizAttempted.value = false;
}

function submitQuizAnswer(index) {
  quizAttempted.value = true;
  currentQuizAnswer.value = index;
  const quiz = features.value[selectedFeature.value].quiz;
  const isCorrect = index === quiz.answerIndex;
  quizResult.value = { isCorrect, explanation: quiz.explanation };
  if (isCorrect) features.value[selectedFeature.value].completed = true;
}

function retryQuiz() {
  currentQuizAnswer.value = null;
  quizResult.value = null;
  quizAttempted.value = false;
}
</script>

<style scoped>
.main-content {
  padding: 2rem;
  max-width: 1100px;
  margin: auto;
}
.progress-banner {
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, #3b82f6, #1e40af);
  color: #fff;
  border-radius: 12px;
  padding: 1rem;
}
.hero {
  margin-bottom: 2rem;
  text-align: center;
}
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
.feature-card {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 1rem;
  background: white;
}
.details-container {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 1rem;
  background: #f8fafc;
  margin-top: 1rem;
}
.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}
</style>
