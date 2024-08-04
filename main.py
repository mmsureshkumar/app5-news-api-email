import requests

API_KEY = "7ae9f92f67dd4c598299b3eb94061a36"
url = f"https://newsapi.org/v2/everything?q=apple&from=2024-08-03&to=2024-08-03&sortBy=popularity&apiKey={API_KEY}"

# Make the request
request = requests.get(url)

# Get the dictionary
context = request.json()

for article in context["articles"]:
    print(article["description"])
    print(article["title"])
