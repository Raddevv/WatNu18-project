<template>
  <main class="notfound">
    <h2>Pagina niet gevonden</h2>
    <p>De URL die je probeerde bestaat niet.</p>
    <button @click="$router.push('/')">Terug naar start</button>
  </main>
</template>

<script setup></script>

<style scoped>
.notfound {
  padding: 2rem;
  text-align: center;
}
.notfound button {
  margin-top: 1rem;
  padding: 0.8rem 1.2rem;
  background: #0057d9;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
</style>
