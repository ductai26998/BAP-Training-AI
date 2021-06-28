# Searching synonyms

## Set up
**Install python and pip: [Here](https://www.python.org/downloads/)**

**Install virtual environment for Searching_synonyms project:**
```php
python -m venv Searching_synonyms
```
**Install dependences:**
```php
pip install -r requirements.txt
```
## Usage
**connect_db.py:**
Create a object which can connect to mySQL database and handle with this database:
* connect_database: private
* get_all: public
* get_item: public

**scrapy_data.py:**
Scrape data from a web page

**main.py:** Has the functions:
* insert_record: public
* scrape_and_insert: public
* search: public
