# fetch/rss_reader.py
import feedparser

FEED_URLS = [
    # Nature Portfolio
    "https://www.nature.com/nclimate.rss",
    "https://www.nature.com/ngeo.rss",
    "https://www.nature.com/ncomms.rss",
    "https://www.nature.com/commsenv.rss",
    "https://www.nature.com/natrevearthenviron.rss",
    "https://www.nature.com/natreviews.rss",
    # Science family
    "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science",
    "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=sciadv",
    # AGU journals
    "https://agupubs.onlinelibrary.wiley.com/feed/journal/21699275/earlyview",  # GRL
    "https://agupubs.onlinelibrary.wiley.com/feed/journal/21699291/earlyview",  # JGR: Atmospheres
    "https://agupubs.onlinelibrary.wiley.com/feed/journal/21699273/earlyview",  # JGR: Oceans
    "https://agupubs.onlinelibrary.wiley.com/feed/journal/23284277/earlyview",  # Earth's Future
    # EGU journals
    "https://bg.copernicus.org/rss.xml",  # Biogeosciences
    "https://acp.copernicus.org/rss.xml",  # Atmospheric Chemistry and Physics
    "https://esd.copernicus.org/rss.xml",  # Earth System Dynamics
    "https://nhess.copernicus.org/rss.xml",  # Natural Hazards and Earth System Sciences
    # Other key climate science journals
    "https://journals.ametsoc.org/feed/journal/jcli/earlyview",  # Journal of Climate
    "https://link.springer.com/search.rss?facet-journal-id=382&channel-name=Climate+Dynamics",  # Climate Dynamics
    "https://www.sciencedirect.com/journal/atmospheric-research/rss",  # Atmospheric Research
    # Blogs and News
    "http://feeds.feedburner.com/RealClimate",
    "https://skepticalscience.com/rss.php",
    "https://www.climate.gov/news-features/rss.xml",
    "https://granthaminstitute.com/feed/",
    "https://www.economist.com/climate/rss.xml",
    "https://theconversation.com/au/environment/articles.atom",
    "https://climatebrink.substack.com/feed",
]


def fetch_all_feeds():
    articles = []
    for url in FEED_URLS:
        feed = feedparser.parse(url)
        source = feed.feed.get("title", "Unknown Source")
        for entry in feed.entries:
            articles.append(
                {
                    "title": entry.get("title"),
                    "link": entry.get("link"),
                    "summary": entry.get("summary", ""),
                    "author": entry.get("author", ""),
                    "source": source,
                    "published_parsed": entry.get("published_parsed"),
                }
            )
    return articles
