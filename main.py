import requests
from send_email import send_email

API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
url = f"https://newsapi.org/v2/everything?q=apple&from=2024-08-03&to=2024-08-03&sortBy=popularity&apiKey={API_KEY}&language=en"

# Make the request
request = requests.get(url)

# Get the dictionary
context = request.json()
body = ""
for article in context["articles"]:
    if article["title"] is not None:
        body = ("Subject: Today's News" + body + article["description"] + "\n"
                + article["title"] + "\n" + article["url"] + "\n")

body = body.encode("utf-8")
send_email(body)
