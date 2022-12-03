from django.urls import path
from .views.follow import follow
from .views.signup import signup
from .views.signin import signin
from .views.settings import settings
from .views.index import index
from .views.logout import logout
from .views.like_post import like_post
from .views.profile import profile
from .views.upload import upload
from .views.search import search

urlpatterns = [
    path('', index, name='index'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', logout, name='logout'),
    path('settings', settings, name='settings'),
    path('upload', upload, name='upload'),
    path('like-post', like_post, name='like-post'),
    path('profile/<str:pk>', profile, name='profile'),
    path('follow', follow, name='follow'),
    path('search', search, name='search')
]
