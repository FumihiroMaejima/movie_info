from attrdict import AttrDict

def makeMovieTitlesArray(movies = []):
    titles = []
    # for index, movie in enumerate(movies):
    for movie in movies:
        titles.append(movie.title)

    result = {
        'execution': True,
        'message': 'request OK',
        'data': titles
    }
    return result
