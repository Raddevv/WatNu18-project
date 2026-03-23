<template>
  <header class="header">
    <div class="header-container">
      <div class="logo-section">
        <div class="logo">
          <image src="src/assets/img/... .svg" alt="LOGO" class="logo-image" />
        </div>
      </div>

      <div class="title-section">
        <h1 class="header-title"></h1>
      </div>

      <div class="nav-section">
        <div class="features-menu">
          <button class="features-btn" title="Alle onderdelen">
            <span class="features-icon">
              <image src="src/assets/img/bookicon.png" alt="Book Icon" />
            </span>
          </button>
          <div class="features-dropdown">
            <a href="#about">Over WatNu18</a>
            <a href="#studiefinancing">Studiefinanciering</a>
            <a href="#ov-kaart">OV-studentenkaart</a>
            <a href="#woonkosten">Woonkosten</a>
            <a href="#documenten">Documenten</a>
            <a href="#faq">Veelgestelde Vragen</a>
            <a href="#contact">Contact</a>
          </div>
        </div>

        <a href="/" class="home-btn" title="Terug naar home">
          <span class="home-icon">
            <image src="src/assets/img/hsicon.png" alt="Home Icon" />
          </span>
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
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 3px solid var(--color-accent);
  color: white;
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
  stroke: var(--color-accent);
  transition: all 0.3s ease;
}

.logo-lines:hover {
  filter: drop-shadow(0 0 8px rgba(8, 145, 178, 0.5));
}

.logo-placeholder {
  color: white;
  font-size: 2rem;
  font-weight: bold;
  padding: 0.5rem 0.75rem;
  background-color: rgba(8, 145, 178, 0.2);
  border-radius: 6px;
  border: 2px solid var(--color-accent);
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.logo-placeholder:hover {
  background-color: rgba(8, 145, 178, 0.3);
  box-shadow: 0 0 10px rgba(8, 145, 178, 0.4);
}

.logo-image {
  height: 50px;
  width: auto;
  max-width: 200px;
  object-fit: contain;
}

.title-section {
  flex: 1;
  text-align: center;
}

.header-title {
  color: rgba(255, 255, 255, 0.9);
  text-indent: 12px;
  font-size: 2rem;
  font-weight: bold;
  margin: 0;
  letter-spacing: 2px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.nav-section {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-shrink: 0;
}

.features-menu {
  position: relative;
}

.features-btn {
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  padding: 0.75rem 1rem;
  border: 2px solid var(--color-accent);
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
  background-color: var(--color-accent);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(8, 145, 178, 0.4);
  border-color: white;
  color: white;
}

.features-icon {
  font-size: 1.5rem;
  rotate: 8deg;
  scale: 0.1;
}

.features-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: white;
  color: var(--color-primary);
  min-width: 240px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  margin-top: 0.5rem;
  overflow: hidden;
  border: 2px solid var(--color-accent);
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
  color: var(--color-primary);
  padding: 1rem 1.5rem;
  text-decoration: none;
  display: block;
  transition: all 0.3s ease;
  border-left: 4px solid transparent;
  font-weight: 500;
}

.features-dropdown a:hover {
  background-color: var(--color-primary);
  border-left-color: var(--color-accent);
  padding-left: 2rem;
  color: white;
}

.home-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background-color: rgba(0, 0, 0, 0.1);
  border: 2px solid white;
  border-radius: 8px;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.3s ease;
  color: white;
}

.home-btn:hover {
  background-color: white;
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-color: white;
  color: var(--color-primary);
}

.home-icon {
  font-size: 1.5rem;
  scale: 0.1;
}

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