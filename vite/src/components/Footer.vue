<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">Wat<span>Nu</span>18</div>
          <p>Helpt MBO-studenten grip te krijgen op studiefinanciering, OV, verzekeringen en meer — precies als je 18 wordt.</p>
        </div>
        <div class="footer-links-group">
          <h4>Informatie</h4>
          <ul>
            <li><a href="#features" @click.prevent="go('#features')">Jouw 5-stappen plan</a></li>
            <li><a href="#studiefinanciering" @click.prevent="go('#studiefinanciering')">Studiefinanciering</a></li>
            <li><a href="#ov-kaart" @click.prevent="go('#ov-kaart')">OV-studentenkaart</a></li>
            <li><a href="#woonkosten" @click.prevent="go('#woonkosten')">Woonkosten & huurtoeslag</a></li>
            <li><a href="#zorgverzekering" @click.prevent="go('#zorgverzekering')">Zorgverzekering</a></li>
            <li><a href="#documenten" @click.prevent="go('#documenten')">Documenten checklist</a></li>
          </ul>
        </div>
        <div class="footer-links-group">
          <h4>Help & contact</h4>
          <ul>
            <li><a href="mailto:info@watnu.nl">info@watnu.nl</a></li>
            <li><a href="tel:+31612345678">+31 6 12 345 678</a></li>
            <li><a href="#faq" @click.prevent="go('#faq')">Veelgestelde vragen</a></li>
            <li><a href="#privacy" @click.prevent="go('#privacy')">Privacy</a></li>
          </ul>
        </div>
        <div class="footer-social" id="social">
          <h4>Volg ons</h4>
          <div class="social-icons">
            <a href="#social" aria-label="Instagram" @click.prevent="go('#social')"><span>📷</span></a>
            <a href="#social" aria-label="LinkedIn" @click.prevent="go('#social')"><span>in</span></a>
            <a href="#social" aria-label="X" @click.prevent="go('#social')"><span>𝕏</span></a>
            <a href="#social" aria-label="TikTok" @click.prevent="go('#social')"><span>♫</span></a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 WatNu18 — gemaakt voor MBO'ers, door MBO'ers</p>
        <div class="legal-links">
          <a href="#privacy" @click.prevent="go('#privacy')">Privacybeleid</a>
          <span>•</span>
          <a href="#terms" @click.prevent="go('#terms')">Gebruiksvoorwaarden</a>
          <span>•</span>
          <a href="#cookies" @click.prevent="go('#cookies')">Cookievoorkeuren</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { useSiteNavigation } from '../composables/siteNavigation.js'

const go = useSiteNavigation()
</script>

<style scoped>
@import '../styles/variables.css';

.footer {
  background: linear-gradient(135deg, var(--color-gray-900) 0%, var(--color-primary-dark) 100%);
  color: var(--color-white);
  margin-top: var(--spacing-4xl);
  padding: var(--spacing-3xl) var(--spacing-xl) var(--spacing-2xl);
  border-top: 4px solid var(--color-accent);
  overflow: hidden;
  position: relative;
}

.footer::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 300px;
  background: radial-gradient(ellipse at 20% top, rgba(74, 181, 142, 0.12), transparent 60%);
  pointer-events: none;
}

.footer-container {
  position: relative;
  z-index: 2;
  max-width: var(--container-width);
  margin: 0 auto;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--spacing-2xl);
  margin-bottom: var(--spacing-3xl);
}

.footer-brand .footer-logo {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-md);
  letter-spacing: -0.3px;
}

.footer-brand .footer-logo span {
  color: var(--color-accent);
}

.footer-brand p {
  font-size: var(--font-size-sm);
  line-height: var(--line-height-relaxed);
  color: rgba(255,255,255,0.7);
  max-width: 260px;
}

.footer-links-group h4 {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-md);
  color: var(--color-accent-light);
}

.footer-links-group ul {
  list-style: none;
  padding: 0;
}

.footer-links-group li {
  margin-bottom: var(--spacing-sm);
}

.footer-links-group a {
  color: rgba(255,255,255,0.7);
  text-decoration: none;
  font-size: var(--font-size-sm);
  transition: color var(--transition-fast);
}

.footer-links-group a:hover {
  color: var(--color-accent);
  text-decoration: underline;
}

.social-icons {
  display: flex;
  gap: var(--spacing-md);
}

.social-icons a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(255,255,255,0.1);
  border-radius: var(--radius-full);
  font-size: 1.2rem;
  transition: all var(--transition-base);
  text-decoration: none;
  color: white;
}

.social-icons a:hover {
  background: var(--color-accent);
  transform: translateY(-3px);
}

.footer-bottom {
  text-align: center;
  padding-top: var(--spacing-xl);
  border-top: 1px solid rgba(255,255,255,0.1);
  font-size: var(--font-size-xs);
  color: rgba(255,255,255,0.6);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.legal-links {
  display: flex;
  justify-content: center;
  gap: var(--spacing-sm);
  flex-wrap: wrap;
}

.legal-links a {
  color: rgba(255,255,255,0.6);
  text-decoration: none;
}

.legal-links a:hover {
  color: var(--color-accent);
}

@media (max-width: 768px) {
  .footer-grid {
    gap: var(--spacing-xl);
  }
}
</style>