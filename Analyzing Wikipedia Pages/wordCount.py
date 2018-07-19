from bs4 import BeautifulSoup
from collections import Counter
import re

def word_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    text = re.sub("\W+", " ", text.lower())
    words = text.split(" ")
    words = [w for w in words if len(w) >= 5]
    return Counter(words).most_common(10)