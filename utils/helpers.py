# utils/helpers.py
def format_markdown(grouped_by_group):
    md = "# 🌍 Monthly Climate Science Digest\n\n"
    md += "📌 **Top 3 Highlights**\n\n"

    # Collect top 3 articles by date across all sources
    top3 = []
    for group in grouped_by_group:
        for source_name, bundle in grouped_by_group[group].items():
            top3.extend(bundle["articles"])
    top3.sort(key=lambda x: x.get("pub_dt"), reverse=True)
    for art in top3[:3]:
        md += f"### ⭐ [{art['title']}]({art['link']})\n"
        if art["author"]:
            md += f"👤 **Author**: {art['author']}\n"
        if art["pub_dt"]:
            md += f"🗓️ **Published**: {art['pub_dt'].strftime('%Y-%m-%d')}\n"
        md += f"📰 **Source**: {art.get('source_name','Unknown')}\n"
        md += f"{art['summary']}\n\n"

    # Now list the rest grouped by journal/blog
    for group in ["Journals 📚", "Blogs & News 📰", "Other ❓"]:
        if group in grouped_by_group:
            md += f"# {group}\n\n"
            for source_name, bundle in sorted(grouped_by_group[group].items()):
                md += f"## 🏛️ {source_name}\n"
                if bundle["url"]:
                    md += f"🔗 Feed: {bundle['url']}\n\n"
                for art in bundle["articles"]:
                    md += f"### [{art['title']}]({art['link']})\n"
                    if art["author"]:
                        md += f"👤 **Author**: {art['author']}\n"
                    if art["pub_dt"]:
                        md += f"🗓️ **Published**: {art['pub_dt'].strftime('%Y-%m-%d')}\n"
                    md += f"{art['summary']}\n\n"
    return md
