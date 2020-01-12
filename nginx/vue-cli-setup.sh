#!/bin/sh

# nodejs,npmのインストール
installNode() {
    apt install -y nodejs npm
}

# wgetのインストール
installWget() {
    apt install -y wget
}

# nのインストール
installN() {
    npm install n -g
}

# nのバージョン設定
# パラメーター:stable,latest
setNVersion() {
    n $1
}

# node,npmのパージ
purgeNodeNpm() {
    apt purge -y nodejs npm
}

# yarnのインストール
installYarn() {
    npm install -g yarn
}

# vue-cliのインストール
addVueCli() {
    yarn global add @vue/cli
}

# バージョン切り替え失敗後の再試行時のみコメントアウトを外して使用
#installNode

# 関数呼び出し
installWget
installN

### nのバージョンの指定
N_VERSION="stable"

setNVersion ${N_VERSION}

purgeNodeNpm
installYarn
addVueCli
