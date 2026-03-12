<template>
  <section class="hero-section">
    <div class="hero-content">
      <div class="hero-text">
        <h2>Ontdek je studiefinanciering!</h2>
        <p>DUO-erkend advies voor basisbeurs,贷lening, zorgtoeslag en meer. Doe de quiz en verdien punten voor exclusieve badges!</p>
        <div class="hero-ctas">
          <button @click="startQuiz" class="cta-primary coral-btn glow-effect">
            🚀 Start Quiz (100pts!)
          </button>
          <button @click="checkEligibility" class="cta-secondary teal-btn">
            Bereken Eligibility
          </button>
        </div>
        <div class="points-teaser">
          <span>💎 Ontgrendel badges en stijg in de leaderboard!</span>
        </div>
      </div>
      <div class="hero-image">
        <div class="student-illus">
          <span>📚 Student succes</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroComponent',
  methods: {
    startQuiz() {
      this.earnPoints(100);
      // Simulate quiz start
      alert('Quiz gestart! Beantwoord vragen om je punten te verdienen. +100 punten!');
    },
    checkEligibility() {
      alert('Eligibility calculator: Je komt in aanmerking voor €500/maand basisbeurs! Verdien 50pts door door te gaan.');
      this.earnPoints(50);
    },
    earnPoints(amount) {
      // Local sim; emit to parent if needed
      console.log(`+${amount} punten verdiend! Totaal wordt bijgewerkt in header.`);
    }
  }
};
</script>

<style scoped>
.hero-section {
  background: linear-gradient(135deg, #0A6E6A 0%, #FF5E5E40 100%);
  padding: 4rem 2rem;
  color: #2D3748;
  display: flex;
  align-items: center;
}
.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}
.hero-text h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  background: linear-gradient(45deg, #FFD700, #FF5E5E);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-text p { font-size: 1.2rem; margin-bottom: 2rem; }
.hero-ctas { display: flex; gap: 1rem; flex-wrap: wrap; }
.cta-primary, .cta-secondary {
  padding: 1rem 2rem;
  border: none;
  border-radius: 50px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1.1rem;
}
.coral-btn {
  background: linear-gradient(45deg, #FF5E5E, #FF8E8E);
  color: white;
  box-shadow: 0 4px 15px rgba(255, 94, 94, 0.4);
}
.teal-btn {
  background: #0A6E6A;
  color: white;
  box-shadow: 0 4px 15px rgba(10, 110, 106, 0.4);
}
.coral-btn:hover, .teal-btn:hover { transform: scale(1.05); }
.glow-effect:hover { box-shadow: 0 0 20px rgba(255, 94, 94, 0.6); }
.points-teaser {
  background: rgba(255,215,0,0.2);
  padding: 1rem;
  border-radius: 10px;
  font-weight: 500;
}
.hero-image {
  text-align: center;
}
.student-illus {
  font-size: 8rem;
  opacity: 0.8;
}
@media (max-width: 768px) {
  .hero-content { grid-template-columns: 1fr; text-align: center; gap: 2rem; }
  .hero-text h2 { font-size: 2rem; }
  .hero-ctas { justify-content: center; }
}
</style>
