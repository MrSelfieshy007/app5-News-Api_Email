import requests
from send_email import send_email

topic = 'tesla'

api_key = "8b996866cebb471fb2c15edbd6c1cffe"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2023-05-27&" \
    "sortBy=publishedAt&" \
    "apiKey=8b996866cebb471fb2c15edbd6c1cffe&" \
    "language=en"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:10]:
    body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + article["description"] +"\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
