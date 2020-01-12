#!/bin/sh

# npmとnodeのバージョンアップ
changeNpmVersion() {
   sh ./change-npm-version.sh
}

# yarnのインストール
installYarn() {
    npm install -g yarn
}

# vue-cliのインストール
addVueCli() {
    yarn global add @vue/cli
}

# 関数呼び出し

## npmとnodeのバージョンアップをバックグラウンドで実行(&付与)
changeNpmVersion &

## バックグラウンド処理終了まで待機
wait

installYarn
addVueCli
