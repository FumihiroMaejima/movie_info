<template>
  <v-card class="mx-auto text-center" color="gray" dark outlined>
    <v-card-title class="text-right">
      <div class="display-1 font-weight-thick">Movie Search!</div>
    </v-card-title>
    <v-card-text>
      <div class="display-1 font-weight-thick">Movie Info Search Servise</div>
      <v-row>
        <v-col cols="12">
          <!-- combobox -->
          <slot/>
        </v-col>
      </v-row>
      <v-card-actions>
        <v-spacer/>
        <FunctionButton
          :class="'success'"
          :largeOption="true"
          :msg="'Search!'"
          :checkDisabled="disabledFlag"
          :clickEvent="startSearch"
        >
          <template>
            <VuetifyIcon :icon="'mdi-database-search'"/>
          </template>
        </FunctionButton>
      </v-card-actions>
    </v-card-text>
  </v-card>
</template>

<script>
import VuetifyIcon from '@/components/atoms/VuetifyIcon.vue'
import FunctionButton from '@/components/atoms/FunctionButton.vue'

export default {
  name: 'CardMovieSearch',
  components: {
    FunctionButton,
    VuetifyIcon
  },
  props: {
    disabledFlag: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
    }
  },
  methods: {
    startSearch() {
      // return search event to parent.
      this.$emit('searchEvent', true)
    }
  }
}
</script>
