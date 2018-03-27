import read
from collections import Counter

df = read.load_data()

all_string = df["headline"].str.cat(sep=', ')

all_string = all_string.lower()

print(Counter((all_string).split()).most_common(100))
