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
        <VuetifyButton
          :class="'success'"
          :largeOption="true"
          :msg="'Search!'"
          :clickEvent="startSearch"
        >
          <template>
            <VuetifyIcon :icon="'mdi-database-search'"/>
          </template>
        </VuetifyButton>
      </v-card-actions>
    </v-card-text>
  </v-card>
</template>

<script>
import VuetifyIcon from '@/components/atoms/VuetifyIcon.vue'
import VuetifyButton from '@/components/atoms/VuetifyButton.vue'

export default {
  name: 'CardMovieSearch',
  components: {
    VuetifyButton,
    VuetifyIcon
  },
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
    },
    startSearch() {
      this.$emit('searchEvent', true)
    }
  }
}
</script>
