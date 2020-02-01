<template>

  <v-app>
    <GlobalHeader/>

    <v-content>
      <router-view/>
      <Graph/>
    </v-content>

    <GlobalFooter/>
  </v-app>

  <!--
  <router-view/>
  -->
</template>

<script>
import GlobalFooter from '@/components/_global/GlobalFooter.vue'
import GlobalHeader from '@/components/_global/GlobalHeader.vue'
import Graph from '@/components/molecules/Graph.vue'

export default {
  name: 'App',
  components: {
    GlobalFooter,
    GlobalHeader,
    Graph
  },
  data: () => ({
  })
};
</script>
