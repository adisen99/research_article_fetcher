# main.py
from fetch.rss_reader import fetch_all_feeds
from summarizer import summarize_articles
from utils.helpers import format_markdown  # , save_pdf
import json
from pathlib import Path
from datetime import datetime, timedelta


def main():
    feeds = fetch_all_feeds()

    # Filter by date (last 7 days)
    recent_articles = []
    cutoff = datetime.utcnow() - timedelta(days=7)
    for art in feeds:
        pub_date = art.get("published_parsed")
        if pub_date:
            pub_dt = datetime(*pub_date[:6])
            if pub_dt >= cutoff:
                recent_articles.append(art)

    summaries = summarize_articles(recent_articles)
    md = format_markdown(summaries)

    # Save Markdown and PDF to output file
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "climate_digest.md", "w") as f:
        f.write(md)

    # save_pdf(md, output_dir / "climate_digest.pdf")

    print(
        "\nClimate digest created at output/climate_digest.md and output/climate_digest.pdf"
    )


if __name__ == "__main__":
    main()
