import requests
import xml.etree.ElementTree as ET
from goose3 import Goose
import db

def fetch_article_links(feed_url):
  response = requests.get(feed_url)
  response.raise_for_status()  # Raise an exception if there's an error

  root = ET.fromstring(response.content)
  channel = root.find("channel")  # Assuming a standard RSS structure
  items = channel.findall("item")

  article_links = [item.find("link").text for item in items]
  return article_links

article_urls = fetch_article_links('http://18.153.14.238/api/query.php?user=freshrss&t=59YTupLQxkyOwAQdRjwhqX&f=rss')


def insert_articles():
    g = Goose()
    current_rows = db.table.get_rows()
    for url in article_urls:
            print(url)
            if not db.check_duplicates(current_rows, url):
                id = db.add_new_row().id
                print(id)
                article = g.extract(url=url)
                print("article.cleaned_text")
                db.save_article(id, url, article.cleaned_text)
                print(False)
            else:
                print(True)
                continue
    g.close()

insert_articles()

