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

        <v-list nav dense>
          <v-list-group
            v-for="nav_list in nav_lists"
            :key="nav_list.name"
            :prepend-icon="nav_list.icon"
            no-action
            :append-icon="nav_list.lists ? undefined : ''"
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>{{ nav_list.name }}</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item v-for="list in nav_list.lists" :key="list.name" :to="list.link">
              <v-list-item-content>
                <v-list-item-title>{{ list }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
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

    <About/>
    <v-row>
      <v-col cols="12" sm="6" md="4" lg="3">
        <Graph/>
      </v-col>
      <v-col cols="12" sm="6" md="4" lg="3">
        <Graph/>
      </v-col>
      <v-col cols="12" sm="6" md="4" lg="3">
        <Graph/>
      </v-col>
      <v-col cols="12" sm="6" md="4" lg="3">
        <Graph/>
      </v-col>
    </v-row>

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
import Graph from '../Molecules/Graph.vue'
import About from './About.vue'

export default {
  name: 'DashBoardPage',
  components: {
    Graph,
    About
    // DashBoardFooter,
    // DashBoardNavBar,
    // DashBoardSideBar
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
        nav_lists: [
          {
            name: 'Getting Started',
            icon: 'mdi-speedometer',
            lists:['Quick Start','Pre-made layouts']
          },
          {
            name: 'Customization',
            icon: 'mdi-cogs'
          },
          {
            name: 'Styles & animations',
            icon: 'mdi-palette',
            lists:['Colors','Content','Display']
          },
          {
            name: 'UI Components',
            icon: 'mdi-view-dashboard',
            lists:['API explorer','Alerts']
          },
          {
            name: 'Directives',
            icon: 'mdi-function'
          },
          {
            name: 'Preminum themes',
            icon: 'mdi-vuetify'
          },
        ]
    }
  }
}
</script>
