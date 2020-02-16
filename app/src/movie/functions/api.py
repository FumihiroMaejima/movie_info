import django_filters
import requests
# import json
from attrdict import AttrDict
from movie.config import *
from rest_framework import viewsets, filters

def testApi():
    response = requests.get(
        API_TEST_CONFIG.test_api_url,
        params = {
            API_TEST_CONFIG.param_api_key: API_TEST_CONFIG.value_api_key,
            API_TEST_CONFIG.param_language: API_TEST_CONFIG.value_language
        }
    )
    return response.json()


def getPopularApi():
    response = requests.get(
        API_POPULAR_CONFIG.test_api_url,
        params = {
            API_POPULAR_CONFIG.param_api_key: API_POPULAR_CONFIG.value_api_key,
            API_POPULAR_CONFIG.param_language: API_POPULAR_CONFIG.value_language,
            API_POPULAR_CONFIG.param_page: API_POPULAR_CONFIG.value_page
        }
    )
    return response.json()


def searchMovie(query=''):
    response = requests.get(
        API_SEARCH_CONFIG.search_url,
        params = {
            API_SEARCH_CONFIG.param_api_key: API_SEARCH_CONFIG.value_api_key,
            API_SEARCH_CONFIG.param_language: API_SEARCH_CONFIG.value_language,
            API_SEARCH_CONFIG.param_page: API_SEARCH_CONFIG.value_page,
            API_SEARCH_CONFIG.param_query: query
        }
    )
    return response.json()

def getImage():
    response = requests.get(
        API_TEST_CONFIG.test_api_url,
        params = {
            API_TEST_CONFIG.param_api_key: API_TEST_CONFIG.value_api_key
        }
    )

    imageUrl = MOVIE_IMAGE_CONFIG.poster_size_185_url + AttrDict(response.json()).production_companies[0].logo_path
    return imageUrl
