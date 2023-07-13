import requests
from send_email import send_email
from datetime import date

#topic = 'tesla'
#today = str(date.today())
#print(today)

api_key = "use_newsapi.org_for_api"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-29&sortBy=publishedAt&apiKey=8b996866cebb471fb2c15edbd6c1cffe"

request = requests.get(url)
content = request.json()
print(content)
body = ""
for article in content["articles"][:10]:
    body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + article["description"] +"\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
