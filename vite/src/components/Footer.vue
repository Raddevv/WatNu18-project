<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-content">
        <!-- Kolom 1: Over ons -->
        <div class="footer-section">
          <h3>Over Watnu</h3>
          <p>
            Watnu helpt MBO studenten begrijpen hoe studiefinanciering, OV-studentenkaarten 
            en andere zaken werken als je 18 word. We maken het ingewikkelde simpel!
          </p>
        </div>

        <!-- Kolom 2: Handige Links -->
        <div class="footer-section">
          <h3>Handige Links</h3>
          <ul>
            <li><a href="#studiefinancing">Studiefinanciering</a></li>
            <li><a href="#ov-kaart">OV-studentenkaart</a></li>
            <li><a href="#woonkosten">Woonkosten</a></li>
            <li><a href="#faq">Veelgestelde Vragen</a></li>
          </ul>
        </div>

        <!-- Kolom 3: Contact -->
        <div class="footer-section">
          <h3>Contact</h3>
          <p>
            <strong>Email:</strong> <a href="mailto:info@watnu.nl">info@watnu.nl</a><br>
            <strong>Telefoon:</strong> <a href="tel:+31612345678">+31 6 12 345 678</a><br>
            <strong>Adres:</strong> Nederland
          </p>
        </div>

        <!-- Kolom 4: Socials -->
        <div class="footer-section">
          <h3>Volg ons</h3>
          <div class="social-links">
            <a href="#facebook" class="social-btn" title="Facebook">f</a>
            <a href="#instagram" class="social-btn" title="Instagram">📷</a>
            <a href="#linkedin" class="social-btn" title="LinkedIn">in</a>
            <a href="#twitter" class="social-btn" title="Twitter">𝕏</a>
          </div>
        </div>
      </div>

      <!-- Divider -->
      <div class="footer-divider"></div>

      <!-- Copyright -->
      <div class="footer-bottom">
        <p>&copy; 2026 Watnu. Alle rechten voorbehouden.</p>
        <div class="footer-links">
          <a href="#privacy">Privacybeleid</a>
          <span class="divider">|</span>
          <a href="#terms">Gebruiksvoorwaarden</a>
          <span class="divider">|</span>
          <a href="#cookies">Cookiebeleid</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
// Footer component logic kan hier worden toegevoegd
</script>

<style scoped>
.footer {
  background: linear-gradient(135deg, #0D3B2F 0%, #061820 100%);
  color: #F6F4F3;
  margin-top: 4rem;
  padding: 3rem 2rem 1rem;
  border-top: 3px solid #00D9A3;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-section {
  padding: 0 1rem;
}

.footer-section h3 {
  color: #00D9A3;
  font-size: 1.1rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

.footer-section p {
  line-height: 1.6;
  color: #F6F4F3;
  font-size: 0.95rem;
  margin-bottom: 1rem;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section ul li {
  margin-bottom: 0.5rem;
}

.footer-section a {
  color: #F6F4F3;
  text-decoration: none;
  transition: all 0.3s ease;
}

.footer-section a:hover {
  color: #00D9A3;
  text-decoration: underline;
}

/* Social Links */
.social-links {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.social-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: rgba(0, 217, 163, 0.1);
  border: 2px solid #00D9A3;
  border-radius: 50%;
  color: #00D9A3;
  text-decoration: none;
  transition: all 0.3s ease;
  font-weight: bold;
  font-size: 0.9rem;
}

.social-btn:hover {
  background-color: #00D9A3;
  color: #F6F4F3;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 217, 163, 0.4);
}

/* Footer Divider */
.footer-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.1);
  margin: 2rem 0;
}

/* Footer Bottom */
.footer-bottom {
  text-align: center;
  padding: 1.5rem 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-bottom p {
  color: #F6F4F3;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.footer-links a {
  color: #F6F4F3;
  font-size: 0.85rem;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: #00D9A3;
}

.divider {
  color: rgba(255, 255, 255, 0.2);
}

/* Responsive */
@media (max-width: 768px) {
  .footer {
    padding: 2rem 1rem 1rem;
  }

  .footer-content {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .footer-section {
    padding: 0;
  }

  .footer-bottom {
    padding: 1rem 0;
  }

  .footer-links {
    gap: 0.5rem;
  }
}

@media (max-width: 480px) {
  .footer {
    padding: 1.5rem 0.5rem 0.5rem;
  }

  .footer-section h3 {
    font-size: 1rem;
  }

  .footer-section p {
    font-size: 0.85rem;
  }

  .footer-links {
    flex-direction: column;
    gap: 0.5rem;
  }

  .divider {
    display: none;
  }
}
</style>
