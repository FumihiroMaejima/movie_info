<template>
    <div>
        <button @click="testAction">increment {{ step }}</button>
        <span>total {{ count }}</span>
        <br>
        <span>{{ msg }}</span>
    </div>
</template>

<script>
export default {
    name: 'TestSubModuleComponent',
    props: {
        module: {
            type: String,
            required: false,
        }
    },
    computed: {
        step() {return this.$store.getters[`${this.module}/step`]},
        count() {return this.$store.getters[`${this.module}/count`]},
        msg() {return this.$store.getters[`${this.module}/msg`]}
    },
    methods: {
        testAction() {
            this.$store.dispatch(`${this.module}/testAction`)
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
