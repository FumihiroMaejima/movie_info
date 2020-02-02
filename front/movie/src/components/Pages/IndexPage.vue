<template>
  <v-container>
    <v-layout text-center wrap>
      <v-flex mb-5 xs12>
        <v-card class="mx-auto text-center" color="gray" dark outlined>
          <v-card-title class="text-right">
            <div class="display-1 font-weight-thick">Movie Search!</div>
          </v-card-title>
          <v-card-text>
            <div class="display-1 font-weight-thick">Movie Info Search Servise</div>
            <v-row>
              <v-col cols="12">
                <v-combobox
                  v-model="select"
                  :items="items"
                  label="Input Movie Name"
                  outlined
                  dense
                  small-chips
                />
              </v-col>
            </v-row>
            <v-card-actions>
              <v-spacer/>
              <v-btn class="success" text large>
                Search!<v-icon dark right>mdi-database-search</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-flex>

      <v-flex xs12>
        <v-card class="mx-auto" max-width="400">
          <v-img
            :class="movieInfo.image.class"
            :height="movieInfo.image.height"
            :src="movieInfo.image.src"
          >
            <v-card-title>{{ movieInfo.title }}</v-card-title>
          </v-img>

          <v-card-subtitle :class="movieInfo.subTitle.class">{{ movieInfo.subTitle.text }}</v-card-subtitle>

          <v-card-text :class="movieInfo.cardText.class">
            <div>{{ movieInfo.cardText.text1 }}</div>
            <div>{{ movieInfo.cardText.text2 }}</div>
          </v-card-text>

          <v-card-actions>
            <v-btn :color="movieInfo.cardAction.btnColor1" text>{{ movieInfo.cardAction.btnText1 }}</v-btn>
            <v-btn :color="movieInfo.cardAction.btnColor2" text>{{ movieInfo.cardAction.btnText2 }}</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>

      <v-flex xs12>

      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
// import Login from '@/components/organisms/Login.vue'
// IndexPage
import def from '@/config/default.json'

export default {
  name: 'IndexPage',
  components: {
      //Login
  },
  data () {
    return {
      /*
        seorce
        https://vuetifyjs.com/en/components/cards
        https://vuetifyjs.com/en/components/combobox
      */
      select: def.searchListItem.select,
      items: def.searchListItem.items,
      movieInfo: def.searchMovieInfo
    }
  }
}
</script>
