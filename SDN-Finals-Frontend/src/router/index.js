import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PackageOperation from "@/components/PackageOperation.vue";
import QueryOperation from "@/components/QueryOperation.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      children:[{
        path: 'package-operation',
        name: 'package-operation',
        component: PackageOperation,
      },{
        path: 'query-package',
        name: 'query-package',
        component: QueryOperation,
      }


      ]
    },
  ]
})

export default router
