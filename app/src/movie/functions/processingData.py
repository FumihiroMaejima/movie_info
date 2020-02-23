from attrdict import AttrDict

def makeMovieTitlesArray(movies = []):
    result = []
    # for index, movie in enumerate(movies):
    for movie in movies:
        result.append(movie.title)
    return result
