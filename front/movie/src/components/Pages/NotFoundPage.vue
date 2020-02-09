<template>
  <v-container>
    <v-layout text-center wrap>
      <v-flex mb-5 xs12>
        <v-card>
          <v-toolbar color="pink" dark dense flat>
            <v-toolbar-title class="body-2">Error Info</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <div  class="display-3 font-weight-thick">404 Not Found!</div>
            <br>
            <div  class="font-weight-light">Request page is not exist.</div>
          </v-card-text>
          <v-card-actions>
            <v-spacer/>
            <v-btn class="success" text large href="/">
              Home
              <VuetifyIcon :icon="'mdi-home'"/>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import VuetifyIcon from '@/components/atoms/VuetifyIcon.vue'

export default {
  name: 'NotFoundPage',
  components: {
    VuetifyIcon
  },
  data () {
    return {
    }
  }
}
</script>
