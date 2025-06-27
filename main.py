# main.py
from scraper.rss_scraper import fetch_rss_articles
from scraper.arxiv_scraper import fetch_arxiv_papers
from scraper.extra_sources import fetch_google_news, fetch_producthunt
from llm.summarizer import summarize_text
from storage.db_neon import save_newsletter
from scraper.playwright_scraper import fetch_ai_news_playwright
from mail.send_mailchimp import send_newsletter
import markdown

def run_newsletter():
    # read current edition from edition.txt
    with open("edition.txt", "r") as f:
        edition_number = int(f.read().strip())

    title = f"Weekly AI Transcription Digest — Edition #{edition_number}"

    print("Fetching articles...")
    rss_sources = [
        "https://www.reddit.com/r/MachineLearning/.rss",
        "https://techcrunch.com/tag/ai/feed/",
        "https://venturebeat.com/category/ai/feed/"
    ]
    articles = fetch_rss_articles(rss_sources)

    print("Fetching papers...")
    papers = fetch_arxiv_papers("speech transcription")

    print("Fetching Google News...")
    google_news = fetch_google_news("speech to text")

    print("Fetching Product Hunt launches...")
    producthunt = fetch_producthunt()

    playwright_articles = fetch_ai_news_playwright()
    combined_stories = articles[:3] + google_news[:2] + producthunt[:2] + playwright_articles[:2]

    # build the markdown
    newsletter_md = f"""# 🗞️ {title}

Welcome to this week’s curated roundup of the most important updates in the world of **AI Transcription** and **Speech-to-Text** technologies. Stay ahead with industry news, fresh research, and innovative tools.

---

## 🧠 Featured Stories

"""

    for story in combined_stories:
        print(f"Summarizing: {story['title']}")
        summary = summarize_text(story['title'] + "\n" + story['link'])
        newsletter_md += f"""### 🎯 [{story['title']}]({story['link']})

{summary}

"""

    newsletter_md += """---

## 📚 Research Spotlights

The latest breakthroughs and scholarly highlights worth exploring:
"""

    for paper in papers[:3]:
        print(f"Summarizing: {paper['title']}")
        summary = summarize_text(paper['summary'])
        newsletter_md += f"""### 📄 [{paper['title']}]({paper['link']})

{summary}

"""

    newsletter_md += f"""---

Thanks for reading this edition of **AI Transcription Digest**. We’ll see you next week with more cutting-edge updates and insights.

*Edition #{edition_number} — Automated with ❤️ by the GTM Engineering Challenge Stack*

"""

    # Save markdown
    with open(f"newsletter_edition_{edition_number}.md", "w") as f:
        f.write(newsletter_md)

    # Save to Neon
    save_newsletter(edition_number, title, newsletter_md)

    # Convert to HTML
    final_output = markdown.markdown(newsletter_md)

    # Send via Mailchimp
    send_newsletter(title, final_output)

    print(f"\n✅ Newsletter Edition #{edition_number} generated and sent successfully!\n")

    # increment edition number
    with open("edition.txt", "w") as f:
        f.write(str(edition_number + 1))

    return final_output

if __name__ == "__main__":
    run_newsletter()
