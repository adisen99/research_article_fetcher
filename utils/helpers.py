# utils/helpers.py
from fpdf import FPDF
from pathlib import Path


def format_markdown(articles):
    md = "# Weekly Climate Research Digest\n\n"
    for art in articles:
        md += f"### [{art['title']}]({art['link']})\n"
        if art["author"]:
            md += f"**Author**: {art['author']}\n"
        if art["source"]:
            md += f"**Source**: {art['source']}\n"
        md += f"{art['summary']}\n\n"
    return md


def save_pdf(markdown_text, filepath):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=12)

    for line in markdown_text.split("\n"):
        # Convert special characters to ASCII fallback
        clean_line = line.encode("latin-1", "replace").decode("latin-1")
        if clean_line.strip():
            pdf.multi_cell(0, 10, clean_line)
        else:
            pdf.ln()

    pdf.output(str(filepath))
