<template>
  <div>
    <span>total {{ count }}</span>
  </div>
</template>

<script>
export default {
    name: "TestModuleComponent",
    computed: {
        count() {
            /* eslint-disable no-console */
            return this.$store.getters['testModule/count']}
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
