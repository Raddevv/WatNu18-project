<template>
  <header class="site-header teal-bg">
    <div class="header-container">
      <div class="logo">
        <h1>💰 Studiefinanciering Coach</h1>
      </div>
      <nav class="main-nav">
        <a href="#home">Home</a>
        <a href="#bereken">Bereken</a>
        <a href="#quiz">Quiz</a>
        <a href="#profiel">Profiel</a>
        <a href="https://duo.nl" target="_blank">DUO Portal</a>
      </nav>
      <div class="gamification-hub">
        <div class="points-display">
          <span>Punten: {{ points }}</span>
        </div>
        <div class="badges">
          <span v-for="badge in badges" :key="badge" :class="['badge', getBadgeClass(badge)]">{{ badge }}</span>
        </div>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: progress + '%' }"></div>
          <span>Level {{ currentLevel }} - {{ progress }}%</span>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderComponent',
  data() {
    return {
      points: 250,
      badges: ['Brons'],
      progress: 25,
      currentLevel: 1
    };
  },
  methods: {
    getBadgeClass(badge) {
      const classes = { Brons: 'bronze', Zilver: 'silver', Goud: 'gold', Diamant: 'diamond' };
      return classes[badge] || '';
    },
    earnPoints(amount) {
      this.points += amount;
      // Simulate level up
      if (this.points >= 1000) {
        this.badges.push('Goud');
        this.progress = 0;
        this.currentLevel++;
        alert('🎉 Goud badge ontgrendeld!');
      }
    }
  }
};
</script>

<style scoped>
.site-header {
  background: linear-gradient(135deg, #0A6E6A 0%, #FF5E5E 100%);
  color: white;
  padding: 1rem 0;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
.header-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
}
.logo h1 { margin: 0; font-size: 1.5rem; }
.main-nav a {
  color: white;
  text-decoration: none;
  margin-left: 2rem;
  font-weight: 500;
  transition: color 0.3s;
}
.main-nav a:hover { color: #FFD700; }
.gamification-hub {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.points-display { font-weight: bold; font-size: 1.1rem; }
.badges { display: flex; gap: 0.5rem; }
.badge {
  padding: 0.25rem 0.5rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: bold;
}
.bronze { background: #CD7F32; color: white; }
.silver { background: #C0C0C0; color: white; }
.gold { background: #FFD700; color: #2D3748; }
.diamond { background: linear-gradient(45deg, #FFD700, #FF5E5E); color: white; }
.progress-bar {
  background: rgba(255,255,255,0.2);
  border-radius: 10px;
  padding: 0.5rem;
  min-width: 150px;
}
.progress-fill {
  height: 8px;
  background: #FFD700;
  border-radius: 4px;
  transition: width 0.5s ease;
}
@media (max-width: 768px) {
  .header-container { flex-direction: column; gap: 1rem; }
  .main-nav a { margin-left: 0; margin-right: 1rem; }
}
</style>
