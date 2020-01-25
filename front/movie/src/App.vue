<template>

  <v-app>
    <DashBoardSideBar/>

    <DashBoardNavBar/>

    <v-content>
      <router-view/>
      <Graph/>
    </v-content>

    <DashBoardFooter/>
  </v-app>

  <!--
  <router-view/>
  -->
</template>

<script>
import DashBoardFooter from './components/Molecules/DashBoardFooter.vue'
import DashBoardNavBar from './components/Molecules/DashBoardNavBar.vue'
import DashBoardSideBar from './components/Molecules/DashBoardSideBar.vue'
import Graph from './components/Molecules/Graph.vue'

export default {
  name: 'App',
  components: {
    Graph,
    // About,
    DashBoardFooter,
    DashBoardNavBar,
    DashBoardSideBar
  },
  data: () => ({
    //
  }),
};
</script>
