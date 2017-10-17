import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import CriarForm from '@/components/CriarForm'
import Home from '@/components/Home'
import ListarForms from '@/components/ListarForms'
import Responder from '@/components/Responder'
import EnvioRelatorio from '@/components/EnvioRelatorio'
import ListarRelatorios from '@/components/ListarRelatorios'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/login/',
      name: 'Login',
      component: Login
    },
    {
    	path: '/criarForm',
    	name: 'CriarForm',
    	component: CriarForm
    },
    {
    	path: '/listarForms',
    	name: 'ListarForms',
    	component: ListarForms
    },
    {
      path: '/Responder',
      name: 'Responder',
      component: Responder
    },
    {
      path: '/envioRelatorio',
      name: 'EnvioRelatorio',
      component: EnvioRelatorio
    },
    {
      path: '/listarRelatorios',
      name: 'ListarRelatorios',
      component: ListarRelatorios
    }
  ]
})
