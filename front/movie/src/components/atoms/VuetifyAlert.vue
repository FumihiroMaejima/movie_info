<template>
  <v-alert :type="alertType">
    {{ message }}
  </v-alert>
</template>

<script>
export default {
  name: "VuetifyAlert",
  props: {
    alertType: {
      type : String,
      default: 'error'
    },
    message: {
      type : String,
      default: 'this is alert!'
    }
  },
  data(){
    return{
    }
  }
}
</script>
