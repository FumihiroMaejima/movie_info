from .api import *
from .processingData import *
from attrdict import AttrDict
from movie.serializers import *

def execGetApi():
    response = getPopularApi()
    return response

def execGetMovieTitleApi():
    response = getPopularApiPerPage()
    result = makeMovieTitlesArray(AttrDict(response).results)
    return result

def execSearchApi(query=''):
    validated = InputDataValidationSerializer(data={'inputData': query})
    if validated.is_valid():
        return searchMovie(query)
    else:
        result = {
            'execution' : False,
            'message' : 'your input data is wrong',
            'data': AttrDict(validated.errors).inputData[0]
        }
        return result
