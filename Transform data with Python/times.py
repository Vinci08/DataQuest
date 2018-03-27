import read
import pandas as pd
import dateutil
import datetime

df = read.load_data()

def extract_hour(time):
    y = dateutil.parser.parse(time)
    return y.hour

df["hour"] = df["submission_time"].apply(extract_hour)

hour_count = df["hour"].value_counts()

print(hour_count.head())
