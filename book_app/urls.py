from django.urls import path
from .views import All_books, A_book

urlpatterns = [
    path("", All_books.as_view(), name="all_books"),
    path("<int:id>/", A_book.as_view(), name="a_book"),
]