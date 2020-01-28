<template>
  <div>
    <Login/>
  </div>
</template>

<script>
//import TestSubModuleComponent from './TestSubModuleComponent.vue'
//import TestModuleComponent from './TestModuleComponent.vue'
import Login from '../organisms/Login.vue'
//import DashBoardFooter from '../Molecules/DashBoardFooter.vue'

export default {
    name: 'app',
    components: {
        //TestSubModuleComponent,
        //TestModuleComponent
        Login
    },
    data() {
        return {
            showPassword : false
        }
    }
}
</script>
