<template>
    <div>
        <h3>Pinterest Template</h3>
        <scroll-loader :loader-method="get10Images" :loader-enable="loadMore">
            
        </scroll-loader>
        <div 
                v-images-loaded:on.progress="imagesProgress"
                v-masonry origin-left="true"
                transition-duration="0.3s" 
                item-selector=".grid-item"
                horizontal-order="false"
                fit-width="true"
                class="grid">
                <!-- .grid-sizer empty element, only used for element sizing -->
                <div class="grid-sizer"></div>
                <div v-masonry-tile 
                    v-bind:class="`grid-item ${im.class}`" 
                    v-for="im in images" :key="im.id">
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
import ScrollLoader from 'vue-scroll-loader';
import axios from 'axios'
export default {
    name: 'Pinterest',
    components: {
        VueMasonryPlugin,
        ScrollLoader
    },
    directives: {
        imagesLoaded
    },
    data () {
        return {
            loadMore: true,
            images: [],
            sPoint: 0
        }
    },
    methods: {
        loadMoreFServer(){
            const path = 'http://localhost:5000/api/images'
            axios.get(path)
            .then(response => {
                this.images.push(...response.data)
                const tempoData = response.data;
                const items = [];
                for(let i=0; i< tempoData.length; i++)
                    items.append({i});
                this.images.extend(items);

                this.sPoint += 10;
            })
            .catch(error => {
                console.log(error)
            })
        },
        imagesProgress(instance, image) {
            // const result = image.isLoaded ? 'loaded' : 'broken';
            // console.log('image is '+ result + ' for ' + image.img.src );
        },
        get10Images(){
            const path = 'http://localhost:5000/api/images'
            axios.get(path,{
                params: {
                    start: this.sPoint
                }
            })
            .then(response => {
                this.images.concat(response.data)

                this.sPoint += 10
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    created () {
        this.loadMoreFServer();
        this.imagesProgress();
    },
    mounted () {
        this.get10Images()
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
