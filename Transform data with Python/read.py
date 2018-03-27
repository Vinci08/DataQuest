import pandas as pd 

def load_data():
    hn=pd.read_csv('hn_stories.csv', header = None)
    hn.columns=['submission_time','upvotes','url','headline']
    return hn

    if __name__ == "__main__": 
        load_data()
