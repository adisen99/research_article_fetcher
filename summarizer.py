# summarizer.py
def summarize_articles(articles, max_chars=300):
    # Rule-based summary: truncate summary if needed
    summarized = []
    for art in articles:
        desc = art["summary"]
        desc = desc.replace("\n", " ").strip()
        short_desc = desc[:max_chars] + ("..." if len(desc) > max_chars else "")
        summarized.append({
            "title": art["title"],
            "link": art["link"],
            "summary": short_desc,
            "author": art.get("author", ""),
            "source": art.get("source", "")
        })
    return summarized
