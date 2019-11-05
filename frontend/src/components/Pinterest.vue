<template>
    <div>
        <h3>Pinterest Template</h3>
        <div 
                v-images-loaded:on.progress="imagesProgress"
                v-masonry origin-left="true"
                transition-duration="0.3s" 
                item-selector=".grid-item"
                horizontal-order="false"
                fit-width="true"
                class="grid"
                id="pinterest"
                v-on:scroll.native="handleScroll">
                <!-- .grid-sizer empty element, only used for element sizing -->
                <div class="grid-sizer"></div>
                <div v-masonry-tile 
                    v-bind:class="`grid-item ${im.class}`" 
                    v-for="(im, index) in images" :key="index">
                    <!-- Block item markup -->
                    <img v-bind:src="`${im.url}`" 
                    v-bind:alt="`picture ${im.name}`"/>
                </div>
            </div>
    </div>
</template>
<script>
import { VueMasonryPlugin } from 'vue-masonry';
import imagesLoaded from 'vue-images-loaded';
import axios from 'axios'
export default {
    name: 'Pinterest',
    components: {
        VueMasonryPlugin
    },
    directives: {
        imagesLoaded
    },
    data () {
        return {
            fullStock: 0,
            images: [],
            sPoint: 0
        }
    },
    methods: {
        loadMoreFServer(){
            let path = 'http://localhost:5000/api/getImages'
            if (this.sPoint <= this.fullStock)
                axios.get(path,{
                    params: {
                        'start': this.sPoint
                    }
                })
                .then(response => {
                    let currentData = response.data
                    this.images.push(...currentData)
                    if (this.sPoint < this.fullStock)
                        this.images.concat(currentData);
                        this.sPoint = this.sPoint + 10;
                })
                .catch(error => {
                    console.log(error)
                })
        },
        loadFull(){
            const path = 'http://localhost:5000/api/countTotalImanges'
            axios.get(path)
            .then(response => {
                this.fullStock = response.data
            })
            .catch(error => {
                console.log(error)
            })
        },
        imagesProgress(instance, image) {
            // const result = image.isLoaded ? 'loaded' : 'broken';
            // console.log('image is '+ result + ' for ' + image.img.src );
        },
        handleScroll () {
            // code to be executed when the window is scrolled.
            let container = document.getElementById('pinterest')
            if ((window.scrollY > container.clientHeight * 0.8) && (this.fullStock > this.sPoint))
                console.log(this.sPoint)
                this.loadMoreFServer()
        }
    },
    created () {
        this.loadFull();
        this.loadMoreFServer();
        this.imagesProgress();
        window.addEventListener('scroll', this.handleScroll);
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll);
    }
}
</script>
<style scoped>
.grid-sizer,
.grid-item { 
    width: 240px; 
    padding: 5px;
}

.grid-item--width2 {  }

.grid-item img{
    width: 100%;
}
h3 {
        font-weight: normal;
        padding-top: 20px;
        padding-bottom: 30px
    }

    /* https://vuejsexamples.com/a-scroll-loading-component-for-vue-js/ */
</style>
