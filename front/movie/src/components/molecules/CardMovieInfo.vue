<template>
  <v-card class="mx-auto" max-width="400">
    <v-img
      :class="movieData.image.class"
      :height="movieData.image.height"
      :src="movieData.image.src"
    >
      <v-card-title>{{ movieData.title }}</v-card-title>
    </v-img>

    <v-card-subtitle :class="movieData.subTitle.class">{{ movieData.subTitle.text }}</v-card-subtitle>

    <v-card-text :class="movieData.cardText.class">
      <div>{{ movieData.cardText.text1 }}</div>
      <div>{{ movieData.cardText.text2 }}</div>
    </v-card-text>

    <v-card-actions>
      <v-btn :color="movieData.cardAction.btnColor1" text>{{ movieData.cardAction.btnText1 }}</v-btn>
      <v-btn :color="movieData.cardAction.btnColor2" text>{{ movieData.cardAction.btnText2 }}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

export default {
  name: 'CardMovieInfo',
  /*
  components: {
  }
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
  }
}
</script>
