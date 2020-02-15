import os
import json
from attrdict import AttrDict

# TMDB API INFO
MOVIE_API_DOMAIN = os.getenv('TMDB_API_DOMAIN', 'pymovie')
MOVIE_API_KEY = os.getenv('TMDB_API_KEY', 'pymovie')
MOVIE_TEST_API_ROUTE = '3/movie/550'

"""
Movie API Config
type: json
"""
API_TEST_CONFIG = AttrDict(json.loads('{}'))
API_TEST_CONFIG.test_api_domain = MOVIE_API_DOMAIN + MOVIE_TEST_API_ROUTE
API_TEST_CONFIG.api_key = MOVIE_API_KEY
API_TEST_CONFIG.param_name = 'api_key'
