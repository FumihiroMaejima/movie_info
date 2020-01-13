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
