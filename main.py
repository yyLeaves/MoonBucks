from Trie import *
from graph import Graph
from articles import articles
from moon_utils import pick_country

if __name__ == '__main__':

    # pick country
    top5 = pick_country(5)
    print(f"Top 5 countries with most stores are {', '.join(top5)}\n")

    # build sentiment trie
    trie = trie_utils().pickle_load_trie()

    data_list = []

    # sentiment analysis by words
    for country in articles.keys():
        data_list = []

        article_arr = trie_utils().preprocess(articles[country])

        # If want other stats about words, run the below,
        # you can fetch the stats in the dict
        # res = trie.generate_sentiment_search_report(article_arr)
        # sentiment = res['sentiment']

        # If only want score, this will be more efficiency
        sentiment = trie.sentiment_search(article_arr)
        score = trie_utils().get_score(sentiment)

        data_list.append([country, sentiment[0], sentiment[-1], sentiment[1], sentiment[11], score])

        print(
            f"{country} has {sentiment[0]} neutral words, {sentiment[-1]} negative words, {sentiment[1]} positive words, {sentiment[11]} stop words")
        print(f"{country} has a score of {score}")
    # graph = Graph()
    # graph.graph_maker()
    # graph.score_ranker()
