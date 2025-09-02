# utils/helpers.py
from fpdf import FPDF


def format_markdown(grouped_by_group):
    md = "# 🌍 Weekly Climate Research Digest\n\n"
    for group in ["Journals 📚", "Blogs & News 📰", "Other ❓"]:
        if group in grouped_by_group:
            md += f"# {group}\n\n"
            for source_name, bundle in sorted(grouped_by_group[group].items()):
                md += f"## {source_name}\n"
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


def save_pdf(markdown_text, filepath):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=12)

    for line in markdown_text.split("\n"):
        clean_line = line.encode("latin-1", "replace").decode("latin-1")
        if clean_line.strip():
            pdf.multi_cell(0, 10, clean_line)
        else:
            pdf.ln()

    pdf.output(str(filepath))
