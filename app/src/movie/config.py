import os
import json
from attrdict import AttrDict

# TMDB API INFO
MOVIE_API_DOMAIN = os.getenv('TMDB_API_DOMAIN', 'pymovie')
MOVIE_API_KEY = os.getenv('TMDB_API_KEY', 'pymovie')
MOVIE_TEST_API_ROUTE = '3/movie/550'
MOVIE_POPULAR_API_ROUTE = '3/movie/popular'

# TMDB IMAGE INFO
MOVIE_IMAGE_DOMAIN = os.getenv('TMDB_IMAGE_API_DOMAIN', 'pymovie')

"""
Movie Image of API Config
type: json
"""
MOVIE_IMAGE_CONFIG = AttrDict(json.loads('{}'))
MOVIE_IMAGE_CONFIG.poster_size_185_url = MOVIE_IMAGE_DOMAIN + 't/p/w185'
MOVIE_IMAGE_CONFIG.poster_size_342_url = MOVIE_IMAGE_DOMAIN + 't/p/w342'

"""
Movie Test API Config
type: json
"""
API_TEST_CONFIG = AttrDict(json.loads('{}'))
API_TEST_CONFIG.test_api_url = MOVIE_API_DOMAIN + MOVIE_TEST_API_ROUTE
# get request parameter
API_TEST_CONFIG.param_api_key = 'api_key'
API_TEST_CONFIG.value_api_key = MOVIE_API_KEY
API_TEST_CONFIG.param_language = 'language'
API_TEST_CONFIG.value_language = 'ja-JP'

"""
Movie Popular API Config
type: json
"""
API_POPULAR_CONFIG = AttrDict(json.loads('{}'))
API_POPULAR_CONFIG.test_api_url = MOVIE_API_DOMAIN + MOVIE_POPULAR_API_ROUTE
# get request parameter
API_POPULAR_CONFIG.param_api_key = 'api_key'
API_POPULAR_CONFIG.value_api_key = MOVIE_API_KEY
API_POPULAR_CONFIG.param_language = 'language'
API_POPULAR_CONFIG.value_language = 'ja-JP'
API_POPULAR_CONFIG.param_page = 'page'
API_POPULAR_CONFIG.value_page = 1



