import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    jj_count = data["JJ"].value_counts()
    sch_count = data["SCH_STATUS_MAGNET"].value_counts()
    
    jj_pt = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")

    sch_pt = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
    
    print(sch_pt)
    print(jj_pt)
    