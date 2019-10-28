import Vue from 'vue'
import VueRouter from 'vue-router'

// Components
import Home from '@/components/Home'
import About from '@/components/About'
import Pinterest from '@/components/Pinterest'
import NotFound from '@/components/NotFound'

const routerOptions = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/pinterest',
        name: 'Pinterest',
        component: Pinterest
    },
    {
        path: '*',
        name: 'NotFound',
        component: NotFound
    }
]

Vue.use(VueRouter)
export default new VueRouter({
    routes: routerOptions,
    mode: 'history'
})