import json
from django.db.models.query import prefetch_related_objects
from django.test import TestCase
from rest_framework import response, serializers
from rest_framework.test import APIClient
from books.models import Author, Book, Category
from books.api.views import BookListApiView
from books.api.serializers import BookSerializer
# Create your tests here.

class BookTestCase(TestCase):
    def setUp(self):
        a1 = Author.objects.create(name="John Smith")
        a2 = Author.objects.create(name="Bob Cross")
        c1 = Category.objects.create(name="Biology")
        c2 = Category.objects.create(name="Educational")

        book = Book.objects.create(api_id="zxcvb", 
                            title="Ants",
                            published_date=2005,
                            average_rating=3.5,
                            ratings_count=10,
                            thumbnail="https://via.placeholder.com/350x150")

        book.authors.set([a1, a2])
        book.categories.set([c1, c2])
        book2 = Book.objects.create(api_id="asdfg", 
                            title="Cooking",
                            published_date=2021,
                            average_rating=5,
                            ratings_count=3,
                            thumbnail="https://via.placeholder.com/350x150")

    def test_book_creation(self):
        book = Book.objects.get(api_id="zxcvb")
        self.assertEqual(book.authors.count(), 2)
        self.assertEqual(book.categories.count(), 2)

    def test_get_list_method(self):
        client = APIClient()
        response = client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
    
    def test_get_details_method(self):
        client = APIClient()
        response = client.get('/api/books/1')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        book = Book.objects.get(id=1)
        serializer = BookSerializer(book)
        self.assertEqual(response_data, serializer.data)

    def test_get_search(self):
        client = APIClient()
        book = Book.objects.get(id=1)
        response = client.get(f'/api/books/?published_date={book.published_date}')
        response_data = json.loads(response.content)
        serializer = BookSerializer(book)
        self.assertEqual(*response_data, serializer.data)

    def test_get_authors(self):
        client = APIClient()
        book = Book.objects.get(id=1)
        response = client.get(f'/api/books/?author=John+Smith&author=Bob+Cross')
        response_data = json.loads(response.content)
        serializer = BookSerializer(book)
        self.assertEqual(*response_data, serializer.data)

    def test_sort_published_date_asc(self):
        client = APIClient()
        book = Book.objects.get(id=1)
        response = client.get('/api/books/?sort=published_date')
        response_data = json.loads(response.content)[0]
        serializer = BookSerializer(book)
        self.assertEqual(response_data, serializer.data)

    def test_sort_published_date_desc(self):
        client = APIClient()
        book = Book.objects.get(id=2)
        response = client.get('/api/books/?sort=-published_date')
        response_data = json.loads(response.content)[0]
        serializer = BookSerializer(book)
        self.assertEqual(response_data, serializer.data)



    def test_post_method(self):
        client = APIClient()
        response = client.post('/api/db/', {'q': 'war'}, format='json')
        self.assertEqual(response.status_code, 200)
        books = Book.objects.all()
        self.assertEqual(books.count(), 12)


