<template>
  <section class="home-view">
    <h1>Welkom bij WatNu18</h1>
    <p>Klik op "FAQ" om de vragenpagina te bekijken.</p>
    <router-link class="btn" to="/vragen">Ga naar FAQ</router-link>
  </section>
</template>

<script setup></script>

<style scoped>
.home-view {
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #fff;
  text-align: center;
  padding: 3rem 1rem;
}

.home-view h1 {
  margin-bottom: 1rem;
  font-size: 2rem;
}

.home-view p {
  margin-bottom: 1.25rem;
  opacity: 0.9;
}

.btn {
  background: #2a6dff;
  color: white;
  padding: 0.75rem 1.3rem;
  border-radius: 9px;
  text-decoration: none;
  font-weight: 600;
}

.btn:hover {
  background: #4e95ff;
}
</style>
