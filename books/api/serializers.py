from django.db.models import fields
from rest_framework import serializers
from books.models import Author, Book, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publishedDate', 'categories',
                  'average_rating', 'ratings_count', 'thumbnail']

