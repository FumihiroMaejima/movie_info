<template>
  <v-card class="mx-auto text-center" color="gray" dark outlined>
    <v-card-title class="text-right">
      <div class="display-1 font-weight-thick">Movie Search!</div>
    </v-card-title>
    <v-card-text>
      <div class="display-1 font-weight-thick">Movie Info Search Servise</div>
      <v-row>
        <v-col cols="12">
          <v-combobox
            v-model="getSelectData"
            :items="itemsData"
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
</template>

<script>

export default {
  name: 'CardMovieSearch',
  /*
  components: {
  }
  */
  props: {
    selectData: {
      type: Object,
      required: false
    },
    itemsData: {
      type: Array,
      required: false
    }
  },
  data () {
    return {
    }
  },
  computed: {
    getSelectData: {
      get() {
        return this.selectData
      },
      set(SetSelectData) {
        return SetSelectData
      }
    }
  },
  methods: {
    SetSelectData() {
      return this.selectData
    }
  }
}
</script>
