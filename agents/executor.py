from tools.weather_tool import get_weather
from tools.github_tool import search_repos

def execute(plan: dict):
    results = []

    for step in plan["steps"]:
        try:
            if step["tool"] == "weather":
                results.append(get_weather(step["action"]))

            elif step["tool"] == "github":
                results.append(search_repos(step["action"]))

        except Exception as e:
            results.append({
                "error": str(e),
                "step": step
            })

    return results
