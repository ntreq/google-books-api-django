# google-books-api-django

### Simple Google Books API application written in Django which saves fetched books data to database found from given query - for example _'hobbit'_ or _'war'_.
###
https://www.googleapis.com/books/v1/volumes?q=query
---
### Instalation
``` 
pip install -r requirements.txt
```
---
### Run tests
```
python manage.py test book
```
---
### Usage

**List of all saved books:**

- GET `http://127.0.0.1:8000/api/books/`

**Book details:**

- GET `http://127.0.0.1:8000/api/books/{id}`

**Search by publish date (year):**

- GET `http://127.0.0.1:8000/api/books/?published_date={year}`

**Ascending sorting by publish date:**

- GET `http://127.0.0.1:8000/api/books/?sort=published_date`

**Descending sorting by publish date:**

- GET `http://127.0.0.1:8000/api/books/?sort=-published_date`

**Filtering by author (to filter by many authors append more '&author='):**

- GET `http://127.0.0.1:8000/api/books/?author={}`

**Fetching data from Google API for given query:**

- POST `http://127.0.0.1:8000/api/db`
- Request body - `{'q': 'query'}`
- Head - `"Content-Type: application/json"`

Example using cURL:
```
$ curl -X POST -H "Content-Type: application/json" --data '{"q": "hobbit"}' 127.0.0.1:8000/api/db/
```