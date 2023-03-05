import Vue from "vue";
import Router from "vue-router";
import answer from "@/views/answer/index.vue";
Vue.use(Router);

export default new Router({
  routes: [

    {
      path: "/",
      name: "answer",
      component: answer
    },
    {
      path: "/answer",
      name: "answer",
      component: answer
    },
  ]
});
