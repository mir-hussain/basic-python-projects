from bs4 import BeautifulSoup
import requests


yc_website = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(yc_website.text, "html.parser")

anchor_list = soup.select(".titleline a")

titles = [a.text for a in anchor_list]
links = [a.get("href") for a in anchor_list]

upvotes = [int(upvote.text.split()[0]) for upvote in soup.select(".score")]

top_voted_index = upvotes.index(max(upvotes))

top_voted_article = {
    "title": titles[top_voted_index],
    "link": links[top_voted_index],
    "upvote": upvotes[top_voted_index]
}

# print(links)
print(top_voted_article)
