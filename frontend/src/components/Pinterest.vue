<template>
    <div>
        <h3>Pinterest Template</h3>
        <div v-masonry origin-left="true"
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
                v-bind:alt="`${im.name}`"/>
            </div>
        </div>
    </div>
</template>
<script>
import { VueMasonryPlugin } from 'vue-masonry';
import axios from 'axios'
export default {
    components: {
        VueMasonryPlugin
    },
    data () {
        return {
            images: 0
        }
    },
    methods: {
        getImagesFromServer (){
            const path = 'http://localhost:5000/api/images'
            axios.get(path)
            .then(response => {
                this.images = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    created () {
        this.getImagesFromServer()
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
</style>
