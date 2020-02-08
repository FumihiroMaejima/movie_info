<template>
  <v-layout text-center wrap>
    <v-flex mb-5 xs12>
      <CardMovieSearch
       :selectData="select"
       :itemsData="items"
      />
    </v-flex>

    <v-flex xs12>
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
      select: def.searchListItem.select,
      items: def.searchListItem.items,
      movieInfo: def.searchMovieInfo
    }
  }
}
</script>
