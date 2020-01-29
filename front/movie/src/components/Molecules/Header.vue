<template>
  <header>
    <SideBar :open="clickHumbergerMenu"/>
    <NavBar @relayClickHunbergerMenuEvent="getClickHunbergerMenuEvent($event)"/>
  </header>
</template>

<script>
import NavBar from '@/components/molecules/NavBar.vue'
import SideBar from '@/components/molecules/SideBar.vue'

export default {
  name: "Header",
  components: {
    NavBar,
    SideBar
  },
  data: () => ({
    clickHumbergerMenu: false
  }),
  methods: {
    getClickHunbergerMenuEvent(getValue) {
      this.clickHumbergerMenu = getValue
    }
  }
}
</script>
