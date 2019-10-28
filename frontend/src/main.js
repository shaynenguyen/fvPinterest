// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'

import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/build/css/mdb.css'

// import ES6 style
import { VueMasonryPlugin } from 'vue-masonry'

import App from './App'
import router from './router'

Vue.config.productionTip = false
Vue.use(VueMasonryPlugin)

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: {
        App
    },
    template: '<App/>'
})