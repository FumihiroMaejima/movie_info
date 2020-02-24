<template>
  <v-card class="mx-auto" max-width="400" hover style="margin: 0, 0, 5px, 0">
    <v-img
      v-if="movieData.poster_path !== null"
      class="white--text align-end"
      height="200px"
      :src="'https://image.tmdb.org/t/p/original'+movieData.poster_path"
    >
      <v-card-title>{{ movieData.title }}</v-card-title>
    </v-img>
    <v-img
      v-else
      class="white--text align-end"
      height="200px"
      src="./../../assets/img/camera.png"
      alt="イメージポスター画像"
    >
      <v-card-title>{{ movieData.title }} (No Image)</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Release: {{ movieData.release_date }}</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Original Title: {{ movieData.original_title }}</div>
      <div>{{ movieData.overview }}</div>
    </v-card-text>

    <v-card-actions>
      <v-btn color="orange" text @click="checkDetail(movieData.id)">detail</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

export default {
  name: 'CardMovieInfo',
  /*
  components: {
  },
  */
  props: {
    movieData: {
      type: Object,
      required: false
    }
  },
  data () {
    return {
    }
  },
  methods: {
    checkDetail(value) {
      this.$emit('checkDetailEvent', value)
    },
  }
}
</script>
