from django.urls import path
from movie.views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies/search', MovieViewSet, basename='movie')
urlpatterns = router.urls

'''
from . import views
app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
'''
