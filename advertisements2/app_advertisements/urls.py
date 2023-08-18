from django.urls import path
from .views import *
urlpatterns = [
    path('index/', index,  name ='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile,  name ='profile'),
    path('advertisement/', advertisement,  name='advertisement'),
]