
import feedparser

def fetch_rss_articles(sources, max_items=5):
    articles = []

    for source in sources:
        feed = feedparser.parse(source)
        for entry in feed.entries[:max_items]:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.get('published', ''),
                'source': source
            })

    return articles


if __name__ == "__main__":
    urls = [
        "https://www.reddit.com/r/MachineLearning/.rss",
        "https://techcrunch.com/tag/ai/feed/",
        "https://venturebeat.com/category/ai/feed/"
    ]
    for article in fetch_rss_articles(urls):
        print(article['title'], "-", article['link'])
