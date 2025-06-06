# fetch/rss_reader.py
import feedparser

FEED_URLS = [
    "https://www.nature.com/nclimate.rss",
    "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science",
    "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=sciadv",
    "http://feeds.feedburner.com/RealClimate",
    "https://skepticalscience.com/rss.php",
    "https://www.climate.gov/news-features/rss.xml",
    "https://granthaminstitute.com/feed/",
]

def fetch_all_feeds():
    articles = []
    for url in FEED_URLS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title"),
                "link": entry.get("link"),
                "summary": entry.get("summary", "")
            })
    return articles


