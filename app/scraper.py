from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm

img_dumb = []
url = f"https://www.xendan.org/detailnews/{178140}"
proxied_fetch = f"https://spontaneous-faloodeh-9e9321.netlify.app/?destination={url}"
html = urlopen(proxied_fetch)
bs = BeautifulSoup(html, "html.parser")
header_elem = bs.find("div", {"class": "detail-top"})
article_elem = bs.find("div", {"class": "detail-big-text-p"})
img_elem = bs.find("div", {"class": "detail-big-img"})
# print(img_elem.img['src'])
if header_elem and article_elem and header_elem.find("h1"):
    header = header_elem.find("h1").text.strip()
    article = article_elem.text.strip()
    image = img_elem.img["src"] if img_elem else " "
    img_dumb.append({"Header": header, "Article": article, "Link": url})
