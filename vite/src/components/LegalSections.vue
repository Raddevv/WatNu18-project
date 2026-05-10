<template>
  <section class="legal-sections" aria-label="Juridische informatie">
    <div class="legal-inner">
      <article id="privacy" class="legal-card" tabindex="-1">
        <h2>Privacy</h2>
        <p>
          WatNu18 is een schoolproject. We verwerken geen accountgegevens op deze demo-site. Gebruik de chat
          niet om BSN, ID of bankgegevens te delen. Voor productie zou hier een volledig privacybeleid staan.
        </p>
      </article>
      <article id="terms" class="legal-card" tabindex="-1">
        <h2>Gebruiksvoorwaarden</h2>
        <p>
          De inhoud is bedoeld als oriëntatie voor MBO-studenten. Officiële regels kun je vinden bij DUO, de
          Belastingdienst en andere overheidsbronnen. Geen rechten kunnen worden ontleend aan deze site.
        </p>
      </article>
      <article id="cookies" class="legal-card" tabindex="-1">
        <h2>Cookievoorkeuren</h2>
        <p>
          Deze demo gebruikt alleen technisch noodzakelijke cookies zoals je browser die zet. Er is geen
          marketing-tracker geconfigureerd. Later kun je hier een echte cookie-banner koppelen.
        </p>
      </article>
    </div>
  </section>
</template>

<style scoped>
@import '../styles/variables.css';

.legal-sections {
  background: var(--color-gray-900);
  color: rgba(255, 255, 255, 0.85);
  padding: var(--spacing-3xl) var(--spacing-xl);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.legal-inner {
  max-width: var(--container-width);
  margin: 0 auto;
  display: grid;
  gap: var(--spacing-xl);
}

.legal-card {
  scroll-margin-top: 5.5rem;
}

.legal-card h2 {
  font-size: var(--font-size-xl);
  color: var(--color-accent);
  margin-bottom: var(--spacing-sm);
}

.legal-card p {
  font-size: var(--font-size-sm);
  line-height: var(--line-height-relaxed);
  max-width: 720px;
}
</style>
