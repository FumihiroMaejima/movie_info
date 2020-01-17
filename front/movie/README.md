# movie

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# 環境構築

## envファイルの設定

「.env.local-example」をリネームして環境ごとの環境変数を設定する

```
.env.local
.env.development
.env.prod

# .env.local
NODE_ENV='local'
VUE_APP_API_BASE_URL='http://localhost:8080/api/v1/xxx'

# .env.development
# NODE_ENV='development'
# VUE_APP_API_BASE_URL='https://development/api/v1/xxx'

# .env.prod
# NODE_ENV='production'
# VUE_APP_API_BASE_URL='https://production/api/v1/xxx'
```

## アセットディレクトリの作成

movie/src/assets/下に
「css」、「img」、「js」ディレクトリ作成

## ライブラリの追加

下記のライブラリを追加

```
$ yarn add vue-router
$ yarn add vuex
$ yarn add axios
$ yarn add axios-mock-server
$ yarn add vuetify
$ yarn add material-design-icons-iconfont
$ yarn add @vue/test-utils
$ yarn add --dev prettier
$ yarn add --dev stylelint

下記の様にコマンド実行する
$ docker exec -it pymovie_nginx /bin/sh -c "cd /var/www && yarn add vue-router"
```

## ライブラリの設定

package.jsonの編集

```
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint",
    "lint:css": "stylelint src/**/*.css",
    "fmt": "prettier --write \"src/**/*.js\"",
    "mock:build": "axios-mock-server -b",
    "mock:watch": "axios-mock-server -w"
  },
```

movie/.eslintrc.jsの作成と編集

```
module.exports = {
    root: true,
    env: {
        node: true
    },
    'extends': [
        'plugin:vue/essential',
        'eslint:recommended'
    ],
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
    },
    parserOptions: {
        parser: 'babel-eslint'
    }
}
```

movie/.stylelintrcの作成と編集

```
{
  "rules": {
    "color-hex-length": "short",
    "color-no-invalid-hex": true,
    "custom-property-no-outside-root": true,
    "indentation": 2,
    "length-zero-no-unit": true,
    "media-feature-name-no-vendor-prefix": true,
    "number-leading-zero": "never",
    "selector-root-no-composition": true,
    "string-quotes": "single"
  }
}
```

## Componentsディレクトリの設定(Atomic Designs)

movie/src/Components下に下記のディレクトリを作成する
Atomic Designs

```
Atoms
Molecules
Organisms
Templates
Pages
```

## vue-routerの設定

movie/src/router.jsの作成と編集

```
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import TestPage from './components/Pages/TestPage.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: HelloWorld
        },
        {
            path: '/test',
            name: 'test',
            component: TestPage
        },
    ]
})

```

## vuexの設定

movie/src/store.jsの作成と編集

関連するモジュールも作成しておくこと

```
import Vue from 'vue'
import Vuex from 'vuex'
import testModule from './store/modules/testModule'
import testSubModule from './store/modules/testSubModule'

Vue.use(Vuex)

const store = new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    modules: {
        subModule1: testSubModule,
        subModule2: testSubModule,
        testModule
    },
    state: {

    },
    mutations: {

    },
    actions: {

    }
})
/* eslint-disable no-console */
store.dispatch('testModule/testAction', ['subModule1', 'subModule2'])

export default store
```


movie/src/store/modulesディレクトリの作成

```
mkdir /src/store/modules
```

movie/src/store/modules/testModule.jsの作成と編集

movie/src/store/modules/testSubModule.jsも作成する

コードは省略


## モジュールを利用するコンポーネントの作成

「/test」にアクセスした時に利用するコンポーネント

movie/src/components/Pages/TestPage.vueの作成と編集

```
<template>
    <div>
        <TestSubModuleComponent module="subModule1"/>
        <TestSubModuleComponent module="subModule2"/>
        <TestModuleComponent/>
    </div>
</template>

<script>
import TestSubModuleComponent from './TestSubModuleComponent.vue'
import TestModuleComponent from './TestModuleComponent.vue'

export default {
    name: 'app',
    components: {
        TestSubModuleComponent,
        TestModuleComponent,
    }
}
```

testModuleモジュールはTestModuleComponentコンポーネントで利用する

testSubModuleモジュールはTestSubModuleComponentコンポーネントで利用する

TestSubModuleComponentコンポーネントはそれぞれ別名をつけて2つのコンポーネントとして利用する



## main.jsの設定

main.jsの編集

```
import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app')
```

## App.vueの設定

App.vueの編集

```
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>
```


## vuetifのインストール

vuetifのインストール

```
$ docker exec -it pymovie_nginx /bin/sh -c "cd /var/www/ && vue add vuetify"
```

