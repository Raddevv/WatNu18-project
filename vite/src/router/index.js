import { createRouter, createWebHistory } from "vue-router";
import VragenView from "../views/VragenView.vue";

const routes = [{ path: "/vragen", name: "Vragen", component: VragenView }];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
