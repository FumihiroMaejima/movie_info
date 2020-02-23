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
      titles: [],
      movieInfo: def.searchMovieInfo
    }
  },
  computed: {
    getTitlesList: {
      get() {
        return this.$store.getters['index/titles']
      },
      set(SetTitlesList) {
        this.$store.dispatch('index/getTitlesDataAction', SetTitlesList)
      }
    },
    getSelectData: {
      get() {
        return this.$store.getters['index/searchData']
      },
      set(SetSelectData) {
        this.checkDisabledData(SetSelectData)
        this.$store.dispatch('index/getSearchDataAction', SetSelectData)
      }
    }
  },
  created: function() {
    /* get movie titles */
    this.$client
    .get('movies/titles')
    .then(response => {
      // this.titles = response.data.data
      this.$store.dispatch('index/getTitlesDataAction', response.data.data)
    })
    .catch(error => {
      this.errorFlag = true
      this.errorMessage = 'created: ' + error.name + ': ' +error.message
    })
  },
  methods: {
    SetTitlesList() {
      return this.$store.getters['index/titles']
    },
    SetSelectData() {
      return this.$store.getters['index/searchData']
    },
    checkDisabledData(inputData) {
      return this.noInputFlag = (inputData === null) ? true : false
    },
    showMovieInfo(eventFlag){
      this.$client
      .get('movies/search', {
        params : {
          'title' : this.$store.getters['index/searchData']
        }
      })
      .then(response => {
        const responseData = response.data
        const execution = responseData.execution
        const moviesData = responseData.data.results
        /* eslint-disable no-console */
        console.log(response)
        console.log(responseData)

        if(!execution || !moviesData.length) {
          this.errorFlag = true
          this.noInputFlag = true
          this.searchFlag = false
          if(!execution) {
            /* バリデーションエラーの場合 */
            return this.errorMessage = responseData.message
          }
          else {
            /* 検索数が0の場合 */
            return this.errorMessage = 'search result is 0. please try again.'
          }

        }
        else {
          this.errorFlag = false
          this.noInputFlag = false
          this.searchFlag = eventFlag
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
