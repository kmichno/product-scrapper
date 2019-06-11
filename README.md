# product-scrapper

Programy można uruchomić komendą:
```
scrapy crawl product_ceneo -a phrase="Brother" -a task_id="1"
scrapy crawl product_allegro -a phrase="Brother" -a task_id="1"
```
Jako pierwszy argument podajemy jakąś nazwę produktu jakiego poszukujemy, a jako drugi identyfikator zadania.

Modułu potrzebne do zaimportowania to:
```
Scrapy
pymongo
```

Potrzebne do skonfigurawania dane do MongoDB w pliku `product_scrapper/settings.py`:
```
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "scrapper"
MONGODB_COLLECTION = "products"
```
Pola w kolekcji "products":
```
name
url
description
price
task_id
```
