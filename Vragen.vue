<template>
  <div class="faq-page" @keydown="onKeydown" tabindex="0" ref="root">
    <header>
      <h1>Dit zijn de meest gestelde vragen</h1>
      <p>
        Gebruik pijltjestoetsen of WASD om te navigeren en spatie om te openen.
      </p>
    </header>

    <transition name="modal-fade">
      <div v-if="selectedItem" class="modal-overlay" @click.self="closeModal">
        <article class="modal-box">
          <button class="close-btn" @click="closeModal" aria-label="Sluiten">
            ×
          </button>
          <h2>{{ selectedItem.title }}</h2>
          <p>{{ selectedItem.text }}</p>
          <img
            :src="selectedItem.dialogImg"
            :alt="selectedItem.title + ' afbeelding'"
          />
          <div class="modal-cta">
            <button @click="closeModal" type="button">Sluiten</button>
          </div>
        </article>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

const selectedItem = ref(null);
const hoverIndex = ref(null);
const activeIndex = ref(0);

const buttonRefs = ref([]);
const setButtonRef = (el) => {
  if (el) buttonRefs.value.push(el);
};

const openItem = (item, i) => {
  selectedItem.value = item;
  activeIndex.value = i;
};

const closeModal = () => {
  selectedItem.value = null;
};

const focusActiveButton = () => {
  const element = buttonRefs.value[activeIndex.value];
  if (element && typeof element.focus === "function") {
    element.focus();
  }
};

const onKeydown = (event) => {
  const key = event.key.toLowerCase();
  let delta = 0;

  if (key === "arrowright" || key === "d") delta = 1;
  if (key === "arrowleft" || key === "a") delta = -1;
  if (key === "arrowdown" || key === "s") delta = 1;
  if (key === "arrowup" || key === "w") delta = -1;

  if (delta !== 0) {
    event.preventDefault();
    activeIndex.value =
      (activeIndex.value + delta + items.length) % items.length;
    hoverIndex.value = activeIndex.value;
    focusActiveButton();
  }

  if (key === " " || key === "spacebar") {
    event.preventDefault();
    openItem(items[activeIndex.value], activeIndex.value);
  }

  if (key === "escape" && selectedItem.value) {
    closeModal();
  }
};

onMounted(() => {
  focusActiveButton();
});

onBeforeUnmount(() => {
  buttonRefs.value = [];
});
</script>

<style scoped>
.faq-page {
  position: relative;
  min-height: 100vh;
  padding: 2.5rem 1rem 4rem;
  color: #ddd;
  background: radial-gradient(
    circle at center,
    #0f1322 0%,
    #05070f 60%,
    #030408 100%
  );
  overflow-x: hidden;
  outline: none;
}

header {
  text-align: center;
  margin-bottom: 1.5rem;
  text-shadow: 0 0 8px rgba(0, 0, 0, 0.8);
}

h1 {
  color: #dbe6ff;
  font-size: clamp(1.5rem, 4vw, 2.8rem);
  margin-bottom: 0.45rem;
}

p {
  color: #9cb4ff;
  opacity: 0.9;
}

.buttons-area {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
}

.buttons-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
}

button {
  border: 1px solid rgba(120, 180, 255, 0.4);
  background: rgba(12, 18, 35, 0.75);
  color: #eef6ff;
  border-radius: 14px;
  padding: 1rem;
  text-align: left;
  position: relative;
  cursor: pointer;
  transition:
    transform 0.14s ease,
    box-shadow 0.16s ease,
    background-color 0.2s ease;
  box-shadow: 0 1px 12px rgba(0, 0, 0, 0.3);
  min-height: 98px;
}

button:hover,
button.active,
button:focus-visible {
  transform: translateY(-2px);
  background: rgba(36, 54, 93, 0.85);
  border-color: rgba(140, 210, 255, 0.85);
  box-shadow: 0 0 18px rgba(84, 180, 255, 0.45);
  outline: none;
}

button span {
  font-weight: 600;
  font-size: 1.05rem;
}

.hover-preview {
  position: absolute;
  right: -18px;
  top: 50%;
  width: 100px;
  height: 100px;
  object-fit: cover;
  transform: translateY(-50%);
  border: 2px solid rgba(170, 220, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 0 13px rgba(0, 140, 255, 0.25);
  z-index: 5;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(6, 9, 18, 0.84);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  z-index: 40;
}

.modal-box {
  max-width: 680px;
  width: clamp(320px, 80%, 680px);
  background: linear-gradient(
    to bottom right,
    rgba(11, 18, 32, 0.96),
    rgba(18, 28, 48, 0.96)
  );
  border: 1px solid rgba(147, 199, 255, 0.35);
  border-radius: 18px;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.55);
  padding: 1.3rem;
  color: #f0f6ff;
  position: relative;
}

.modal-box h2 {
  margin-top: 0;
  margin-bottom: 0.8rem;
}

.modal-box p {
  line-height: 1.55;
  margin-bottom: 1rem;
}

.modal-box img {
  width: 100%;
  border-radius: 12px;
  border: 1px solid rgba(35, 55, 95, 0.7);
  margin-bottom: 1rem;
}

.close-btn {
  position: absolute;
  top: 0.72rem;
  right: 0.72rem;
  background: rgba(25, 42, 70, 0.95);
  color: #c9deff;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  border: 1px solid rgba(170, 210, 255, 0.3);
  font-size: 1.2rem;
  cursor: pointer;
}

.modal-cta {
  text-align: right;
}

.modal-cta button {
  background: rgba(58, 115, 198, 0.9);
  border: none;
  color: #fff;
  padding: 0.55rem 1rem;
  border-radius: 8px;
  cursor: pointer;
}

button:focus-visible,
.close-btn:focus-visible,
.modal-cta button:focus-visible {
  outline: 2px solid rgba(190, 230, 255, 0.8);
  outline-offset: 2px;
}

.fade-enter-active,
.fade-leave-active,
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: all 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}
</style>
