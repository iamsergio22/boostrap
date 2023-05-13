from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book import serializers
from django.http import JsonResponse

from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def postBook(request):
    data=request.data
    book=Book.objects.create(
        body=data['body']
    )
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def putBook(request,pk):
    data=request.data
    book=Book.objects.get(id=pk)
    serializer=BookSerializer(instance=book,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBook(request,pk):    
    book=Book.objects.get(id=pk)
    book.delete()
    return Response('Book deleted')



