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

```
http://localhost
```


## movie アプリケーションの作成

sttings.pyの「INSTALLED_APPS」に下記を追記

```Python
INSTALLED_APPS = {
...
    'webpack_loader',
    'your_app',
...
}
```
movieディレクトリへのシンボリックリンクの作成

```shell-session
$ docker-compose run uwsgi ln -s ../movie movie
```

アセットコンパイル

```shell-session
$ docker-compose run uwsgi npm run dev
```
pymovie/urls.pyを下記の通り修正する。

```Python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),
]
```

gameアプリーションデータのマイグレーションファイル作成

```shell-session
$ docker-compose run uwsgi python manage.py makemigrations game
```

gameアプリーションデータのマイグレーション実行

```shell-session
$ docker-compose run uwsgi python manage.py migrate
```


## アプリケーションの新規作成

```shell-session
$ docker-compose run uwsgi ./manage.py startapp your_app
```
pymovie/settings.pyの「INSTALLED_APPS」に作成したアプリケーション名を追記すること。

```Python
INSTALLED_APPS = {
...
    'your_app',
...
}
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
