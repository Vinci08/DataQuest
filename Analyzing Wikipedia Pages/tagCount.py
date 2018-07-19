from bs4 import BeautifulSoup

def tag_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = {}
    for tag in soup.find_all():
        if tag.name not in tags:
            tags[tag.name] = 0
        tags[tag.name] += 1
    return tags