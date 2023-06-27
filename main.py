import requests
from send_email import send_email

api_key = "8b996866cebb471fb2c15edbd6c1cffe"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-27&sortBy=publishedAt&apiKey=8b996866cebb471fb2c15edbd6c1cffe"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
