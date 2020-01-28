<template>
  <v-app-bar-nav-icon @click="clickHumberburgerMenu"></v-app-bar-nav-icon>
</template>

<script>
export default {
  name: "HumburgerMenu",
  data(){
    return{
        openMenu: false
    }
  },
  methods: {
    clickHumberburgerMenu() {
      this.openMenu = !this.openMenu
      this.$emit('clickHumbergerMenuEvent', this.openMenu)
    }
  }
}
</script>
