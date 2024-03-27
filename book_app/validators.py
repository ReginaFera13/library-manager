from django.core.exceptions import ValidationError
import re

def validate_title(title):
    error_message = 'This title should be "Book #" format'
    regex = r'^Book [\d]+$'
    good_title = re.match(regex, title)
    if good_title:
        return title
    raise ValidationError(error_message, params={'Current Value':title})

def validate_author(author):
    error_message = 'This author should be "Author #" format'
    regex = r'^Author [\d]+$'
    good_author = re.match(regex, author)
    if good_author:
        return author
    raise ValidationError(error_message, params={'Current Value':author})

def validate_isbn(isbn):
    error_message = 'This isbn should be "###-##########" format'
    regex = r'^\d{3}-\d{10}$'
    good_isbn = re.match(regex, isbn)
    if good_isbn:
        return isbn
    raise ValidationError(error_message, params={'Current Value':isbn})

def validate_genre(genre):
    error_message = 'This genre should be Title format'
    regex = r'^[A-Z][a-z]+( [A-Z][a-z]+)*$'
    good_genre = re.match(regex, genre)
    if good_genre:
        return genre
    raise ValidationError(error_message, params={'Current Value':genre})

