from rest_framework import serializers
from book.models import Book, Author
from django_filters import rest_framework as filters


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
   
    class Meta:
        
        model = Book
        fields = ('title','publication')
