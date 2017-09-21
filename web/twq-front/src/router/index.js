import Vue from 'vue';
import Router from 'vue-router';

import Login from '@/components/Login';
import Home from '@/components/Home';
import CriarForm from '@/components/CriarForm';
import ListarForms from '@/components/ListarForms';
import Responder from '@/components/Responder';
import Graphic from '@/components/Graphic';
import EnvioRelatorio from '@/components/EnvioRelatorio'
import ListarRelatorios from '@/components/ListarRelatorios'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login/',
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
      path: '/graphic',
      name: 'Graphic',
      component: Graphic
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
});
