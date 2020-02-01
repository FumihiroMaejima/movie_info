<template>
  <header>
    <v-navigation-drawer app v-model="open" clipped>
      <v-container>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title grey--text text--darken-2">
              Side Bar
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>

        <v-list nav dense>
          <v-list-group
            v-for="navList in navLists"
            :key="navList.name"
            :prepend-icon="navList.icon"
            no-action
            :append-icon="navList.lists ? undefined : ''"
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>{{ navList.name }}</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item v-for="list in navList.lists" :key="list.name" :to="list.link">
              <v-list-item-content>
                <v-list-item-title>{{ list.name }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </v-list>

      </v-container>
    </v-navigation-drawer>

    <v-app-bar dark app clipped-left>
      <v-app-bar-nav-icon @click="open=!open"></v-app-bar-nav-icon>
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
              <v-icon color="teal darken-2">{{ support.icon }}</v-icon>
              <v-list-item-content>
                <v-list-item-title>{{ support.name }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar-items>
    </v-app-bar>
  </header>
</template>

<script>
import cnf from '@/config/global.json'

export default {
  name: "GlobalHeader",
  data(){
    return{
      open: false,
      supports: cnf.supports,
      navLists: cnf.navLists
    }
  }
}
</script>
