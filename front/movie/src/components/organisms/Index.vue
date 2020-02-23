<template>
  <v-layout text-center wrap>
    <v-flex mb-5 xs12>
      <CardMovieSearch
      :disabledFlag="noInputFlag"
       @searchEvent="showMovieInfo($event)"
      >
        <template>
          <v-combobox
            v-model="getSelectData"
            :items="items"
            label="Input Movie Name"
            outlined
            dense
            small-chips
          />
        </template>
      </CardMovieSearch>
    </v-flex>

    <v-flex xs12 v-if="searchFlag">
      <CardMovieInfo
        :movieData="movieInfo"
      />
    </v-flex>
  </v-layout>
</template>

<script>
import CardMovieInfo from '@/components/molecules/CardMovieInfo.vue'
import CardMovieSearch from '@/components/molecules/CardMovieSearch.vue'
import def from '@/config/default.json'

export default {
  name: 'Index',
  components: {
      CardMovieInfo,
      CardMovieSearch
  },
  data () {
    return {
      /*
        source
        https://vuetifyjs.com/en/components/cards
        https://vuetifyjs.com/en/components/combobox
      */
      searchFlag: false,
      noInputFlag: true,
      select: def.searchListItem.select,
      items: def.searchListItem.items,
      movieInfo: def.searchMovieInfo
    }
  },
  computed: {
    getSelectData: {
      get() {
        return this.$store.getters['index/searchData']
      },
      set(SetSelectData) {
        this.checkDisabledData(SetSelectData)

        console.log('SetSelectData: ' + SetSelectData)

        this.$store.dispatch('index/getSearchDataAction', SetSelectData)
        console.log('getSelectData: ' + this.$store.getters['index/searchData'])
      }
    }
  },
  methods: {
    SetSelectData() {
      return this.$store.getters['index/searchData']
    },
    checkDisabledData(inputData) {
      return this.noInputFlag = (inputData === null) ? true : false
    },
    showMovieInfo(eventFlag){
      this.searchFlag = eventFlag

      /* eslint-disable no-console */
      this.$client
      .get('movies/search', {
        params : {
          'title' : 'Hello'
        }
      })
      .then(response => {
        console.log(response)
        console.log(response.data)
      })
      .catch(error => {
        /* eslint-disable no-console */
        console.log('error name: ' + error.name)
        console.log('error message: ' + error.message)
        this.searchFlag = false
      })
    }
  }
}
</script>
