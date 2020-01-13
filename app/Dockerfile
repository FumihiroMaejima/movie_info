FROM python:3.7
ENV PYTHONUNBUFFERED 1
#
#RUN apt-get update && apt install -y \
#    nodejs \
#    npm \
#    && npm install n -g \
#    && n stable \
#    && apt purge -y nodejs npm \
#    && npm install -g yarn \
#    && yarn global add @vue/cli
RUN mkdir /var/www
WORKDIR /var/www
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src
CMD ["uwsgi", "--socket", ":3031", "--module", "pymovie.wsgi"]
