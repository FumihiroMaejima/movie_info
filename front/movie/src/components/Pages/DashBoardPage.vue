<template>
  <v-app>
    <v-content>
      <!--
      <DashBoardSideBar/>
      <DashBoardNavBar/>
      <DashBoardFooter/>
    </v-content>
    -->

    <v-navigation-drawer app v-model="drawer" clipped>
      <v-container>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title grey--text text--darken-2">
              Navigation Lists+++
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>

        <v-list dense nav>
          <v-list-item v-for="nav_list in nav_lists" :key="nav_list.name">
            <v-list-item-icon>
              <v-icon>{{ nav_list.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ nav_list.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

      </v-container>
    </v-navigation-drawer>

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
            <v-subheader>Get helpInfo</v-subheader>
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
        ],
        nav_lists:[
          {name: 'Getting Started',icon: 'mdi-vuetify'},
          {name: 'Customization',icon: 'mdi-cogs'},
          {name: 'Styles & animations',icon: 'mdi-palette'},
          {name: 'UI Components',icon: 'mdi-view-dashboard'},
          {name: 'Directives',icon: 'mdi-function'},
          {name: 'Preminum themes',icon: 'mdi-vuetify'},
        ]
    }
  }
}
</script>
