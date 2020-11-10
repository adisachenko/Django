from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response




class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
           queryset = queryset.filter(title=title)
           return queryset

from .models import Author

class AuthorViewSet(viewsets.ViewSet):
    
    
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)