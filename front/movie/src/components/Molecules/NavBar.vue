<template>
  <v-app-bar dark app clipped-left>
    <HumburgerMenu/>
    <v-toolbar-title>Vuetify</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn text>For Enterprise</v-btn>
      <v-menu offset-y>
        <template v-slot:activator="{on}">
          <v-btn v-on="on" text>Support<v-icon>mdi-menu-down</v-icon></v-btn>
        </template>
        <v-list>
          <v-subheader>Get helpInfo</v-subheader>

          <v-list-item v-for="support in supports" :key="support.name" :to="support.link">
            <v-list-item-content>
              <v-list-item-title>{{ support.icon }}</v-list-item-title>
            </v-list-item-content>
            <v-list-item-content>
              <v-list-item-title>{{ support.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script>
import HumburgerMenu from '../atoms/HumburgerMenu.vue'

export default {
  name: "NavBar",
  components: {
    HumburgerMenu
  },
  data(){
    return{
      drawer: null,
      supports:[
        {
          name: 'Consulting and suppourt',
          icon: 'mdi-vuetify',
          link: '/consulting-and-support'
        },
        {
          name: 'Discord community',
          icon: 'mdi-discord',
          link: '/discord-community'},
        {
          name: 'Report a bug',
          icon: 'mdi-bug',
          link: '/report-a-bug'
        },
        {
          name: 'Github issue board',
          icon: 'mdi-github-face',
          link: '/guthub-issue-board'
        },
        {
          name: 'Stack overview',
          icon: 'mdi-stack-overflow',
          link: '/stack-overview'
        },
      ],
    }
  }
}
</script>
