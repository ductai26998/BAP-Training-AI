import connect_db as db
import scrapy_data as scrapy

# Connect to database
my_db = db.Database(host='localhost',
                 user='root',
                 password='ductai2207',
                 port='3307',
                 database='bap_ai')
# info of the 3000 words web page
words_url = "https://www.ef-australia.com.au/english-resources/english-vocabulary/top-3000-words/"
words_selector = "p:last-child"

# info of the synonyms web page
synonyms_url = "https://www.thesaurus.com/browse/"
synonyms_selector = "#meanings .e1ccqdb60"

# scrape data from the 3000 words web page
words = scrapy.scrape(words_url, words_selector)

def insert_record(word: str, synonyms: str):
    """
        insert a record into your database
        input:
            word: field word
            synonyms: field synonyms
    """
    sql = "INSERT INTO synonyms(word, synonyms) VALUES (%s, %s)"
    params = (word, synonyms)
    my_db.insert_item(sql, *params)

def scrape_and_insert():
    """
        scrape data from the synonyms web page of each word
        in the 3000 words web page.
    """
    count = 1;
    for word in words:
        word_url = "https://www.thesaurus.com/browse/" + word
        synonyms = scrapy.scrape(word_url, synonyms_selector)
        insert_record(word, str(synonyms))
        print(count)
        count = count + 1

def search(word: str):
    """
        search and print the synonyms of the word in the 3000 words web page
    """
    sql = "SELECT synonyms FROM synonyms WHERE word=%s"
    params = (word,)
    synonyms = my_db.get_item(sql, *params)
    print("synonyms of {}: ".format(word))
    for synonym in synonyms:
        print(synonym)

# scrape_and_insert()
keyword = input("Enter the keyword: ")
search(keyword)