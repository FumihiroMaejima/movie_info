# Sample Site by Django

### 構成

-Python:3.7

-MySQL:８

-Nginx:1.17.7


## 開発環境構築


### 不要ファイルの削除

＊コンテナイメージの作り直し時も同様

```shell-session
$ docker-compose down --rmi all
$ unllink app/src/movie
$ rm -rf app/src/node_modules
$ rm -rf app/src/pymovie
$ rm -rf app/src/manage.py
$ rm -rf app/static/*
$ rm -rf mysql/mysql_data
```

### Django環境のコンテナビルド

docker-composeコマンドでstartprojectの実行

```shell-session
$ docker-compose run uwsgi django-admin.py startproject pymovie .
```

下記の事項をそれぞれsettings.pyの所定の箇所に記載する

```Python
import pymysql
pymysql.install_as_MySQLdb()
```

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'user_pass',
        'HOST': 'db_port',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
    }
}
```

```Python
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
```

```Python
STATIC_ROOT = '/var/www/static'
```

```Python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}
```

各種config設定も追記しておく

```Python
CONFIG_VARIABLE = os.getenv("CONFIG_VARIABLE", "default")
```

マイグレーションの実行

```shell-session
$ docker-compose run uwsgi ./manage.py makemigrations
$ docker-compose run uwsgi ./manage.py migrate
```

管理画面作成

管理者名、メールアドレス、パスワードを作成する

```shell-session
$ docker-compose run uwsgi ./manage.py createsuperuser
```

admin側のCSS設定

「STATIC_ROOT」の記述をした状態で下記を実行する

```shell-session
$ docker-compose run uwsgi ./manage.py collectstatic
```

コンテナの全体的な起動

```shell-session
$ docker-compose up -d
```

ブラウザで確認

```
http://localhost
```

## フロントエンド環境の構築

nodeとnpmのバージョンの切り替えとyarnとvue-cliのインストール(バッチの実行)

```
$ docker exec -it pymovie_nginx /bin/sh -c "cd /usr/local/src && ./vue-cli-setup.sh"
```

その他のフロントエンドの手順は[フロントエンド専用のREADME](./front/movie/README.md)を参照

## movieアプリケーションの新規作成

イメージの作り直し等による既存アプリケーションの作成は[下記](##既存movieアプリケーションの作成)へ

```shell-session
$ docker-compose run uwsgi ./manage.py startapp your_app
```
pymovie/settings.pyの「INSTALLED_APPS」に作成したアプリケーション名を追記すること。

```Python
INSTALLED_APPS = {
...
    'your_app.apps.Your_AppConfig',
...
}
...
TEMPLATES = [
    {
    ...
        'DIRS': (os.path.join(BASE_DIR, 'templates'),),
    ...
    }
]
```

movie/urls.pyの作成

```
touch app/src/movie/urls.py
```

下記の通り編集

```Python
from django.urls import path
from . import views

app_name = 'your_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
```

movie/views.pyの編集

```Python
from django.http import HttpResponse
from django.template import loader

def index(request):
    latest_question_list = 1
    template = loader.get_template('your_app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('your_app/about.html')
    context = {}
    return HttpResponse(template.render(context, request))
```

pymovie/urls.pyの編集

```Python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),
]
```

movie/templatesディレクトリの作成

```
mkdir app/src/movie/templates
```


movie/templates/movieディレクトリの作成

```
mkdir app/src/movie/templates/movie
```

movie/templates/movieディレクトリの作成

```
mkdir app/src/movie/templates/movie
```

movie/templates/layout.htmlの作成

```
touch app/src/movie/templates/layout.html
```

movie/templates/movie/ index.htmlの作成

```
touch app/src/movie/templates/movie/index.html
```

/app/static/下にアセットディレクトリを作成&アセット追加

```
mkdir app/static/css
mkdir app/static/img
mkdir app/static/js
touch app/static/css/app.css
touch app/static/js/app.js
```


## 既存movieアプリケーションの作成

アプリケーションの新規作成は[movieアプリケーションの新規作成](##movieアプリケーションの新規作成)へ

movieディレクトリへのシンボリックリンクの作成

movieディレクトリの[パス](./app/movie):[/app/movie]

```shell-session
$ docker-compose run uwsgi ln -s ../movie movie
```

sttings.pyの「INSTALLED_APPS」に下記を追記

```Python
INSTALLED_APPS = {
...
    'your_app.apps.Your_AppConfig',
...
}
```

## movieアプリケーションのマイグレーション実行

movieアプリーションデータのマイグレーションファイル作成

```shell-session
$ docker-compose run uwsgi python manage.py makemigrations movie
```

マイグレーションファイル編集

マイグレーション実行

```shell-session
$ docker-compose run uwsgi python manage.py migrate
```


## 本番環境構築

本番環境での手順を簡単にまとめる。

### 手順

```
・Gitのインストール
・Dockerのインストール
・certbotのインストール
・.well-knownディレクトリの作成
・コンテナのビルド
```
