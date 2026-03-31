<template>
  <header class="header">
    <div class="header-container">
      <div class="logo-section">
        <a href="/" class="logo-link" aria-label="WatNu18 homepage">
          <div class="logo-mark">
            <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8 20L20 8L32 20L20 32L8 20Z" stroke="var(--color-accent)" stroke-width="2" fill="none"/>
              <circle cx="20" cy="20" r="4" fill="var(--color-accent)"/>
            </svg>
          </div>
          <span class="logo-text">Wat<span>Nu</span>18</span>
        </a>
      </div>

      <div class="nav-section">
        <div class="features-menu">
          <button class="features-btn" aria-label="Menu">
<svg width="72" height="72" viewBox="0 0 72 72" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round">
  <line x1="18" y1="26" x2="54" y2="26" />
  <line x1="18" y1="36" x2="54" y2="36" />
  <line x1="18" y1="46" x2="54" y2="46" />
</svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <div class="features-dropdown">
            <a href="#studiefinanciering">📘 Studiefinanciering</a>
            <a href="#ov-kaart">🚆 OV-studentenkaart</a>
            <a href="#woonkosten">🏠 Woonkosten & toeslagen</a>
            <a href="#verzekeringen">🛡️ Zorgverzekering</a>
            <a href="#documenten">📄 Belangrijke documenten</a>
            <a href="#faq">❓ Veelgestelde vragen</a>
          </div>
        </div>
        <a href="/" class="home-btn" aria-label="Home">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 9L12 3L21 9L21 19C21 19.5304 20.7893 20.0391 20.4142 20.4142C20.0391 20.7893 19.5304 21 19 21H5C4.46957 21 3.96086 20.7893 3.58579 20.4142C3.21071 20.0391 3 19.5304 3 19V9Z"/>
            <path d="M9 21V12H15V21"/>
          </svg>
        </a>
      </div>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
@import '../styles/variables.css';

.header {
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  box-shadow: var(--shadow-md);
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  border-bottom: 3px solid var(--color-accent);
}

.header-container {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: var(--spacing-md) var(--spacing-xl);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--spacing-md);
}

.logo-section {
  flex-shrink: 0;
}

.logo-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  text-decoration: none;
  transition: opacity var(--transition-fast);
}

.logo-link:hover {
  opacity: 0.9;
}

.logo-mark {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,0.1);
  border-radius: var(--radius-lg);
  transition: transform var(--transition-base);
}

.logo-link:hover .logo-mark {
  transform: scale(1.02);
}

.logo-text {
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-bold);
  color: var(--color-white);
  letter-spacing: -0.3px;
}

.logo-text span {
  color: var(--color-accent);
  font-weight: 800;
}

.nav-section {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

.features-menu {
  position: relative;
}

.features-btn {
  background: rgba(255,255,255,0.08);
  border: none;
  padding: var(--spacing-sm) var(--spacing-lg);
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  font-weight: var(--font-weight-semibold);
  font-size: var(--font-size-sm);
  color: var(--color-white);
  cursor: pointer;
  transition: all var(--transition-base);
  backdrop-filter: blur(4px);
}

.features-btn:hover {
  background: rgba(255,255,255,0.2);
  transform: translateY(-1px);
}

.features-btn svg {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.features-btn svg:first-child {
  width: 28px;
  height: 28px;
}

.features-btn svg:last-child {
  width: 14px;
  height: 14px;
  opacity: 0.8;
}

.features-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: var(--color-white);
  min-width: 260px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  margin-top: var(--spacing-sm);
  overflow: hidden;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-8px);
  transition: all var(--transition-base);
  pointer-events: none;
  border: 1px solid var(--color-gray-200);
}

.features-menu:hover .features-dropdown {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  pointer-events: auto;
}

.features-dropdown a {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-md) var(--spacing-lg);
  color: var(--color-gray-600);
  text-decoration: none;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  transition: all var(--transition-fast);
  border-left: 3px solid transparent;
}

.features-dropdown a:hover {
  background: var(--color-gray-300);
  border-left-color: var(--color-accent);
  padding-left: calc(var(--spacing-lg) + 4px);
}

.home-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  background: rgba(255,255,255,0.08);
  border-radius: var(--radius-full);
  transition: all var(--transition-base);
  color: var(--color-white);
  text-decoration: none;
}

.home-btn:hover {
  background: var(--color-accent);
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

@media (max-width: 768px) {
  .header-container {
    padding: var(--spacing-sm) var(--spacing-lg);
  }
  .logo-text {
    font-size: var(--font-size-lg);
  }
  .features-btn span:first-child {
    display: none;
  }
  .features-btn {
    padding: var(--spacing-sm);
  }
}
</style>