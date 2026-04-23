<template>
  <div class="gif-background" aria-hidden="true"></div>
  <div class="vragen-view">
    <h1>Dit zijn de meest gestelde vragen</h1>

    <div class="questions-grid" role="list">
      <button
        v-for="(faq, index) in faqs"
        :key="faq.id"
        class="faq-button"
        :class="{
          focused: focusedIndex === index,
          active: activeFAQ === index,
        }"
        @click="openFAQ(index)"
        @mouseover="hoverIndex = index"
        @mouseleave="hoverIndex = null"
        :aria-label="`Open vraag: ${faq.question}`"
        :aria-pressed="activeFAQ === index"
        type="button"
      >
        <span>{{ faq.question }}</span>
        <div v-if="hoverIndex === index" class="hover-preview">
          <img :src="faq.hoverImage" :alt="faq.question + ' preview'" />
        </div>
      </button>
    </div>

    <div
      v-if="activeFAQ !== null"
      class="modal-backdrop"
      @click.self="closeFAQ"
      role="dialog"
      aria-modal="true"
    >
      <div class="modal-card">
        <button class="modal-close" @click="closeFAQ" aria-label="Sluit popup">
          ✕
        </button>
        <h2>{{ faqs[activeFAQ].question }}</h2>
        <p>{{ faqs[activeFAQ].answer }}</p>
        <img
          class="modal-image"
          :src="faqs[activeFAQ].detailImage"
          :alt="faqs[activeFAQ].question + ' afbeelding'"
        />
      </div>
    </div>

    <div class="help-text">
      <p>
        Gebruik de pijltjestoetsen of WASD om tussen knoppen te navigeren, en
        spatie/enter om te openen.
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const faqs = ref([
  {
    id: 1,
    question: "Hoe vraag ik studiefinanciering aan?",
    answer:
      "Ga naar DUO, log in met DigiD, en volg de stappen om studiefinanciering te starten. Bewaar alle bewijsstukken en stel een herinnering in.",
    hoverImage: "https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif",
    detailImage: "https://picsum.photos/seed/studiefinanciering/640/360",
  },
  {
    id: 2,
    question: "Wat zijn de voorwaarden voor OV-chipkaart?",
    answer:
      "Je moet 18+ zijn en ingeschreven bij een opleiding. Kies weekendvrij of doordeweeks 40% korting via DUO. Zorg dat je rekeningnummer klopt.",
    hoverImage: "https://media.giphy.com/media/3o6Zt2TFQ4BfNGzaEA/giphy.gif",
    detailImage: "https://picsum.photos/seed/ovchipkaart/640/360",
  },
  {
    id: 3,
    question: "Hoe sluit ik een zorgverzekering af?",
    answer:
      "Vergelijk pakketten, kies basisdekking met voorkeurzorg, en sluit af voor 1 januari. Controleer of je in aanmerking komt voor zorgtoeslag.",
    hoverImage: "https://media.giphy.com/media/26gssIytJvy1b1THO/giphy.gif",
    detailImage: "https://picsum.photos/seed/zorgverzekering/640/360",
  },
  {
    id: 4,
    question: "Wanneer kan ik huurtoeslag krijgen?",
    answer:
      "Als je een zelfstandige woonruimte huurt, 18+ bent en je inkomen lager is dan de grens. Vraag online aan bij de Belastingdienst.",
    hoverImage: "https://media.giphy.com/media/xT0BKGmab4bOazg27y/giphy.gif",
    detailImage: "https://picsum.photos/seed/huurtoeslag/640/360",
  },
  {
    id: 5,
    question: "Wat heb ik nodig voor mijn identiteitsbewijs?",
    answer:
      "Een geldig paspoort of ID-kaart. Maak op tijd een afspraak bij de gemeente en regel een DigiD in de tussentijd.",
    hoverImage: "https://media.giphy.com/media/3oKIP8irnK7b1AjmPM/giphy.gif",
    detailImage: "https://picsum.photos/seed/identiteitsbewijs/640/360",
  },
]);

const activeFAQ = ref(null);
const hoverIndex = ref(null);
const focusedIndex = ref(0);

function openFAQ(index) {
  activeFAQ.value = index;
}

function closeFAQ() {
  activeFAQ.value = null;
}

function focusNext() {
  focusedIndex.value = (focusedIndex.value + 1) % faqs.value.length;
}

function focusPrevious() {
  focusedIndex.value =
    (focusedIndex.value - 1 + faqs.value.length) % faqs.value.length;
}

function onKeydown(event) {
  if (event.key === "ArrowDown" || event.key.toLowerCase() === "s") {
    event.preventDefault();
    focusNext();
    return;
  }

  if (event.key === "ArrowUp" || event.key.toLowerCase() === "w") {
    event.preventDefault();
    focusPrevious();
    return;
  }

  if (event.key === "ArrowRight" || event.key.toLowerCase() === "d") {
    event.preventDefault();
    focusNext();
    return;
  }

  if (event.key === "ArrowLeft" || event.key.toLowerCase() === "a") {
    event.preventDefault();
    focusPrevious();
    return;
  }

  if (event.key === " " || event.key === "Enter") {
    event.preventDefault();
    openFAQ(focusedIndex.value);
    return;
  }

  if (event.key === "Escape") {
    if (activeFAQ.value !== null) {
      closeFAQ();
    }
  }
}

onMounted(() => {
  window.addEventListener("keydown", onKeydown);
});

onUnmounted(() => {
  window.removeEventListener("keydown", onKeydown);
});
</script>

<style scoped>
.vragen-view {
  position: relative;
  min-height: 100vh;
  color: #f5f5f5;
  background: radial-gradient(
    circle at center,
    #111 0%,
    #07080f 70%,
    #020205 100%
  );
  padding: 4rem 1.5rem 2rem;
  overflow: visible;
  min-height: calc(100vh - 110px);
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 1;
}

h1 {
  font-size: 2.2rem;
  text-align: center;
  margin-bottom: 1.5rem;
  text-shadow: 0 0 20px rgba(111, 204, 255, 0.6);
  z-index: 1;
}

.questions-grid {
  width: min(700px, 100%);
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  z-index: 10;
  overflow-x: hidden;
}

.faq-button {
  position: relative;
  padding: 1rem 1.25rem;
  min-height: 88px;
  border-radius: 1rem;
  border: 1px solid rgba(132, 255, 255, 0.35);
  background: rgba(15, 20, 40, 0.18);
  color: #e6f4ff;
  text-align: left;
  font-size: 1rem;
  backdrop-filter: blur(8px);
  cursor: pointer;
  transition:
    transform 0.18s ease,
    box-shadow 0.18s ease,
    background 0.18s ease;
  overflow: hidden;
}

.faq-button.focused,
.faq-button:hover {
  box-shadow: 0 0 24px rgba(47, 225, 255, 0.46);
  transform: translateY(-2px);
  border-color: rgba(66, 182, 255, 0.9);
}

.faq-button.active {
  border-color: rgba(255, 200, 90, 0.9);
  background: rgba(30, 40, 65, 0.75);
}

.hover-preview {
  position: absolute;
  right: -220px;
  top: 50%;
  transform: translateY(-50%);
  width: 180px;
  height: 120px;
  overflow: hidden;
  border-radius: 0.75rem;
  border: 1px solid rgba(102, 213, 255, 0.35);
  background: rgba(3, 13, 63, 0.9);
  box-shadow: 0 0 16px rgba(0, 255, 255, 0.25);
}

.hover-preview img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  filter: brightness(1.1);
}

.modal-backdrop {
  z-index: 50;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.65);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.modal-card {
  position: relative;
  background: linear-gradient(
    160deg,
    rgba(14, 20, 35, 0.98),
    rgba(8, 12, 28, 0.95)
  );
  border: 1px solid rgba(15, 221, 255, 0.24);
  border-radius: 1rem;
  max-width: 620px;
  width: 100%;
  padding: 1.5rem;
  box-shadow: 0 0 40px rgba(52, 140, 255, 0.35);
}

.modal-close {
  position: absolute;
  top: 0.8rem;
  right: 0.8rem;
  border: none;
  background: rgba(255, 255, 255, 0.12);
  color: #fff;
  width: 34px;
  height: 34px;
  border-radius: 0.65rem;
  cursor: pointer;
  font-size: 1.1rem;
}

.modal-card h2 {
  margin: 0 0 0.8rem;
  font-size: 1.55rem;
}

.modal-card p {
  line-height: 1.5;
  margin-bottom: 1rem;
}

.modal-image {
  width: 100%;
  border-radius: 0.8rem;
  border: 1px solid rgba(102, 211, 255, 0.32);
  box-shadow: 0 0 20px rgba(65, 150, 255, 0.25);
}

.help-text {
  margin-top: 1.2rem;
  color: #8fb9d9;
  font-size: 0.95rem;
  text-align: center;
  z-index: 1;
}
</style>
