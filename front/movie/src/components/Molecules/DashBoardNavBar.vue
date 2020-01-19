<template>
  <v-app-bar dark app>
    <HumburgerMenu/>
    <v-toolbar-title>Vuetify</v-toolbar-title>
  </v-app-bar>
</template>

<script>
import HumburgerMenu from '../Atoms/HumburgerMenu.vue'

export default {
  name: "DashBoardNavBar",
  components: {
    HumburgerMenu
  },
  data(){
    return{
        drawer: null
    }
  }
}
</script>
