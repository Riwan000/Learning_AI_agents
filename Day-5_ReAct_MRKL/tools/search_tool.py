import os
import requests

def web_search(query: str) -> str:
    api_key = os.getenv("SERPAPI_KEY")  # Set this in your .env or shell
    if not api_key:
        return "SerpAPI key not found."

    url = "https://serpapi.com/search"
    params = {"q": query, "api_key": api_key, "num": 3}

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Search failed: {response.text}"

    data = response.json()
    results = data.get("organic_results", [])[:3]
    if not results:
        return "No results found."

    return "\n\n".join([f"{r['title']}\n{r['link']}" for r in results])
