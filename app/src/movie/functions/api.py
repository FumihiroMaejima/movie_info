import django_filters
import requests
# import json
# from attrdict import AttrDict
from movie.config import API_TEST_CONFIG
from rest_framework import viewsets, filters

def testApi():
    response = requests.get(
        API_TEST_CONFIG.test_api_domain,
        params={API_TEST_CONFIG.param_name: API_TEST_CONFIG.api_key}
    )
    return response.json()
