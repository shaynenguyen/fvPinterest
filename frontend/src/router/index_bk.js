import Vue from 'vue'
import Router from 'vue-router'
const routerOptions = [
    { path: '/', component: 'Home' },
    { path: '/about', component: 'About' },
    { path: '/pinterest', component: 'Pinterest' },
    { path: '*', component: 'NotFound' }
]
const appRoute = routerOptions.map(route => {
    return {
        ...route,
        component: () =>
            import (`@/components/${route.component}.vue`)
    }
})
Vue.use(Router)
export default new Router({
    routes: appRoute,
    mode: 'history'
})