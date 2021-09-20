from books.api.views import BookListApiView, BookDetailsApiView, BookCreateApiView
from django.urls import path


urlpatterns = [
    path('books/', BookListApiView.as_view(), name="books-list"),
    path('books/<int:book_id>', BookDetailsApiView.as_view(), name="books-details"),
    path('db/', BookCreateApiView.as_view(), name="books-create")
]

