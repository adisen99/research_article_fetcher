# # fetch/rss_reader.py
# import feedparser
# from fetch.feeds import JOURNAL_FEEDS, BLOG_FEEDS

# ALL_FEEDS = {**JOURNAL_FEEDS, **BLOG_FEEDS}


# def fetch_feed(url):
#     d = feedparser.parse(url)
#     if not d.entries:
#         return []

#     articles = []
#     for entry in d.entries:
#         article = {
#             "title": entry.get("title", ""),
#             "link": entry.get("link", ""),
#             "summary": entry.get("summary", ""),
#             "author": entry.get("author", ""),
#             "published_parsed": entry.get("published_parsed"),
#             "source": entry.get("source", {}).get("title", ""),
#             "rss_source": url,
#         }
#         articles.append(article)
#     return articles


# def fetch_all_feeds():
#     all_articles = []
#     for url in ALL_FEEDS:
#         try:
#             feed_articles = fetch_feed(url)
#             all_articles.extend(feed_articles)
#         except Exception as e:
#             print(f"⚠️ Error fetching {url}: {e}")
#     return all_articles


# fetch/rss_reader.py
import feedparser
from fetch.feeds import JOURNAL_FEEDS, BLOG_FEEDS

# from datetime import datetime
import time

# Merge all feeds
ALL_FEEDS = {**JOURNAL_FEEDS, **BLOG_FEEDS}

# Define which feeds need filtering
CLIMATE_SPECIFIC_FEEDS = {
    "Nature Climate Change",
    "Nature Geoscience",
    "Journal of Climate",
    "JGR Atmospheres",
    "Climate Dynamics",
    "NOAA Climate.gov",
    "RealClimate",
}
GENERAL_FEEDS = set(ALL_FEEDS.keys()) - CLIMATE_SPECIFIC_FEEDS

# Climate keywords for filtering
CLIMATE_KEYWORDS = [
    "climate",
    "warming",
    "temperature",
    "precipitation",
    "ENSO",
    "El Niño",
    "La Niña",
    "greenhouse",
    "carbon",
    "emissions",
    "atmosphere",
    "ocean",
    "cryosphere",
    "monsoon",
    "rainfall",
    "drought",
    "heatwave",
    "sea level",
    "glacier",
]


def is_climate_article(article):
    text = (article.get("title", "") + " " + article.get("summary", "")).lower()
    return any(kw.lower() in text for kw in CLIMATE_KEYWORDS)


def fetch_feed(name, url):
    d = feedparser.parse(url)
    if not d.entries:
        print(f"⚠️ No entries found in {name}")
        return []

    articles = []
    for entry in d.entries:
        pub = entry.get("published_parsed") or entry.get("updated_parsed")
        article = {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "summary": entry.get("summary", ""),
            "author": entry.get("author", ""),
            "published_parsed": pub,
            "source": name,
            "rss_source": url,
            "source_group": "Journal" if name in JOURNAL_FEEDS.values() else "Blog",
        }
        # Apply filter only if it's a general feed
        if name in GENERAL_FEEDS:
            if not is_climate_article(article):
                continue
        articles.append(article)
    print(f"✅ {len(articles)} articles fetched from {name}")
    return articles


def fetch_all_feeds():
    all_articles = []
    for name, url in ALL_FEEDS.items():
        try:
            feed_articles = fetch_feed(name, url)
            all_articles.extend(feed_articles)
        except Exception as e:
            print(f"⚠️ Error fetching {name} ({url}): {e}")
    return all_articles


def get_top_climate_articles(n=10):
    """Fetch and return top N most recent climate articles"""
    articles = fetch_all_feeds()

    # Sort by publication date (newest first)
    articles.sort(
        key=lambda x: (
            time.mktime(x["published_parsed"]) if x["published_parsed"] else 0
        ),
        reverse=True,
    )

    # Limit between 5 and 10
    return articles[: max(5, min(n, 10))]
