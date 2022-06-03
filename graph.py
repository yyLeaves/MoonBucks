import plotly
import plotly.graph_objs as pg
import numpy as np


class Graph:
    def __init__(self):
        self.country_name = []
        self.positive_word = []
        self.negative_word = []
        self.neutral_word = []
        self.stopwords_word = []
        self.score = []

    def data_converter(self, country_detail):
        self.country_name.append(country_detail[0])
        self.neutral_word.append(country_detail[1])
        self.negative_word.append(country_detail[2])
        self.positive_word.append(country_detail[3])
        self.stopwords_word.append(country_detail[4])
        self.score.append(country_detail[5])

    def graph_maker(self):
        # trace = [len(self.country_name)]
        positive = pg.Scatter(
            x=self.country_name,
            y=self.positive_word,
            name="Positive Words"
        )
        negative = pg.Scatter(
            x=self.country_name,
            y=self.negative_word,
            name="Negative Words"
        )
        neutral = pg.Scatter(
            x=self.country_name,
            y=self.neutral_word,
            name="Neutral Words"
        )
        stopwords = pg.Scatter(
            x=self.country_name,
            y=self.stopwords_word,
            name="Stopwords Words"
        )

        trace = [positive, neutral, negative, stopwords]
        layout = pg.Layout(
            title="Words Sentiment Analysis"
        )
        fig = pg.Figure(data=trace, layout=layout)
        plotly.offline.plot(fig, filename='Scatter.html')

    def score_ranker(self):
        arr1 = np.array(self.country_name)
        arr2 = np.array(self.score)
        arrIndex = np.array(arr2).argsort()
        arr1 = arr1[arrIndex]
        arr2 = arr2[arrIndex]

        score_rank = pg.Bar(
            x=arr1,
            y=arr2,
            name="Score"
        )
        layout = pg.Layout(
            title="Score Rank"
        )
        fig = pg.Figure(data=score_rank, layout=layout)
        plotly.offline.plot(fig, filename="Rank.html")
