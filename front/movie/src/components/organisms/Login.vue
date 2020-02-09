<template>
  <v-card class="mx-auto mt-5" width="400px">
    <v-card-title>
      <h1 class="display-1">ログイン</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field prepend-icon="mdi-account-circle" label="ユーザ名" />
        <v-text-field
          v-bind:type="showPassword ? 'text' : 'password'"
          v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          prepend-icon="mdi-lock"
          @click:append="showPassword = !showPassword"
          label="パスワード"
        />
        <v-card-actions>
          <v-btn class="info">ログイン</v-btn>
          <!-- <v-btn class="secondary">ログイン</v-btn> -->
        </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
    name: "Login",
    data() {
        return {
            showPassword : false
        }
    },
    computed: {
        count() {
            /* eslint-disable no-console */
            return this.$store.getters['testModule/count']}
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
