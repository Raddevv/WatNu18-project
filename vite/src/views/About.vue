<template>
  <div>
    <Header />
    <main class="main-content">
      <h1>About</h1>
      <p>Dit is de about pagina.</p>
      <router-link to="/">Terug naar Home</router-link>
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";

export default {
  name: "About",
  components: {
    Header,
    Footer,
  },
};
</script>

<style scoped>
.main-content {
  padding: 20px;
}
</style>
