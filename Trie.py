from moon_words import positive_words, negative_words, stopwords
import re
import dill as pickle
from cfg import sentiment_trie_path


class Node:
    """Sentiment Node"""

    def __init__(self, char):
        self.value = char
        self.children = {}
        self.is_end = False
        self.sentiment = 0
        # self.word = None


class SentimentTrie:
    """Trie structure with each node stores its sentiment"""

    def __init__(self):
        self.root = Node(None)
        self.sentiment_trie = None
        self.search_result = {}

    def insert(self, key: str, sentiment: int):
        """
        insert a word into the trie with its sentiment
        :param key: word
        :param sentiment: 1 as positive, -1 as negative, 11 as stopword
        """
        curr_node = self.root
        for index, char in enumerate(key):
            if char in curr_node.children:
                curr_node = curr_node.children[char]

            else:
                new_node = Node(char)
                curr_node.children[char] = new_node
                curr_node = new_node

        curr_node.is_end = True
        curr_node.sentiment = sentiment
        curr_node.word = key

    def insert_words(self, word_arr: list, sentiment):
        """
        insert an list words with same sentiment into the trie
        :param word_arr: list of words
        :param sentiment: sentiment of the words list
        """
        for word in word_arr:
            self.insert(word, sentiment)

    def search(self, key: str):
        """
        search for a give word in the trie, if the word is in the trie, return its sentiment, else
        the word is considered as neutral, return 0
        :param key: word to be searched
        :return: 1 if key in the trie and has a sentiment of 1 (positive)
                 -1 if key in the trie ana has a sentiment of -1 (negative)
                 11 if key in the trie and has a sentiment of 11 (stopword)
                 0 if key not in the trie (neutral)
        """
        curr_node = self.root
        neutral_sentiment = 0
        for char in key:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return neutral_sentiment  # not exist
        if curr_node.is_end:
            return curr_node.sentiment
        else:
            return neutral_sentiment

    # def sentiment_search(self, article_arr: list):
    #     """search if the words are in the sentiment tree and return the sentiment word counts
    #     :param article_arr: all words in an article as a list
    #     :return: sentiment dict of the number of neutral, positive, negative, stop words
    #     """
    #     sentiment = {0: 0, 1: 0, -1: 0, 11: 0}
    #     for word in article_arr:
    #         word_sentiment = self.search(word)
    #         sentiment[word_sentiment] += 1
    #     return sentiment

    def generate_sentiment_search_report(self, article_arr: list):
        """if the words are in the sentiment tree and return the sentiment search reports
        search
        :param article_arr: all words in an article as a list
        :return: sentiment report dict of sentiment word counts, neutral, positive, negative, and stop word frequencies
        """
        sentiment = {0: 0, 1: 0, -1: 0, 11: 0}
        pos_freq = {}
        neg_freq = {}
        neutral_freq = {}
        stop_freq = {}
        for word in article_arr:
            word_sentiment = self.search(word)
            sentiment[word_sentiment] += 1
            if word_sentiment == 0:
                if word in neutral_freq:
                    neutral_freq[word] += 1
                else:
                    neutral_freq[word] = 1

            elif word_sentiment == 11:
                if word in stop_freq:
                    stop_freq[word] += 1
                else:
                    stop_freq[word] = 1

            elif word_sentiment == 1:
                if word in pos_freq:
                    pos_freq[word] += 1
                else:
                    pos_freq[word] = 1

            else:
                if word in neg_freq:
                    neg_freq[word] += 1
                else:
                    neg_freq[word] = 1

        return {
            "sentiment": sentiment,
            "neutral": neutral_freq,
            "positive": pos_freq,
            "negative": neg_freq,
            "stop": stop_freq
        }

    def clear(self):
        """clear the nodes in the current trie"""
        self.root = Node(None)


class trie_utils:
    def __init__(self):
        self.path = sentiment_trie_path

    def preprocess(self, str):
        return re.sub('[^a-zA-Z\s\-]', ' ', str).split()

    def build_sentiment_trie(self):
        st = SentimentTrie()
        st.insert_words(positive_words, 1)
        st.insert_words(negative_words, -1)
        st.insert_words(stopwords, 11)
        self.pickle_dump_trie(st)
        return st

    def pickle_dump_trie(self, trie):
        file_obj = open(self.path, 'wb')
        pickle.dump(trie, file_obj)
        file_obj.close()

    def pickle_load_trie(self):
        file_obj = open(self.path, 'rb')
        st = pickle.load(file_obj)
        file_obj.close()
        return st

    def get_score(self, sentiment):
        # print(sentiment)
        return (int(sentiment[1]) / int(sentiment[-1])) / int(sentiment[0]) * 100


from articles import cn

if __name__ == '__main__':
    trie = trie_utils().pickle_load_trie()

    article_arr = trie_utils().preprocess(cn)
    res = trie.generate_sentiment_search_report(article_arr)
    res = trie.sentiment_search('bad')

    print(res)
