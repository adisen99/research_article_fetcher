# fetch/filter.py
from datetime import datetime, timedelta
import heapq

SOURCE_WEIGHTS = {
    "Nature": 5,
    "Nature Climate Change": 5,
    "Science": 5,
    "Science Advances": 4,
    "NOAA Climate.gov": 3,
    "RealClimate": 2,
    "Skeptical Science": 2,
    # fallback
    "Other": 1,
}


def score_article(article):
    """Higher score = more important"""
    weight = SOURCE_WEIGHTS.get(article["source"], 1)
    # Prefer recent: subtract days since publication
    if article["published_parsed"]:
        pub_date = datetime(*article["published_parsed"][:6])
        days_old = (datetime.utcnow() - pub_date).days
        recency_bonus = max(0, 7 - days_old)  # up to 7 pts for fresh articles
    else:
        recency_bonus = 0
    return weight * 10 + recency_bonus


def filter_and_rank(articles, max_items=10, days=7):
    cutoff = datetime.utcnow() - timedelta(days=days)
    recent_articles = []
    for a in articles:
        if a["published_parsed"]:
            pub_date = datetime(*a["published_parsed"][:6])
            if pub_date < cutoff:
                continue
        recent_articles.append(a)

    # Rank by score
    ranked = heapq.nlargest(max_items, recent_articles, key=score_article)
    return ranked
