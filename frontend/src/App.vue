<template>
  <div id="app">
    <img src="./assets/logo.png">
    <mHelloWorld/>
    <router-view/>
  </div>
</template>

<script>
import mHelloWorld from "@/components/mHelloWorld";

export default {
  name: 'App',
  components: {
    mHelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
