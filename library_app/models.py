from django.db import models
from book_app.models import Book
from client_app.models import Client

# Create your models here.
class Rental(models.Model):
    a_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    a_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.a_book.title} is currently rented by {self.a_client.username}'