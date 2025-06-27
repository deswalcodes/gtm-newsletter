
import arxiv

def fetch_arxiv_papers(query="speech recognition", max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'summary': result.summary,
            'link': result.entry_id,
            'published': result.published.strftime("%Y-%m-%d"),
            'authors': [author.name for author in result.authors]
        })

    return papers

# Example usage (remove before prod use):
if __name__ == "__main__":
    for paper in fetch_arxiv_papers():
        print(paper['title'], "-", paper['link'])
