<template>
  <v-footer dark app>{{ title }}</v-footer>
</template>

<script>
import cnf from '@/config/global.json'

export default {
  name: "GlobalFooter",
  data(){
    return{
      title: cnf.footerMessage.title
    }
  }
}
</script>
