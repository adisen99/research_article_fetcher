# main.py
from fetch.rss_reader import fetch_all_feeds
from fetch.feeds import JOURNAL_FEEDS, BLOG_FEEDS
from fetch.filter import filter_and_rank  # use your scoring function
from summarizer import summarize_articles
from utils.helpers import format_markdown
from pathlib import Path
from datetime import datetime, timedelta


def main():
    print("🔄 Fetching feeds...")
    feeds = fetch_all_feeds()

    # Only articles from the past 30 days
    cutoff = datetime.utcnow() - timedelta(days=30)
    recent_articles = []
    for art in feeds:
        pub_date = art.get("published_parsed")
        if pub_date:
            pub_dt = datetime(*pub_date[:6])
            if pub_dt >= cutoff:
                art["pub_dt"] = pub_dt
                rss_url = art.get("rss_source", "")
                if rss_url in JOURNAL_FEEDS:
                    art["source_group"] = "Journals 📚"
                    art["source_name"] = JOURNAL_FEEDS[rss_url]
                    art["rss_url"] = rss_url
                elif rss_url in BLOG_FEEDS:
                    art["source_group"] = "Blogs & News 📰"
                    art["source_name"] = BLOG_FEEDS[rss_url]
                    art["rss_url"] = rss_url
                else:
                    art["source_group"] = "Other ❓"
                    art["source_name"] = rss_url or "Unknown"
                    art["rss_url"] = rss_url
                recent_articles.append(art)

    # Rank and filter to top 10 using your scoring function
    top_articles = filter_and_rank(recent_articles, max_items=10, days=30)

    # Summarize
    summaries = summarize_articles(top_articles)

    # Group by source
    grouped = {"Journals 📚": {}, "Blogs & News 📰": {}, "Other ❓": {}}
    for art in summaries:
        grp = art.get("source_group", "Other ❓")
        src = art.get("source_name", "Unknown")
        if src not in grouped[grp]:
            grouped[grp][src] = {"url": art.get("rss_url", ""), "articles": []}
        grouped[grp][src]["articles"].append(art)

    # Sort articles by publication date
    for g in grouped:
        for src in grouped[g]:
            grouped[g][src]["articles"].sort(
                key=lambda x: x.get("pub_dt"), reverse=True
            )

    # Generate Markdown
    md = format_markdown(grouped)

    # Save to output
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "climate_digest_monthly.md", "w") as f:
        f.write(md)

    print("\n✅ Monthly Climate digest created at output/climate_digest_monthly.md")


if __name__ == "__main__":
    main()
