# main.py
from fetch.rss_reader import fetch_all_feeds
from summarizer import summarize_articles
from utils.helpers import format_markdown
import json
from pathlib import Path


def main():
    feeds = fetch_all_feeds()
    summaries = summarize_articles(feeds)
    md = format_markdown(summaries)

    # Save Markdown to output file
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "climate_digest.md", "w") as f:
        f.write(md)

    print("\nClimate digest created at output/climate_digest.md")


if __name__ == "__main__":
    main()
