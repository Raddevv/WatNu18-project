<template>
  <div
    class="wrapper"
    :style="{ backgroundImage: hoveredImage ? `url(${hoveredImage})` : '' }"
  >
    <div class="header">Opleiding wijzigen of stoppen</div>

    <div class="menu-container">
      <div
        v-for="(item, index) in menuItems"
        :key="index"
        class="menu-item"
        :class="{ active: selectedIndex === index }"
        @mouseover="
          setActive(index);
          setHovered(item.bgImage);
        "
        @mouseleave="
          resetFooterText();
          setHovered(null);
        "
        @click="openModal(item)"
      >
        <div class="menu-item-bar">
          <div class="menu-item-text">{{ item.text }}</div>
          <img :src="item.image" />
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="back-button" @click="goHome">← Back (1)</div>
      <div>{{ footerText }}</div>
    </div>
  </div>

  <!-- MODAL -->
  <transition name="modal">
    <div v-if="selectedItem" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <img :src="selectedItem.image" />
        <h2>{{ selectedItem.text }}</h2>
        <p>{{ selectedItem.footerText }}</p>

        <button @click="closeModal">Sluiten (ESC)</button>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "somethingidk",

  data() {
    return {
      footerText: "footer text",
      selectedItem: null,
      selectedIndex: 0,
      hoveredImage: null,

      menuItems: [
        {
          text: "Hulp nodig bij nieuwe opleiding?",
          image: "https://picsum.photos/500/200?random=1",
          bgImage: "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
          footerText: "Wij helpen je bij het kiezen van een nieuwe opleiding.",
        },
        {
          text: "Opleiding stoppen",
          image: "https://picsum.photos/500/200?random=2",
          bgImage: "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
          footerText: "Informatie over stoppen met je opleiding.",
        },
        {
          text: "Opleiding wijzigen",
          image: "https://picsum.photos/500/200?random=3",
          bgImage: "https://media.giphy.com/media/xT0GqeSlGSRQut9PHi/giphy.gif",
          footerText: "Je opleiding veranderen.",
        },
        {
          text: "Studie advies",
          image: "https://picsum.photos/500/200?random=4",
          bgImage:
            "https://cdn.pixabay.com/animation/2024/03/23/11/38/11-38-47-787_512.gif",
          footerText: "Neem contact op met een studie adviseur.",
        },
      ],
    };
  },

  mounted() {
    window.addEventListener("keydown", this.handleKey);
    this.updateFooterText(this.menuItems[0].footerText);
  },

  beforeUnmount() {
    window.removeEventListener("keydown", this.handleKey);
  },

  methods: {
    goHome() {
      this.$router.push("/");
    },

    setActive(index) {
      this.selectedIndex = index;
      this.updateFooterText(this.menuItems[index].footerText);
    },

    setHovered(image) {
      this.hoveredImage = image;
    },

    updateFooterText(text) {
      this.footerText = text;
    },

    resetFooterText() {
      this.footerText = this.menuItems[this.selectedIndex].footerText;
    },

    openModal(item) {
      this.selectedItem = item;
    },

    closeModal() {
      this.selectedItem = null;
    },

    handleKey(e) {
      // modal open
      if (this.selectedItem) {
        if (e.key === "Escape") {
          this.closeModal();
        }
        return;
      }

      // BACK
      if (e.key === "1") {
        this.goHome();
      }

      // OPEN MENU ITEMS
      if (e.key === "2") this.openModal(this.menuItems[0]);
      if (e.key === "3") this.openModal(this.menuItems[1]);
      if (e.key === "4") this.openModal(this.menuItems[2]);
      if (e.key === "5") this.openModal(this.menuItems[3]);

      // NAVIGATIE
      if (["ArrowDown", "s", "S"].includes(e.key)) {
        this.selectedIndex = (this.selectedIndex + 1) % this.menuItems.length;
        this.updateFooterText(this.menuItems[this.selectedIndex].footerText);
      }

      if (["ArrowUp", "w", "W"].includes(e.key)) {
        this.selectedIndex =
          (this.selectedIndex - 1 + this.menuItems.length) %
          this.menuItems.length;

        this.updateFooterText(this.menuItems[this.selectedIndex].footerText);
      }

      if (e.key === "Enter") {
        this.openModal(this.menuItems[this.selectedIndex]);
      }
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: Arial;
  background: #000;
  color: white;
  overflow: hidden;
}

/* animated background */

body::before {
  content: "";
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    #242323 0px,
    #242323 6px,
    #000 6px,
    #000 12px
  );
  animation: scrollBg 8s linear infinite;
  z-index: -2;
}

@keyframes scrollBg {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 0 -300px;
  }
}

.wrapper {
  width: 900px;
  background-color: #000; /* fallback */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  transition: background-image 0.35s ease;
}

#app {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header {
  background: linear-gradient(to bottom, #fff, #e5e5e5);
  padding: 20px 30px;
  font-size: 26px;
  font-weight: bold;
  color: #333;
  border-radius: 12px 12px 0 0;
  border: 3px solid #bdbdbd;
}

.menu-container {
  padding: 35px 0;
}

.menu-item {
  margin: 18px 0;
}

.menu-item-bar {
  height: 90px;
  border-radius: 14px;
  background: linear-gradient(
    145deg,
    rgba(30, 30, 30, 0.7),
    rgba(16, 16, 16, 0.7)
  );
  border: 3px solid #2c2c2c;
  display: flex;
  align-items: center;
  padding-left: 40px;
  font-size: 30px;
  font-weight: bold;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.25s ease;
}

.menu-item-bar img {
  position: absolute;
  right: -120%;
  top: 0;
  height: 100%;
  transition: 0.35s;
  opacity: 0.85;
}

.menu-item:hover img {
  right: 0;
}

.menu-item:hover .menu-item-bar {
  transform: scale(1.06) translateX(10px);
  border: 4px solid #ffd900;
}

.menu-item.active .menu-item-bar {
  transform: scale(1.06) translateX(10px);
  border: 4px solid #ffd900;
  box-shadow:
    0 0 20px rgba(255, 217, 0, 0.7),
    0 20px 40px rgba(0, 0, 0, 0.8);
}

.footer {
  background: linear-gradient(to bottom, #fff, #e9e9e9);
  padding: 15px;
  border: 10px solid #bdbdbd;
  border-radius: 0 0 12px 12px;
  display: flex;
  justify-content: space-between;
  color: #333;
  font-weight: bold;
}

.back-button {
  cursor: pointer;
  transition: 0.2s;
}

.back-button:hover {
  color: #ffd900;
  transform: translateX(-5px);
}

/* modal */

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(6px);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  width: 500px;
  background: #1a1a1a;
  padding: 30px;
  border-radius: 14px;
  text-align: center;
  border: 3px solid #ffd900;
}

.modal img {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 15px;
}

.modal button {
  padding: 10px 25px;
  background: #ffd900;
  border: none;
  font-weight: bold;
  cursor: pointer;
}

.modal-enter-from {
  opacity: 0;
  transform: translateY(120px) scale(0.9);
}

.modal-enter-active {
  transition: 0.35s;
}

.modal-leave-to {
  opacity: 0;
  transform: translateY(120px) scale(0.9);
}

.modal-leave-active {
  transition: 0.25s;
}
</style>
```
