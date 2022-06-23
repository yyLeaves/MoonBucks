import plotly.graph_objs as pg
import numpy as np


def bar_graph(country_detail):
    country_detail = np.transpose(country_detail)
    positive = pg.Bar(
        x=country_detail[0],
        y=np.array(country_detail[3]).astype(int),
        name="Positive Words"
    )
    negative = pg.Bar(
        x=country_detail[0],
        y=np.array(country_detail[2]).astype(int),
        name="Negative Words"
    )
    neutral = pg.Bar(
        x=country_detail[0],
        y=np.array(country_detail[1]).astype(int),
        name="Neutral Words"
    )
    stopwords = pg.Bar(
        x=country_detail[0],
        y=np.array(country_detail[4]).astype(int),
        name="Stopwords Words"
    )
    trace = [positive, neutral, negative, stopwords]
    layout = pg.Layout(
        title="Words Sentiment Analysis"
    )
    fig = pg.Figure(data=trace, layout=layout)
    fig.write_html("Bar.html")


def score_graph(country_detail):
    country_detail = np.transpose(country_detail)
    arr1 = np.array(country_detail[0])
    arr2 = np.array(country_detail[5]).astype(float)
    arrIndex = np.array(arr2).argsort()
    arr1 = arr1[arrIndex]
    arr2 = arr2[arrIndex]

    score_rank = pg.Scatter(
        x=arr1,
        y=arr2,
        name="Score"
    )
    layout = pg.Layout(
        title="Score Rank"
    )
    fig = pg.Figure(data=score_rank, layout=layout)
    fig.write_html("Rank.html")
