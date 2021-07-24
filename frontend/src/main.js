import "bootstrap/dist/css/bootstrap.css";
import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import BootstrapVue from "bootstrap-vue";
Vue.config.productionTip = false
Vue.use(BootstrapVue);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
