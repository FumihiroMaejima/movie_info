<template>
  <v-layout text-center wrap>
    <v-flex mb-5 xs12>
      <CardMovieSearch
       :selectData="select"
       :itemsData="items"
       @searchEvent="showMovieInfo($event)"
      />
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
      select: def.searchListItem.select,
      items: def.searchListItem.items,
      movieInfo: def.searchMovieInfo
    }
  },
  methods: {
    showMovieInfo(value){
      this.searchFlag = value

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
