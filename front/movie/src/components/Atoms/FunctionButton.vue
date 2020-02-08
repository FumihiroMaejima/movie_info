<template>
  <v-btn
    :class="classData"
    text
    :large="largeOption"
    :disabled="checkDisabled"
    @click="clickEvent"
  >
    {{ msg }}
    <slot/>
  </v-btn>
</template>

<script>
export default {
  name: "FunctionButton",
  props: {
    classData: {
      type: String,
      required: false,
      default: ''
    },
    largeOption: {
      type: Boolean,
      required: false,
      default: false
    },
    checkDisabled: {
      type: Boolean,
      required: false,
      default: false
    },
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
