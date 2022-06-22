import pandas as pd
from cfg import csv_path


def pick_country(n):
    df = pd.read_csv(csv_path)
    count_series = df['state'].value_counts()
    count_dict = count_series.to_dict()
    topn = list(count_dict)[:n]
    return topn


def random_sample(country, csv_path, n):
    df = pd.read_csv(csv_path)
    df = df[df['state'] == country]
    df = df[['longitude', 'latitude']]
    stores = df.sample(n)
    stores_dict = stores.to_dict()
    lat = stores_dict['latitude']
    lon = stores_dict['longitude']
    x = [lat[e] for e in lat]
    y = [lon[e] for e in lon]
    return [[x[i], y[i]] for i in range(n)]


stores = random_sample('US', csv_path, n)
# stores

if __name__ == '__main__':
    # US, CA, JP, CN, GB
    top5 = pick_country(5)
    print(f"Top 5 countries with most stores are {', '.join(top5)}")
