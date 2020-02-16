from .api import *
from attrdict import AttrDict

def execGetApi():
    response = getPopularApi()
    return response

def execSearchApi(query=''):
    response = searchMovie(query)
    return response
