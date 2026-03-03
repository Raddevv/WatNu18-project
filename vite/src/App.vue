<template>
  <div id="app">
    <Header />
    <div class="vignette"></div>
    
    <main class="main-content">
      <section class="hero">
        <div class="hero-content">
          <h1 class="hero-title">
            <span class="watnu-text">Wat nu</span><span class="number-18"> 18?</span>
          </h1>
          <p>
            Welkom bij Watnu18! We helpen MBO studenten alles begrijpen wat je moet weten
            als je 18 wordt. Van studiefinanciering tot OV-studentenkaarten, we maken 
            het ingewikkelde simpel.
          </p>
          <button class="cta-btn">Meer Informatie</button>
        </div>
      </section>

      <section class="features">
        <div class="features-wrapper animate-on-scroll">
          <div class="features-menu-vertical">
            <button 
              class="feature-tab-vertical" 
              :class="{ active: selectedFeature === 0 }"
              @click="selectedFeature = 0"
            >
              <span class="feature-icon">€</span>
              <span class="feature-name">Studiefinanciering</span>
            </button>

            <button 
              class="feature-tab-vertical" 
              :class="{ active: selectedFeature === 1 }"
              @click="selectedFeature = 1"
            >
              <span class="feature-icon">🚌</span>
              <span class="feature-name">OV-Kaart</span>
            </button>

            <button 
              class="feature-tab-vertical" 
              :class="{ active: selectedFeature === 2 }"
              @click="selectedFeature = 2"
            >
              <span class="feature-icon">🏠</span>
              <span class="feature-name">Woonkosten</span>
            </button>

            <button 
              class="feature-tab-vertical" 
              :class="{ active: selectedFeature === 3 }"
              @click="selectedFeature = 3"
            >
              <span class="feature-icon">📋</span>
              <span class="feature-name">Documenten</span>
            </button>

            <button 
              class="feature-tab-vertical" 
              :class="{ active: selectedFeature === 4 }"
              @click="selectedFeature = 4"
            >
              <span class="feature-icon">¡</span>
              <span class="feature-name">FAQ</span>
            </button>

            <button 
              class="feature-tab-vertical" 
              :class="{ active: selectedFeature === 5 }"
              @click="selectedFeature = 5"
            >
              <span class="feature-icon">💬</span>
              <span class="feature-name">Contact</span>
            </button>
          </div>

          <!-- Right content area -->
          <div class="features-content animate-on-scroll">
            <transition name="fadeContentSwitch" mode="out-in">
              <div v-if="selectedFeature === 0" key="0" class="feature-detail">
                <h2>💰 Studiefinanciering</h2>
                <p>
                  Begrijp hoe studiefinanciering werkt, wat je kunt aanvragen en hoe je 
                  het aanvraagt als je 18 bent. Dit is een belangrijke ondersteuning voor 
                  veel studenten gedurende hun studiejaren.
                </p>
                <p>
                  Als je 18 bent, kun je aanvrager worden voor studiefinanciering. Dit is 
                  het geld dat je van DUO krijgt om je studie mee te betalen. Er zijn 
                  verschillende vormen van studiefinanciering, zoals studiebeurs en 
                  studieleninig.
                </p>
              </div>

              <div v-else-if="selectedFeature === 1" key="1" class="feature-detail">
                <h2>🚌 OV-Studentenkaart</h2>
                <p>
                  Alles over de OV-studentenkaart: hoe je deze krijgt, wat het kost en 
                  hoe je ermee reist. Met de OV-studentenkaart krijg je korting op je treinkaartjes.
                </p>
                <p>
                  De OV-studentenkaart is een kaart waarmee je tegen gereduceerde tarief 
                  met het openbaar vervoer kunt reizen. Als je studeert aan een MBO-instelling, 
                  ben je meestal recht op de studentenkaart.
                </p>
              </div>

              <div v-else-if="selectedFeature === 2" key="2" class="feature-detail">
                <h2>🏠 Woonkosten</h2>
                <p>
                  Tips voor het vinden van betaalbare huisvesting en hulp bij 
                  woonkostentoeslag. We helpen je om je eerste kamer te vinden.
                </p>
                <p>
                  Voor veel studenten is het vinden van geschikte huisvesting een groot 
                  uitdaging. We geven je tips over waar je kunt zoeken en wat je moet 
                  letten op huurcontracten. Ook helpen we je met aanvragen voor 
                  woonkostentoeslag.
                </p>
              </div>

              <div v-else-if="selectedFeature === 3" key="3" class="feature-detail">
                <h2>📋 Documenten & Formulieren</h2>
                <p>
                  Alle formulieren en documenten die je nodig hebt, op een overzichtelijke 
                  plek verzameld. Download alles wat je nodig hebt in één plek.
                </p>
                <p>
                  Op deze pagina vind je alle belangrijke formulieren en documenten die je 
                  nodig hebt als je 18 bent. Van aanvraagformulieren tot contracten, alles 
                  is hier te vinden en klaar om te downloaden.
                </p>
              </div>

              <div v-else-if="selectedFeature === 4" key="4" class="feature-detail">
                <h2>❓ Veelgestelde Vragen</h2>
                <p>
                  De vragen die andere studenten stellen en hun antwoorden. Misschien 
                  staat jouw vraag ook wel hier. Bekijk onze uitgebreide FAQ.
                </p>
                <p>
                  We hebben een lijst samengesteld met vragen die veel studenten hebben. 
                  Navigeer door de vragen en antwoorden om antwoord op jouw vragen te vinden. 
                  Als je vraag niet beantwoord wordt, neem dan contact met ons op.
                </p>
              </div>

              <div v-else key="5" class="feature-detail">
                <h2>💬 Contact & Ondersteuning</h2>
                <p>
                  Vragen? Neem contact met ons op. Wij helpen je graag verder met 
                  wat je wilt weten. Stuur ons een bericht en we nemen snel contact op.
                </p>
                <p>
                  Heb je vragen of wil je meer informatie? Ons team staat klaar om je 
                  te helpen. Je kunt ons bereiken via e-mail, telefoon of door het 
                  contactformulier in te vullen. We doen ons best om binnen 24 uur 
                  op je bericht te reageren.
                </p>
              </div>
            </transition>
          </div>
        </div>
      </section>

      <section class="info-section animate-on-scroll">
        <h2>Waarom Watnu?</h2>
        <p>
          Wanneer je 18 wordt, zijn er veel dingen die veranderen. Je kunt 
          studiefinanciering aanvragen, je krijgt een OV-studentenkaart, en 
          je moet zelf meer regelen. Watnu helpt je door dit allemaal!
        </p>
        <p>
          Onze website is gemaakt voor MBO studenten, door mensen die snappen 
          hoe verwarrend het allemaal kan zijn. We leggen alles uit in simpel 
          Nederlands, zonder ingewikkelde termen.
        </p>
      </section>
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import { onMounted, ref } from 'vue'

const selectedFeature = ref(0) // Studiefinanciering is standaard open

onMounted(() => {
  // Generate random stars
  const hero = document.querySelector('.hero');
  const starsContainer = document.createElement('div');
  starsContainer.className = 'stars-container';
  
  // Generate 80 random stars (reduced for performance)
  for (let i = 0; i < 80; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    
    // Random position - ONLY in top 40% for stars
    const x = Math.random() * 100;
    const y = Math.random() * 40;
    
    // Smaller stars (0.5px to 1.5px)
    const size = Math.random() * 1 + 0.5;
    
    // Random opacity
    const opacity = Math.random() * 0.6 + 0.3;
    
    // Random animation delay for twinkle
    const twinkleDelay = Math.random() * 5;
    
    star.style.left = x + '%';
    star.style.top = y + '%';
    star.style.width = size + 'px';
    star.style.height = size + 'px';
    star.style.opacity = opacity;
    star.style.animationDelay = twinkleDelay + 's';
    
    starsContainer.appendChild(star);
  }
  
  hero.appendChild(starsContainer);
  
  // Scroll animation observer
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'fadeInUp 0.8s ease forwards'
        observer.unobserve(entry.target)
      }
    })
  }, observerOptions)

  // Observe all animated sections
  document.querySelectorAll('.animate-on-scroll').forEach(el => {
    el.style.opacity = '0'
    observer.observe(el)
  })
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #F6F4F3;
  color: #333;
  line-height: 1.6;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  position: relative;
}

/* Vignette Effect */
.vignette {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 50;
  box-shadow: inset 0 0 80px rgba(5, 20, 15, 0.3), inset 0 0 40px rgba(0, 200, 150, 0.1);
  border-radius: 0;
}

.main-content {
  flex: 1;
  padding: 0;
  position: relative;
  z-index: 1;
  background: white;
}

/* Hero Section */
.hero {
  background: 
    radial-gradient(ellipse at 20% 50%, rgba(0, 150, 120, 0.25) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(0, 200, 160, 0.2) 0%, transparent 50%),
    radial-gradient(ellipse at 40% 80%, rgba(0, 230, 180, 0.12) 0%, transparent 50%),
    linear-gradient(135deg, #051410 0%, #0B2415 25%, #0D3B2F 50%, #061820 75%, #030A06 100%);
  color: #F6F4F3;
  padding: 6rem 2rem 2rem;
  text-align: center;
  margin-bottom: 0;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 50%;
  background: 
    radial-gradient(ellipse 600px 400px at 15% 30%, rgba(0, 150, 120, 0.2) 0%, transparent 50%),
    radial-gradient(ellipse 500px 350px at 85% 20%, rgba(0, 200, 160, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse 450px 300px at 50% 50%, rgba(0, 230, 180, 0.08) 0%, transparent 50%);
  pointer-events: none;
  z-index: 1;
}

.hero::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100px;
  background: linear-gradient(to bottom, rgba(246, 244, 243, 0), white);
  pointer-events: none;
  z-index: 2;
}

@keyframes twinkle {
  0%, 100% {
    opacity: 0.8;
  }
  50% {
    opacity: 0.3;
  }
}

@keyframes floatStars {
  0% {
    transform: translateY(0px) translateX(0px);
  }
  25% {
    transform: translateY(-20px) translateX(10px);
  }
  50% {
    transform: translateY(-40px) translateX(-10px);
  }
  75% {
    transform: translateY(-20px) translateX(10px);
  }
  100% {
    transform: translateY(0px) translateX(0px);
  }
}

/* Stars Container */
.stars-container {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 1;
}

.star {
  position: absolute;
  background: white;
  border-radius: 50%;
  box-shadow: 0 0 2px rgba(255, 255, 255, 0.6);
  animation: twinkle 3s ease-in-out infinite;
}

@keyframes twinkle {
  0%, 100% {
    opacity: 0.3;
  }
  50% {
    opacity: 1;
  }
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  animation: fadeInUp 1s ease;
  position: relative;
  z-index: 2;
}

.hero-title {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  font-weight: 800;
  letter-spacing: -1px;
  display: inline-block;
  line-height: 1.1;
}

.watnu-text {
  -webkit-text-stroke: 2px #00D9A3;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 8px rgba(0, 217, 163, 0.4))
          drop-shadow(0 0 16px rgba(0, 217, 163, 0.2));
  animation: glow 3s ease-in-out infinite;
}

.number-18 {
  background: linear-gradient(135deg, #00D9A3 0%, #00F0B8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0 0 8px rgba(0, 240, 184, 0.4))
          drop-shadow(0 0 16px rgba(0, 217, 163, 0.2));
  animation: glow 3s ease-in-out infinite;
}

@keyframes glow {
  0%, 100% {
    filter: drop-shadow(0 0 8px rgba(0, 240, 184, 0.4))
            drop-shadow(0 0 16px rgba(0, 217, 163, 0.2));
  }
  50% {
    filter: drop-shadow(0 0 12px rgba(0, 240, 184, 0.5))
            drop-shadow(0 0 24px rgba(0, 217, 163, 0.3));
  }
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  line-height: 1.8;
  opacity: 0.98;
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.hero p {
  font-size: 1.1rem;
  margin-bottom: 2rem;
  line-height: 1.8;
  opacity: 0.95;
}

.cta-btn {
  background: linear-gradient(135deg, #00D9A3 0%, #00F0B8 100%);
  color: #051410;
  border: 2px solid #00D9A3;
  padding: 0.75rem 2rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 217, 163, 0.4);
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 25px rgba(0, 240, 184, 0.5);
  border-color: #051410;
  background: linear-gradient(135deg, #00F0B8 0%, #00D9A3 100%);
}

/* Features Section */
.features {
  padding: 0 2rem;
  margin: -40px 0 3rem 0;
  position: relative;
  z-index: 5;
  background: white;
}

.features-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  display: grid;
  grid-template-columns: minmax(250px, 320px) 1fr;
  border: 1px solid #f0f0f0;
  animation: fadeInUp 0.8s ease;
}

/* Left Vertical Menu */
.features-menu-vertical {
  background: linear-gradient(180deg, #fff 0%, #f0faf8 100%);
  border-left: 5px solid #00D9A3;
  border-right: 1px solid rgba(0, 217, 163, 0.15);
  padding: 1rem 0;
}

.feature-tab-vertical {
  width: 100%;
  border: none;
  background: transparent;
  color: #0D3B2F;
  text-align: left;
  padding: 0.95rem 1.2rem;
  font-size: 0.95rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.7rem;
  cursor: pointer;
  border-left: 4px solid transparent;
  transition: background-color 0.25s ease, color 0.25s ease, border-color 0.25s ease, transform 0.25s ease;
  animation: slideInFromLeft 0.45s ease both;
}

.feature-tab-vertical:nth-child(1) { animation-delay: 0.05s; }
.feature-tab-vertical:nth-child(2) { animation-delay: 0.1s; }
.feature-tab-vertical:nth-child(3) { animation-delay: 0.15s; }
.feature-tab-vertical:nth-child(4) { animation-delay: 0.2s; }
.feature-tab-vertical:nth-child(5) { animation-delay: 0.25s; }
.feature-tab-vertical:nth-child(6) { animation-delay: 0.3s; }

.feature-tab-vertical:hover {
  background-color: rgba(0, 217, 163, 0.08);
  border-left-color: #00D9A3;
  transform: translateX(4px);
}

.feature-tab-vertical.active {
  background: linear-gradient(90deg, rgba(0, 217, 163, 0.16), rgba(0, 217, 163, 0.05));
  color: #00D9A3;
  border-left-color: #00D9A3;
}

.feature-tab-vertical .feature-icon {
  font-size: 1.1rem;
  width: 1.4rem;
}

/* Content Area */
.features-content {
  padding: 3rem;
  background: white;
  min-height: 400px;
  margin: 0;
  width: 100%;
  animation: fadeInUp 0.75s ease;
}

.feature-detail {
  animation: fadeContentSwitch 0.3s ease;
}

.feature-detail h2 {
  color: #00D9A3;
  font-size: 2rem;
  margin: 0 0 1.5rem 0;
  font-weight: 700;
}

.feature-detail p {
  color: #555;
  line-height: 1.8;
  margin-bottom: 1.5rem;
  font-size: 1.05rem;
}

.feature-detail p:last-child {
  margin-bottom: 0;
}

/* Info Section */
.info-section {
  max-width: 900px;
  margin: 3rem auto;
  padding: 3.5rem 2.5rem;
  text-align: center;
  background: linear-gradient(135deg, white 0%, rgba(240, 250, 248, 0.5) 100%);
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  border-left: 5px solid #00D9A3;
  animation: slideInFromBottom 0.8s ease;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.info-section::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(0, 217, 163, 0.12) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}

.info-section h2 {
  color: #00D9A3;
  font-size: 2.2rem;
  margin-bottom: 1.5rem;
  font-weight: 700;
  position: relative;
  z-index: 2;
}

.info-section p {
  color: #444;
  margin-bottom: 1.5rem;
  line-height: 1.8;
  font-size: 1.05rem;
  position: relative;
  z-index: 2;
}

.info-section p:last-child {
  margin-bottom: 0;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeContentSwitch {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideDown {
  from {
    opacity: 0;
    max-height: 0;
  }
  to {
    opacity: 1;
    max-height: 500px;
  }
}

@keyframes slideInFromBottom {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInFromLeft {
  from {
    opacity: 0;
    transform: translateX(-14px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.fadeContentSwitch-enter-active,
.fadeContentSwitch-leave-active {
  transition: opacity 0.4s ease;
}

.fadeContentSwitch-enter-from,
.fadeContentSwitch-leave-to {
  opacity: 0;
}

/* Responsive */
@media (max-width: 1024px) {
  .features-wrapper {
    grid-template-columns: minmax(210px, 260px) 1fr;
  }

  .feature-tab-vertical {
    font-size: 0.9rem;
    padding: 0.9rem 1rem;
  }

  .feature-tab-vertical .feature-name {
    font-size: 0.9rem;
  }

  .features-content {
    padding: 2rem;
  }

  .feature-detail h2 {
    font-size: 1.7rem;
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 4rem 1rem 2rem;
    min-height: auto;
  }

  .hero h1 {
    font-size: 2.2rem;
  }

  .hero p {
    font-size: 1rem;
  }

  .hero::after {
    height: 120px;
  }

  .features-wrapper {
    grid-template-columns: 1fr;
  }

  .features-menu-vertical {
    border-left: 4px solid #00D9A3;
    border-right: none;
    border-bottom: 1px solid rgba(0, 217, 163, 0.2);
    padding: 0.4rem 0;
  }

  .feature-tab-vertical {
    padding: 0.85rem 1rem;
  }

  .features-wrapper {
    border-radius: 0;
  }

  .features-content {
    padding: 1.5rem;
    min-height: auto;
  }

  .feature-detail h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }

  .feature-detail p {
    font-size: 1rem;
    margin-bottom: 1rem;
  }

  .info-section {
    margin: 2rem 1rem;
    padding: 2.5rem 1.5rem;
  }

  .info-section h2 {
    font-size: 1.8rem;
  }
}

@media (max-width: 480px) {
  .hero {
    padding: 2rem 1rem 1.5rem;
    min-height: auto;
  }

  .hero h1 {
    font-size: 1.8rem;
  }

  .hero p {
    font-size: 0.95rem;
  }

  .cta-btn {
    padding: 0.6rem 1.5rem;
    font-size: 0.9rem;
  }

  .hero::after {
    height: 100px;
  }

  .feature-tab-vertical {
    padding: 0.75rem 0.85rem;
    font-size: 0.85rem;
  }

  .features-content {
    padding: 1rem;
    min-height: auto;
  }

  .feature-detail h2 {
    font-size: 1.2rem;
    margin-bottom: 0.75rem;
  }

  .feature-detail p {
    font-size: 0.9rem;
    margin-bottom: 0.75rem;
  }

  .info-section {
    padding: 1.5rem 1rem;
    margin: 1.5rem 0.5rem;
  }

  .info-section h2 {
    font-size: 1.3rem;
  }
}
</style>
