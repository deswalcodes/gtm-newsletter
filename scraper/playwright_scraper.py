from playwright.sync_api import sync_playwright

def fetch_ai_news_playwright():
    print("🧪 Scraping AI news with Playwright...")
    articles = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.aitoolsclub.com/")  # You can replace with any dynamic AI tool/news site
        page.wait_for_timeout(5000)  # wait 5 seconds for JS to render

        cards = page.query_selector_all("h2")
        for card in cards[:5]:
            title = card.inner_text()
            articles.append({
                "title": title,
                "link": "https://www.aitoolsclub.com/"
            })

        browser.close()

    return articles
