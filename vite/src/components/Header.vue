<template>
  <header class="header">
    <div class="header-container">
      <!-- Logo aan de linkerkant - SVG lijntjes -->
      <div class="logo-section">
        <div class="logo">
          <svg class="logo-lines" viewBox="0 0 50 50" width="40" height="40">
            <!-- Bolvormige top (lamp) -->
            <circle cx="25" cy="18" r="12" fill="none" stroke="#ED217C" stroke-width="1.5"/>
            <!-- Gloeidraad -->
            <path d="M 20 18 Q 25 25 20 30" fill="none" stroke="#ED217C" stroke-width="1"/>
            <!-- Fitting -->
            <rect x="22" y="30" width="6" height="8" fill="none" stroke="#ED217C" stroke-width="1.5"/>
            <!-- Schroefdraad -->
            <line x1="20" y1="32" x2="30" y2="32" stroke="#ED217C" stroke-width="1"/>
            <line x1="19" y1="34" x2="31" y2="34" stroke="#ED217C" stroke-width="1"/>
            <line x1="20" y1="36" x2="30" y2="36" stroke="#ED217C" stroke-width="1"/>
          </svg>
        </div>
      </div>

      <!-- Watnu titel in het midden -->
      <div class="title-section">
        <h1 class="header-title">Watnu</h1>
      </div>

      <!-- Navigation aan de rechterkant -->
      <div class="nav-section">
        <!-- Expandable menu voor features -->
        <div class="features-menu">
          <button class="features-btn" title="Alle onderdelen">
            <span class="features-icon">📚</span>
          </button>
          <div class="features-dropdown">
            <a href="#about">Over Watnu</a>
            <a href="#studiefinancing">Studiefinanciering</a>
            <a href="#ov-kaart">OV-studentenkaart</a>
            <a href="#woonkosten">Woonkosten</a>
            <a href="#documenten">Documenten</a>
            <a href="#faq">Veelgestelde Vragen</a>
            <a href="#contact">Contact</a>
          </div>
        </div>

        <!-- Home button - House icon made of lines -->
        <router-link to="/" class="home-btn" title="Terug naar home">
          <svg class="home-icon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
            <polyline points="9 22 9 12 15 12 15 22"></polyline>
          </svg>
        </router-link>
      </div>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
.header {
  background: linear-gradient(135deg, rgba(44, 7, 53, 0.95) 0%, rgba(26, 0, 33, 0.98) 100%);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4), 0 0 20px rgba(237, 33, 124, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 2px solid rgba(237, 33, 124, 0.3);
}

.header-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0.5rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

/* Logo sectie - meer naar links */
.logo-section {
  flex-shrink: 0;
  flex: 0 0 auto;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-lines {
  width: 40px;
  height: 40px;
  stroke: #ED217C;
  transition: all 0.3s ease;
}

.logo-lines:hover {
  filter: drop-shadow(0 0 8px rgba(237, 33, 124, 0.5));
}

.logo-placeholder {
  color: #F6F4F3;
  font-size: 2rem;
  font-weight: bold;
  padding: 0.5rem 0.75rem;
  background-color: rgba(237, 33, 124, 0.2);
  border-radius: 6px;
  border: 2px solid #ED217C;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.logo-placeholder:hover {
  background-color: rgba(237, 33, 124, 0.3);
  box-shadow: 0 0 10px rgba(237, 33, 124, 0.4);
}

.logo-image {
  height: 50px;
  width: auto;
  max-width: 200px;
  object-fit: contain;
}

/* Titel in het midden */
.title-section {
  flex: 1;
  text-align: center;
}

.header-title {
  color: #F6F4F3;
  font-size: 2rem;
  font-weight: bold;
  margin: 0;
  letter-spacing: 2px;
  text-shadow: 0 2px 10px rgba(237, 33, 124, 0.3);
}

/* Navigation sectie - aan de rechterkant */
.nav-section {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-shrink: 0;
}

/* Features menu */
.features-menu {
  position: relative;
}

.features-btn {
  background-color: rgba(237, 33, 124, 0.2);
  color: #F6F4F3;
  padding: 0.75rem 1rem;
  border: 2px solid #ED217C;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  width: 50px;
  height: 50px;
}

.features-btn:hover {
  background-color: rgba(237, 33, 124, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(237, 33, 124, 0.4);
  border-color: #F6F4F3;
}

.features-icon {
  font-size: 1.5rem;
}

.features-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: #F6F4F3;
  min-width: 240px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  border-radius: 8px;
  margin-top: 0.5rem;
  overflow: hidden;
  border: 2px solid #ED217C;
  z-index: 1000;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all 0.3s ease;
  pointer-events: none;
}

.features-menu:hover .features-dropdown {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  pointer-events: auto;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.features-dropdown a {
  color: #2C0735;
  padding: 1rem 1.5rem;
  text-decoration: none;
  display: block;
  transition: all 0.3s ease;
  border-left: 4px solid transparent;
  font-weight: 500;
}

.features-dropdown a:hover {
  background-color: rgba(237, 33, 124, 0.1);
  border-left-color: #ED217C;
  padding-left: 2rem;
  color: #ED217C;
}

/* Home button */
.home-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background-color: rgba(237, 33, 124, 0.2);
  border: 2px solid #ED217C;
  border-radius: 8px;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.3s ease;
  color: #F6F4F3;
}

.home-btn:hover {
  background-color: rgba(237, 33, 124, 0.3);
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 4px 8px rgba(237, 33, 124, 0.4);
  border-color: #F6F4F3;
}

.home-icon {
  width: 24px;
  height: 24px;
  stroke: #F6F4F3;
}

/* Responsive */
@media (max-width: 768px) {
  .header-container {
    padding: 0.5rem 1rem;
    gap: 0.5rem;
  }

  .header-title {
    font-size: 1.5rem;
  }

  .logo-placeholder {
    font-size: 1.5rem;
  }

  .logo-image {
    height: 40px;
  }

  .features-btn {
    width: 45px;
    height: 45px;
  }

  .home-btn {
    width: 45px;
    height: 45px;
  }

  .features-dropdown {
    min-width: 200px;
  }
}

@media (max-width: 480px) {
  .header-container {
    flex-wrap: wrap;
    padding: 0.5rem;
  }

  .title-section {
    order: 2;
    flex-basis: 100%;
    margin: 0.5rem 0;
  }

  .header-title {
    font-size: 1.2rem;
  }

  .nav-section {
    order: 3;
    width: 100%;
    justify-content: flex-end;
  }

  .logo-section {
    order: 1;
  }
}
</style>
