
import { createRouter, createWebHashHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import goodsComponent from '../components/goodsComponent.vue'
import stocksComponent from '../components/stocksComponent.vue'
import goodincomesComponent from '../components/goodincomesComponent.vue'
import goodmovesComponent from '../components/goodmovesComponent.vue'
import goodrestsComponent from '../components/goodrestsComponent.vue'
import AboutView from '../views/AboutView.vue'
const routes = [
  {
    path: '/goods',
    name: 'Goods',
    component: goodsComponent
  },
  {
    path: '/stocks',
    name: 'Stocks',
    component: stocksComponent
  }
  ,
  {
    path: '/goodincomes',
    name: 'Goodincomes',
    component: goodincomesComponent
  }
  ,
  {
    path: '/goodmoves',
    name: 'Goodmoves',
    component: goodmovesComponent
  }  
  ,
  {
    path: '/goodrests',
    name: 'Goodrests',
    component: goodrestsComponent
  },
  {
    path: '/',
    name: 'About',
    component: AboutView
  }     
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

