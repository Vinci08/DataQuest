import read
import numpy
import pandas as pd

daf = read.load_data()

domain_end = ["com", "co", "org", "edu", "net"]

def remove_subdomain(domain):
    separate = str(domain).split(".")
    if len(separate) > 2:
        if separate[-1] in domain_end:
            domain = separate[-2]+"."+separate[-1]
        else:
            domain = separate[-3]+"."+separate[-2]+"."+separate[-1]
    return domain

daf["url"] = daf["url"].apply(remove_subdomain)

domains = daf["url"].value_counts()
domains = domains[:99]

for name, row in domains.items():
    print("{0}: {1}".format(name, row))
