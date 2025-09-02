# summarizer.py
def summarize_articles(articles, max_chars=300):
    summarized = []
    for art in articles:
        desc = art["summary"]
        desc = desc.replace("\n", " ").strip()
        short_desc = desc[:max_chars] + ("..." if len(desc) > max_chars else "")
        summarized.append(
            {
                "title": art["title"],
                "link": art["link"],
                "summary": short_desc,
                "author": art.get("author", ""),
                "source": art.get("source", ""),
                "pub_dt": art.get("pub_dt"),
                "rss_source": art.get("rss_source", art.get("source", "")),
                "source_name": art.get("source_name", ""),
                "source_group": art.get("source_group", ""),
                "rss_url": art.get("rss_url", ""),
            }
        )
    return summarized
