import { createRouter, createWebHistory } from "vue-router";
import HomeView from "./views/HomeView2.vue";
import VragenView from "./views/VragenView.vue";

import NotFound from "./views/NotFound.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/vragen",
    name: "Vragen",
    component: VragenView,
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
