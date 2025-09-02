# fetch/rss_reader.py
import feedparser
from fetch.feeds import JOURNAL_FEEDS, BLOG_FEEDS

ALL_FEEDS = {**JOURNAL_FEEDS, **BLOG_FEEDS}


def fetch_feed(url):
    d = feedparser.parse(url)
    if not d.entries:
        return []

    articles = []
    for entry in d.entries:
        article = {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "summary": entry.get("summary", ""),
            "author": entry.get("author", ""),
            "published_parsed": entry.get("published_parsed"),
            "source": entry.get("source", {}).get("title", ""),
            "rss_source": url,
        }
        articles.append(article)
    return articles


def fetch_all_feeds():
    all_articles = []
    for url in ALL_FEEDS:
        try:
            feed_articles = fetch_feed(url)
            all_articles.extend(feed_articles)
        except Exception as e:
            print(f"⚠️ Error fetching {url}: {e}")
    return all_articles
