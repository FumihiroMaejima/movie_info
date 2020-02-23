<template>
  <v-layout text-center wrap>
    <v-flex xs12 v-if="errorFlag">
      <VuetifyAlert
        :alertType="'error'"
        :message="errorMessage"
      />
    </v-flex>

    <v-flex mb-5 xs12>
      <CardMovieSearch
        :disabledFlag="noInputFlag"
        @searchEvent="showMovieInfo($event)"
      >
        <template>
          <v-combobox
            v-model="getSelectData"
            :items="titles"
            label="Input Movie Title"
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
import VuetifyAlert from '@/components/atoms/VuetifyAlert.vue'
import CardMovieInfo from '@/components/molecules/CardMovieInfo.vue'
import CardMovieSearch from '@/components/molecules/CardMovieSearch.vue'
import def from '@/config/default.json'

export default {
  name: 'Index',
  components: {
    VuetifyAlert,
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
      errorFlag: false,
      errorMessage: '',
      searchFlag: false,
      noInputFlag: true,
      select: def.searchListItem.select,
      titles: [],
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

        /* eslint-disable no-console */
        console.log('SetSelectData: ' + SetSelectData)

        this.$store.dispatch('index/getSearchDataAction', SetSelectData)

        /* eslint-disable no-console */
        console.log('getSelectData: ' + this.$store.getters['index/searchData'])
      }
    }
  },
  created: function() {
    /* get movie titles */
    this.$client
    .get('movies/titles')
    .then(response => {
      this.titles = response.data.data
    })
    .catch(error => {
      this.errorFlag = true
      this.errorMessage = 'created: ' + error.name + ': ' +error.message
    })
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

      this.$client
      .get('movies/search', {
        params : {
          'title' : this.$store.getters['index/searchData']
        }
      })
      .then(response => {
        /* eslint-disable no-console */
        console.log(response)
        console.log(response.data)

        this.errorFlag = !response.data.execution ? true : false
        this.noInputFlag = !response.data.execution ? true : false
        this.searchFlag = !response.data.execution ? false : true

        if(!response.data.execution) {
          return this.errorMessage = response.data.message
        }

      })
      .catch(error => {
        this.errorFlag = true
        this.searchFlag = false
        this.noInputFlag = true
        this.errorMessage = 'get Movie Info : ' + error.name + ': ' +error.message
      })
    }
  }
}
</script>
