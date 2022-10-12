import requests
import re
from bs4 import BeautifulSoup



query = input("Введите запрос: ")
query = query.replace(" ", "+")
URL = f"https://google.com/search?q={query}"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
headers = {"User-Agent" : USER_AGENT}
request = requests.get(URL, headers = headers)
print(request.status_code)
soup = BeautifulSoup(request.content, "html.parser")
results = []
results1= []
for res in soup.find_all("div", class_="MjjYud", limit = 20):
    ans = res.find_all("a")
    if ans:
        if "href" in ans[0].attrs:
            link = ans[0]["href"]
    if res.find("h3"):
        title = res.find("h3").text
    item = {
        "title": title,
        "link": link
    }
    results.append(item)
for x in results:
    if x["link"][0] == "/": x["link"] = "https://google.com" + x["link"]
    print(x["title"],": ",x["link"])

