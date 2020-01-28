<template>
  <DashBoardSideBar/>
</template>

<script>
import DashBoardSideBar from '../molecules/DashBoardSideBar.vue'

export default {
  name: "DashBoard",
  components: {
    DashBoardSideBar
  },
  data() {
    return {
      showPassword : false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
