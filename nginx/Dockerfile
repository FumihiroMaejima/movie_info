# ベースイメージの設定
FROM nginx:1.17.7
RUN apt-get update && apt install -y \
    nodejs \
    npm

CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
