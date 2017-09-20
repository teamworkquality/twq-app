import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import CriarForm from '@/components/CriarForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
    	path: '/criarForm',
    	name: 'CriarForm',
    	component: CriarForm
    }
  ]
})
