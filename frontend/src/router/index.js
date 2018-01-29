import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Dashboard from '@/components/Dashboard'
import GroupMessages from '@/components/Message/GroupMessages'
import PrivateMessages from '@/components/Message/PrivateMessages'

import AuthGuard from './auth-guard'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      beforeEnter: AuthGuard,
      children: [
        {
          path: 'member/:id',
          component: PrivateMessages
        },
        {
          path: 'group/:slug',
          component: GroupMessages
        }
      ]
    }
  ]
})
