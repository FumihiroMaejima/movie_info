<template>
  <v-btn text @click="clickEvent">{{ msg }}</v-btn>
</template>

<script>
export default {
  name: "VuetifyButton",
  props: {
    msg: {
      type: String,
      required: true,
      default: ''
    },
    clickEvent: {
      type: Function,
      required: false,
      default: () => {}
    },
  },
  data(){
    return{
    }
  }
}
</script>
