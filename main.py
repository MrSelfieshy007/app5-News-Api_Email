import requests

api_key = "8b996866cebb471fb2c15edbd6c1cffe"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-27&sortBy=publishedAt&apiKey=8b996866cebb471fb2c15edbd6c1cffe"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
