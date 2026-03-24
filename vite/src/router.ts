import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Home from "./views/Home.vue";
import About from "./views/About.vue";
import Somethingidk from "@/views/somethingidk.vue";
import Somethingidk from "./views/somethingidk.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
    meta: { hideLayout: true },
  },
  {
    path: "/idk",
    name: "somethingidk",
    component: Somethingidk,
    meta: { hideLayout: true },
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
