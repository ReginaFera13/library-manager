from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


from .serializers import BookSerializer, Book

# Create your views here.

class All_books(APIView):
    def get(self, request):
        books = Book.objects.order_by('id')
        ser_books = BookSerializer(books, many=True)
        return Response(ser_books.data, status=HTTP_200_OK)
    
class A_book(APIView):
    def get(self, request, id):
       book = get_object_or_404(Book, id=id)
       ser_book = BookSerializer(book)
       return Response(ser_book.data, status=HTTP_200_OK)