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
      console.log("check"+this.openMenu)
      this.$emit('clickHumbergerMenuEvent', this.openMenu)
      //this.openMenu = false
      //this.openMenu = this.openMenu === true ? false : this.openMenu
    }
  }
}
</script>
