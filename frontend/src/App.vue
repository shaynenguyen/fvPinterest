<template>
  <div id="app">
    <Header/>
    <mdb-container fluid>
       <mdb-row>
        <!-- Left Navigation -->
        <mdb-col md="2" sm="2" class="grey lighten-1">
          <mHelloWorld/>
        </mdb-col>
        <!-- Router View -->
        <mdb-col md="10" sm="10">
          <router-view/>
        </mdb-col>
      </mdb-row>
    </mdb-container>
    <Footer/>
  </div>
</template>

<script>
import { mdbContainer, mdbRow, mdbCol } from 'mdbvue';
import mHelloWorld from '@/components/_mHelloWorld';
import About from '@/components/About';
import Header from '@/components/_Header';
import Footer from '@/components/_Footer';

export default {
  name: 'App',
  components: {
    mdbContainer,
    mdbCol,
    mdbRow,
    About,
    Header,
    Footer,
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
  /* margin-top: 60px; */
}
</style>
