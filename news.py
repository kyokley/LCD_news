import requests
import feedparser
from unidecode import unidecode

SOURCES = ['http://feeds.feedburner.com/TheHackersNews',
           'http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml']

def get_headlines():
    headlines = []
    for source in SOURCES:
        try:
            data = requests.get(source, timeout=1).content
        except:
            continue

        feed_data = feedparser.parse(data)
        headlines.extend([unidecode(x.get('title_detail', {})
                           .get('value', ''))
                           .encode('ascii', 'ignore')
                           for x in feed_data.entries])
    return headlines
