# utils/helpers.py
def format_markdown(articles):
    md = "# Weekly Climate Research Digest\n\n"
    for art in articles:
        md += f"### [{art['title']}]({art['link']})\n"
        md += f"{art['summary']}\n\n"
    return md
