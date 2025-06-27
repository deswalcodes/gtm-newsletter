import requests
from bs4 import BeautifulSoup

def fetch_google_news(query="speech recognition"):
    print("Fetching Google News articles...")
    url = f"https://news.google.com/search?q={query.replace(' ', '%20')}&hl=en-IN&gl=IN&ceid=IN:en"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.select("article")[:5]:
        headline = item.select_one("h3")
        if headline:
            title = headline.text
            link = "https://news.google.com" + headline.find("a")["href"][1:]
            articles.append({"title": title, "link": link})
    
    return articles

def fetch_producthunt():
    print("Fetching Product Hunt launches...")
    url = "https://www.producthunt.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    products = []
    for item in soup.select("h3.font-semibold.text-large")[:5]:
        title = item.text.strip()
        products.append({"title": title, "link": "https://www.producthunt.com"})

    return products
