<template>
  <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
</template>

<script>
export default {
  name: "HumburgerMenu",
  data(){
    return{
        drawer: null
    }
  }
}
</script>
