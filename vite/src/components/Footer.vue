<template>
  <footer class="site-footer teal-bg">
    <div class="footer-content">
      <div class="footer-section">
        <p>&copy; 2024 Studiefinanciering Coach. Alle rechten voorbehouden.</p>
        <p>Inspiratie: DUO.nl – Jouw partner in studiefinanciering.</p>
      </div>
      <nav class="footer-nav">
        <a href="#">Privacybeleid</a>
        <a href="#">Gebruiksvoorwaarden</a>
        <a href="#">Helpdesk</a>
        <a href="#leaderboard">Leaderboard</a>
        <a href="https://duo.nl" target="_blank">Officiële DUO Site</a>
      </nav>
      <div class="footer-gami">
        <span>Deel je score! 🏆 #StudieFinCoach</span>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent'
};
</script>

<style scoped>
.site-footer {
  background: linear-gradient(135deg, #0A6E6A 0%, #2D3748 100%);
  color: #F7FAFC;
  padding: 2rem;
  margin-top: 4rem;
}
.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
}
.footer-section p { margin: 0 0 0.5rem 0; opacity: 0.9; }
.footer-nav {
  display: flex;
  gap: 2rem;
}
.footer-nav a {
  color: #F7FAFC;
  text-decoration: none;
  transition: color 0.3s;
}
.footer-nav a:hover { color: #FFD700; }
.footer-gami {
  background: rgba(255, 94, 94, 0.2);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 500;
}
@media (max-width: 768px) {
  .footer-content { flex-direction: column; text-align: center; }
  .footer-nav { flex-wrap: wrap; justify-content: center; }
}
</style>
