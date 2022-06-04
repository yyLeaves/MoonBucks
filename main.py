from Trie import *
from graph import Graph
from articles import articles

if __name__ == '__main__':
    trie = trie_utils().pickle_load_trie()
    graph = Graph()


    for country in articles.keys():
        article_arr = trie_utils().preprocess(articles[country])

        # If want other stats about words, run the below,
        # you can fetch the stats in the dict
        # res = trie.generate_sentiment_search_report(article_arr)
        # sentiment = res['sentiment']

        # If only want score, this will be more efficiency
        sentiment = trie.sentiment_search(article_arr)
        score = trie_utils().get_score(sentiment)
        graph.data_converter([country, sentiment[0], sentiment[-1], sentiment[1], sentiment[11], score])
        print(
            f"{country} has {sentiment[0]} neutral words, {sentiment[-1]} negative words, {sentiment[1]} positive words, {sentiment[11]} stop words")
        print(f"{country} has a score of {score}")
    graph.graph_maker()
    graph.score_ranker()