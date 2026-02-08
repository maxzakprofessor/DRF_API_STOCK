import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
//import pdfMake from 'vue3-pdfmake'
import 'bootstrap'

//import './assets/main.css'

const app = createApp(App)

//app.use(pdfMake)

app.use(router)

app.mount('#app')




