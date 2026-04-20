<template>
  <div id="app">
    <Header />
    <main class="main-content">
      <!-- Progress banner -->
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

      <!-- Hero -->
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

      <!-- 5-Step Mission -->
      <section class="features" id="features">
        <div class="features-wrapper">
          <div class="section-header">
            <h2>Jouw 5‑stappen plan</h2>
            <p>
              Voltooi elke missie, verdien badges en word helemaal klaar voor je
              18e
            </p>
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

      <!-- Detail panel with quiz -->
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
              <div class="quiz-question">
                <p>{{ features[selectedFeature].quiz.question }}</p>
                <div
                  class="quiz-options"
                  v-if="!quizAttempted || !quizResult.isCorrect"
                >
                  <button
                    class="quiz-option"
                    v-for="(option, i) in features[selectedFeature].quiz
                      .options"
                    :key="i"
                    @click="submitQuizAnswer(i)"
                    :class="{ selected: currentQuizAnswer === i }"
                    :disabled="quizAttempted && !quizResult.isCorrect"
                  >
                    {{ option }}
                  </button>
                </div>
                <div class="quiz-result" v-if="quizAttempted && quizResult">
                  <div
                    class="quiz-feedback"
                    :class="quizResult.isCorrect ? 'correct' : 'incorrect'"
                  >
                    <div class="feedback-icon">
                      {{ quizResult.isCorrect ? "🎉" : "🔄" }}
                    </div>
                    <div class="feedback-text">
                      <h4>
                        {{
                          quizResult.isCorrect
                            ? "Goed gedaan!"
                            : "Niet helemaal"
                        }}
                      </h4>
                      <p>{{ quizResult.explanation }}</p>
                    </div>
                  </div>
                  <button
                    v-if="quizResult.isCorrect"
                    class="quiz-action-btn completed"
                    disabled
                  >
                    ✨ Badge verdiend
                  </button>
                  <button
                    v-else
                    class="quiz-action-btn retry"
                    @click="retryQuiz"
                  >
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
            <p>
              Geen overbodige info — alleen wat jij écht nodig hebt als
              MBO‑student.
            </p>
          </div>
          <div class="info-card">
            <div class="info-icon">📋</div>
            <h3>Gebaseerd op DUO & overheid</h3>
            <p>
              Alle informatie up‑to‑date en betrouwbaar, getoetst door experts.
            </p>
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
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import ChatWidget from "./components/ChatWidget.vue";
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
    longDescription:
      "Studiefinanciering van DUO is financiële ondersteuning voor studenten. Je kunt aanvragen zodra je 18 bent en een erkende opleiding volgt. Het bestaat uit een prestatiebeurs (gift) en eventueel een aanvullende beurs. Vul op tijd je aanvraag in via Mijn DUO.",
    completed: true,
    quiz: {
      question: "Wanneer kun je studiefinanciering aanvragen?",
      correctAnswer: 1,
      options: ["Vanaf 16 jaar", "Vanaf 18 jaar", "Vanaf 21 jaar"],
      explanation:
        "Correct! Je kunt studiefinanciering aanvragen zodra je 18 jaar bent en een erkende opleiding volgt.",
    },
  },
  {
    title: "OV-studentenkaart",
    titleShort: "OV",
    description: "Reis voordelig met trein, bus en metro.",
    longDescription:
      "De OV-studentenkaart geeft je gratis of met korting reizen in het weekend of doordeweeks. Je kiest een product via DUO. Let op: je moet wel voldoen aan de voorwaarden (onder andere recht op studiefinanciering).",
    completed: false,
    quiz: {
      question: "Welke keuze kun je maken voor de OV-studentenkaart?",
      correctAnswer: 0,
      options: [
        "Weekend vrij of doordeweeks korting",
        "Altijd 40% korting",
        "Alleen in de zomer",
      ],
      explanation:
        "Je kiest bij DUO of je in het weekend gratis reist (weekend vrij) of doordeweeks 40% korting krijgt.",
    },
  },
  {
    title: "Zorgverzekering & toeslagen",
    titleShort: "Zorg",
    description: "Verplichte zorgverzekering + zorgtoeslag.",
    longDescription:
      "In Nederland ben je verplicht een basiszorgverzekering af te sluiten. Als je 18 wordt, moet je zelf een polis regelen. Kom je in aanmerking voor zorgtoeslag? Check je inkomen en vraag het aan bij de Belastingdienst.",
    completed: false,
    quiz: {
      question: "Is zorgtoeslag automatisch?",
      correctAnswer: 1,
      options: [
        "Ja, je krijgt het vanzelf",
        "Nee, je moet het zelf aanvragen",
        "Alleen als je werkt",
      ],
      explanation:
        "Zorgtoeslag moet je actief aanvragen bij de Belastingdienst. Doe dit op tijd!",
    },
  },
  {
    title: "Woonkosten & huurtoeslag",
    titleShort: "Wonen",
    description: "Energiekosten, huur, en huurtoeslag.",
    longDescription:
      "Woonkosten zijn vaak de grootste uitgave. Als je op kamers gaat of zelfstandig woont, kun je mogelijk huurtoeslag krijgen. De voorwaarden: je huurt een zelfstandige woning, bent 18+, en voldoet aan de inkomensgrens.",
    completed: false,
    quiz: {
      question: "Kan een MBO-student huurtoeslag krijgen?",
      correctAnswer: 0,
      options: ["Ja, onder voorwaarden", "Nee, nooit", "Alleen als je werkt"],
      explanation:
        "Ja, als je 18+ bent, een zelfstandige woning huurt en je inkomen niet te hoog is, kun je huurtoeslag krijgen.",
    },
  },
  {
    title: "Belangrijke documenten",
    titleShort: "Papieren",
    description: "ID, DigiD, bankrekening en meer.",
    longDescription:
      "Zorg dat je een geldig ID‑bewijs hebt, een eigen bankrekening, je DigiD activeert, en je zaken zoals je BSN goed hebt vastgelegd. Bewaar kopieën digitaal en veilig.",
    completed: false,
    quiz: {
      question: "Welke documenten heb je minimaal nodig als je 18 wordt?",
      correctAnswer: 2,
      options: [
        "Alleen ID-kaart",
        "Alleen DigiD",
        "ID, DigiD, bankrekening en eventueel huurcontract",
      ],
      explanation:
        "Je hebt een geldig ID, een actieve DigiD, een eigen bankrekening en bij zelfstandig wonen ook een huurcontract nodig.",
    },
  },
]);

const overallProgress = computed(() => {
  const completedCount = features.value.filter((f) => f.completed).length;
  return Math.round((completedCount / features.value.length) * 100);
});

function scrollToFeatures() {
  document.getElementById("features")?.scrollIntoView({ behavior: "smooth" });
}

function selectFeature(index) {
  selectedFeature.value = index;
  resetQuiz();
}

function submitQuizAnswer(answerIndex) {
  if (!features.value[selectedFeature.value].quiz) return;
  currentQuizAnswer.value = answerIndex;
  const quiz = features.value[selectedFeature.value].quiz;
  const isCorrect = answerIndex === quiz.correctAnswer;
  quizAttempted.value = true;
  quizResult.value = {
    isCorrect,
    explanation: isCorrect
      ? "Fijn! Je bent klaar voor de volgende stap."
      : "Helaas net niet. Lees het stuk nog eens door en probeer opnieuw.",
  };
  if (isCorrect) {
    features.value[selectedFeature.value].completed = true;
  }
}

function retryQuiz() {
  quizAttempted.value = false;
  quizResult.value = null;
  currentQuizAnswer.value = null;
}

function resetQuiz() {
  currentQuizAnswer.value = null;
  quizAttempted.value = false;
  quizResult.value = null;
}
</script>
