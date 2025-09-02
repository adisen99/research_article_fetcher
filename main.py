# main.py
from fetch.rss_reader import fetch_all_feeds
from fetch.feeds import JOURNAL_FEEDS, BLOG_FEEDS
from summarizer import summarize_articles

from utils.helpers import format_markdown  # , save_pdf
import json
from pathlib import Path
from datetime import datetime, timedelta


def main():
    feeds = fetch_all_feeds()

    recent_articles = []
    cutoff = datetime.utcnow() - timedelta(days=7)

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

    summaries = summarize_articles(recent_articles)

    grouped = {"Journals 📚": {}, "Blogs & News 📰": {}, "Other ❓": {}}
    for art in summaries:
        grp = art.get("source_group", "Other ❓")
        src = art.get("source_name", "Unknown")
        if src not in grouped[grp]:
            grouped[grp][src] = {"url": art.get("rss_url", ""), "articles": []}
        grouped[grp][src]["articles"].append(art)

    for g in grouped:
        for src in grouped[g]:
            grouped[g][src]["articles"].sort(
                key=lambda x: x.get("pub_dt"), reverse=True
            )

    md = format_markdown(grouped)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "climate_digest.md", "w") as f:
        f.write(md)

    # save_pdf(md, output_dir / "climate_digest.pdf")

    print(
        "\nClimate digest created at output/climate_digest.md"
        # "\nClimate digest created at output/climate_digest.md and output/climate_digest.pdf"
    )


if __name__ == "__main__":
    main()
