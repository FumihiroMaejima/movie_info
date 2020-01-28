<template>

  <v-app>
    <SideBar/>

    <NavBar/>

    <v-content>
      <router-view/>
      <Graph/>
    </v-content>

    <Footer/>
  </v-app>

  <!--
  <router-view/>
  -->
</template>

<script>
import Footer from './components/molecules/Footer.vue'
import NavBar from './components/molecules/NavBar.vue'
import SideBar from './components/molecules/SideBar.vue'
import Graph from './components/molecules/Graph.vue'

export default {
  name: 'App',
  components: {
    Graph,
    // About,
    Footer,
    NavBar,
    SideBar
  },
  data: () => ({
    //
  }),
};
</script>
