import requests
import time

def search_repos(query: str, retries=2):
    url = (
        f"https://api.github.com/search/repositories"
        f"?q={query}&sort=stars&order=desc"
    )

    for _ in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            items = response.json().get("items", [])[:3]
            return [
                {
                    "name": repo["name"],
                    "stars": repo["stargazers_count"],
                    "url": repo["html_url"]
                }
                for repo in items
            ]
        time.sleep(1)

    raise Exception("GitHub API failed")
