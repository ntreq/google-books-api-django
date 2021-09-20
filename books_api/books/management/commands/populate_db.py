from django.core.management.base import BaseCommand
from books.models import Author, Book, Category
import requests

class Command(BaseCommand):
    args = ''
    help = 'run this command to pupulate database with books information from GoogleAPI'

    def _get_books_data(self, url):
        data = requests.get(url=url)
        return data.json()

    def _create(self):
        data = self._get_books_data()
        for item in data['items']['volumeInfo']:
            




