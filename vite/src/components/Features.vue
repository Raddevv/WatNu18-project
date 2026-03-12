<template>
  <section class="features-section charcoal-bg">
    <div class="features-container">
      <h2>Je Studiefinanciering Toolkit</h2>
      <p class="section-subtitle">Verdien punten door interactie! Ontgrendel badges bij milestones.</p>
      <div class="features-grid">
        <div class="feature-card teal-card" @click="activateFeature(1)">
          <div class="card-icon">🧮</div>
          <h3>Bereken Eligibility</h3>
          <p>Check basisbeurs, lening & toeslag op basis van inkomen/leeftijd.</p>
          <button class="earn-btn coral-btn">Bereken (+50pts)</button>
        </div>
        <div class="feature-card coral-card" @click="activateFeature(2)">
          <div class="card-icon">📊</div>
          <h3>Aanvraagstatus</h3>
          <p>Volg je DUO-aanvraag realtime met notificaties.</p>
          <button class="earn-btn gold-accent">Check Status (+30pts)</button>
        </div>
        <div class="feature-card gold-card" @click="activateFeature(3)">
          <div class="card-icon">💡</div>
          <h3>Tips & Tricks</h3>
          <p>Maximaliseer je financiering met slimme hacks.</p>
          <button class="earn-btn teal-btn">Lees Tips (+20pts)</button>
        </div>
        <div class="feature-card diamond-card" @click="activateFeature(4)">
          <div class="card-icon">❓</div>
          <h3>Wetensquiz</h3>
          <p>Test kennis studiefinanciering – bonuspunten!</p>
          <button class="earn-btn coral-glow">Start Quiz (+100pts)</button>
        </div>
        <div class="feature-card teal-card" @click="activateFeature(5)">
          <div class="card-icon">🏆</div>
          <h3>Badge Gallery</h3>
          <p>Bekijk & deel je verdiende achievements.</p>
          <button class="earn-btn gold-btn">Bekijk Badges</button>
        </div>
      </div>
      <div class="leaderboard-teaser">
        <span>Top spelers deze week: Max (2450pts) | Sara (1980pts)</span>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'FeaturesComponent',
  data() {
    return {
      features: [
        { id: 1, points: 50 },
        { id: 2, points: 30 },
        { id: 3, points: 20 },
        { id: 4, points: 100 },
        { id: 5, points: 0 }
      ]
    };
  },
  methods: {
    activateFeature(id) {
      const feature = this.features.find(f => f.id === id);
      if (feature.points > 0) {
        alert(`Feature geactiveerd! +${feature.points} punten verdiend. Check je header voor update!`);
        console.log(`Feature ${id} activated, +${feature.points}pts`);
      } else {
        alert('Bekijk je badges – deelbaar op socials!');
      }
    }
  }
};
</script>

<style scoped>
.features-section {
  color: #F7FAFC;
  padding: 4rem 2rem;
}
.features-container {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}
.section-subtitle {
  font-size: 1.2rem;
  margin-bottom: 3rem;
  opacity: 0.9;
}
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}
.feature-card {
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(255,255,255,0.2);
}
.feature-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}
.teal-card { border-left: 5px solid #0A6E6A; }
.coral-card { border-left: 5px solid #FF5E5E; }
.gold-card { border-left: 5px solid #FFD700; }
.diamond-card { border-left: 5px solid linear-gradient(45deg, #FFD700, #FF5E5E); }
.card-icon { font-size: 3rem; display: block; margin-bottom: 1rem; }
.feature-card h3 { margin-bottom: 1rem; }
.earn-btn {
  margin-top: 1rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 25px;
  font-weight: bold;
  transition: all 0.3s;
}
.coral-btn, .coral-glow {
  background: linear-gradient(45deg, #FF5E5E, #FF8E8E);
  color: white;
}
.teal-btn { background: #0A6E6A; color: white; }
.gold-accent, .gold-btn {
  background: linear-gradient(45deg, #FFD700, #FFA500);
  color: #2D3748;
}
.earn-btn:hover { transform: scale(1.05); }
.leaderboard-teaser {
  background: rgba(255,215,0,0.2);
  padding: 1rem 2rem;
  border-radius: 10px;
  font-weight: 500;
}
@media (max-width: 768px) {
  .features-grid { grid-template-columns: 1fr; }
}
</style>
