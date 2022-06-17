import pandas as pd
from cfg import csv_path


def pick_country(n):
    df = pd.read_csv(csv_path)
    count_series = df['state'].value_counts()
    count_dict = count_series.to_dict()
    topn = list(count_dict)[:n]
    return topn


if __name__ == '__main__':
    # US, CA, JP, CN, GB
    top5 = pick_country(5)
    print(f"Top 5 countries with most stores are {', '.join(top5)}")
