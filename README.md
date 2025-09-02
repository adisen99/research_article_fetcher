# research_article_fetcher

A Python program to fetch recently published climate research articles and summarize them. Generates **weekly or monthly digests** of top climate articles from journals and blogs.

---

## **Features ✅**

- Fetches articles from **major climate science journals**:
  - Nature, Nature Climate Change, Nature Geoscience, Nature Communications, Science, Science Advances, Journal of Climate, Climate Dynamics, Geophysical Research Letters, JGR: Atmospheres & Oceans, Earth’s Future, Atmospheric Research, and more.  
- Fetches articles from **blogs & news sources**:
  - Skeptical Science, RealClimate, NOAA Climate.gov, Grantham Institute, The Economist (Climate), The Conversation (Climate), Climate Brink.  
- Filters articles to **climate-related topics** using keywords.  
- Selects **top 5–10 most important articles** based on source weights and recency.  
- Summarizes articles using **Sumy extractive summarization**:
  - Uses RSS summary + title for all articles.  
  - Optionally, top articles can be summarized from full text for richer highlights.  
- Produces a **Markdown digest** with:
  - Top 3 highlights section  
  - Grouped journals and blogs  
  - Author, publication date, and RSS feed link  
- Lightweight, runs **without any paid APIs**.  
- Configurable for **weekly or monthly digests**.

---

## **Usage 🛠️**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/research_article_fetcher.git
cd research_article_fetcher
```


2. Install dependencies

```bash
pip install -r requirements.txt
```


3. Run the script.

```bash
python main.py
```

4. Choose digest frequency in main.py


```python
# For weekly digest (default)
cutoff_days = 7

# For monthly digest
cutoff_days = 30
```

5. Output markdown digest is saed in the `output/` folder

```bash
output/climate_digest.md
```


## **Project Structure 📂**

```bash
research_article_fetcher/
├─ main.py             # Main script to generate digest
├─ fetch/
│  ├─ feeds.py         # RSS feed URLs
│  ├─ rss_reader.py    # Fetches articles from feeds
│  └─ filter.py        # Ranking and filtering logic
├─ summarizer.py       # Summarizes articles using Sumy
├─ utils/
│  └─ helpers.py       # Markdown formatting helpers
├─ output/             # Generated Markdown digests
└─ requirements.txt    # Python dependencies
```



## **To-Do / Future Improvements 📝**


- Fetch full article text for richer summarization of top articles.
- Add PDF export in addition to Markdown.
- Add highlight emojis/icons for top articles or categories.
- Expand source feeds to cover more climate journals/news outlets.
- Add keyword-based filtering for specific topics (ENSO, monsoon, sea-level rise, etc.).
- Implement automatic scheduling for weekly/monthly digest generation.
- Optional interactive web version for displaying digests.
- Improve summarization quality using hybrid methods for top articles.
