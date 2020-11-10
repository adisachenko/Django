from django.urls import path
from .views import BookList
from django_filters.views import FilterView
from django.conf.urls import url
from book.models import Book, Author
from book.views import AuthorViewSet
from rest_framework import routers
from . import views



app_name = 'book'
# app_name will help us do a reverse look-up latter.

router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet, basename='Author')

urlpatterns = [
    path('books/', BookList.as_view()),
]
urlpatterns +=router.urls 
