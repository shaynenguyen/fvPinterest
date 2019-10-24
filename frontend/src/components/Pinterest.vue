<template>
    <div>
        <h3>Pinterest Template</h3>
        <div v-masonry="containerId" transition-duration="0.3s" item-selector=".grid">
            <div v-masonry-tile 
                v-bind:class="`grid-item ${im.class}`" 
                v-for="im in images" :key="im.id">
                <!-- Block item markup -->
                <img v-bind:src="`http://localhost:5000/uploads/images/${im.name}`" 
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
.grid-item{
    width:33%;
    padding:5px;
    margin:5px;
    float:left;
    position: relative;
}
.grid-item--width{
    width:66%;
}

.grid-item img{
    position: relative;
    width:100%;
}
</style>