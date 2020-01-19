<template>
  <v-app>
    <v-content>
      <!--
      <DashBoardSideBar/>
      <DashBoardNavBar/>
      <DashBoardFooter/>
    </v-content>
    -->

    <v-navigation-drawer app v-model="drawer" clipped>Navigation Lists</v-navigation-drawer>
    <v-app-bar color="primary" dark app clipped-left>
      <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Vuetify</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text>For Enterprise</v-btn>
        <v-menu offset-y>
          <template v-slot:activator="{on}">
            <v-btn v-on="on" text>Support<v-icon>mdi-menu-down</v-icon></v-btn>
          </template>
          <v-list>
            <v-subheader>Get help</v-subheader>
            <v-list-item v-for="support in supports" :key="support.name">
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
    <v-footer color="primary" dark app>
      Vuetify
    </v-footer>
  </v-app>
</template>

<script>
//import DashBoardFooter from '../Molecules/DashBoardFooter.vue'
//import DashBoardNavBar from '../Molecules/DashBoardNavBar.vue'
//import DashBoardSideBar from '../Molecules/DashBoardSideBar.vue'
// import DashBoard from '../Organisms/DashBoard.vue'

export default {
  name: 'DashBoardPage',
  /*
  components: {
    DashBoardFooter,
    DashBoardNavBar,
    DashBoardSideBar
  }
  */
  data(){
    return{
        drawer: null,
        supports:[
          {name: 'Consulting and suppourt',icon: 'vuetify'},
          {name: 'Discord community',icon: 'discord'},
          {name: 'Report a bug',icon: 'bug'},
          {name: 'Github issue board',icon: 'github-face'},
          {name: 'Stack overview',icon: 'mdi-stack-overflow'},
        ]
    }
  }
}
</script>
