from django.db import models
from django.core import validators as v
from .validators import validate_author, validate_genre, validate_isbn, validate_title

# Create your models here.
class Book(models.Model):
    title = models.CharField(validators = [v.MaxLengthValidator(100), validate_title])
    author = models.CharField(validators = [v.MaxLengthValidator(100), validate_author])
    isbn = models.CharField(unique=True, validators = [v.MaxLengthValidator(14), validate_isbn])
    genre = models.CharField(validators = [v.MaxLengthValidator(100), validate_genre])
    published_date = models.DateField()
    
    def __str__(self):
        return f'{self.title} by {self.author}'