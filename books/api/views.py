from django_filters.rest_framework import DjangoFilterBackend
import requests
import json
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework import filters
from rest_framework import filters
from rest_framework.response import Response
from books.models import Author, Book, Category
from books.api.serializers import AuthorSerializer, BookSerializer, CategorySerializer

class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['published_date']
    ordering_fields = ['published_date']

    def filter_queryset(self, queryset):
        queryset = super(BookListApiView, self).filter_queryset(queryset)
        # published_date = self.request.query_params.get('published_date', None)
        authors = self.request.query_params.getlist('author', None)
        if authors is not None:
            for author in authors:
                queryset = queryset.filter(authors__name__contains=author)
        # if published_date is not None:
                # queryset = queryset.filter()
        return queryset


class BookDetailsApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, book_id):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request):
        body_decoded = self.request.body.decode('utf-8')
        body = json.loads(body_decoded)
        query = body["q"]
        if query is not None:
            r = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")
            if r.status_code == 200:
                books_data = r.json()
                for item in books_data["items"]:
                    volume_info = item["volumeInfo"]
                    book_info = {
                        "api_id": item["id"],
                        "title": volume_info.get("title"),
                        "published_date": volume_info.get("publishedDate")[:4],
                        "average_rating": volume_info.get("averageRating"),
                        "ratings_count": volume_info.get("ratingsCount"),
                    }
                    if volume_info.get("imageLinks") is not None:
                        book_info["thumbnail"] = volume_info.get("imageLinks").get("thumbnail")
                    else:
                        book_info["thumbnail"] = None
                    authors = [Author.objects.get_or_create(name=author)[0] 
                                for author in volume_info.get("authors", [])]
                    categories = [Category.objects.get_or_create(name=category)[0]
                                for category in volume_info.get("categories", [])]
                    book, _ = Book.objects.update_or_create(**book_info)
                    book.authors.add(*authors)
                    book.categories.set(categories)
                    book.save()
                return Response(status=200)
            return Response({"error": "Query"}, status=r.status_code)
        return Response({"error": "Please specify 'q' parameter in the URL."}, status=400)
        