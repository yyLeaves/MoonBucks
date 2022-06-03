from moon_words import positive_words, negative_words


class Node:
    """Sentiment Node"""

    def __init__(self, char):
        self.value = char
        self.children = {}
        self.is_end = False
        self.sentiment = 0
        self.word = None


class SentimentTrie:
    def __init__(self):
        self.root = Node(None)
        self.sentiment_trie = None
        self.search_result = {}

    def insert(self, key: str, sentiment: int):
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
        for word in word_arr:
            self.insert(word, sentiment)

    def search(self, key: str):
        curr_node = self.root
        neutral_sentiment = 0
        for char in key:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return neutral_sentiment  # not exist
        if curr_node.is_end == True:
            return curr_node.sentiment
        else:
            return neutral_sentiment

    def sentiment_search(self, article_arr: list):
        sentiment = {0: 0, 1: 0, -1: 0}
        for word in article_arr:
            word_sentiment = self.search(word)
            sentiment[word_sentiment] += 1
        return sentiment

    def generate_sentiment_search_report(self, article_arr: list):
        sentiment = {0: 0, 1: 0, -1: 0}
        pos_freq = {}
        neg_freq = {}
        neutral_freq = {}
        for word in article_arr:
            word_sentiment = self.search(word)
            sentiment[word_sentiment] += 1
            if word_sentiment == 0:
                if word in neutral_freq:
                    neutral_freq[word] += 1
                else:
                    neutral_freq[word] = 1

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
            "negative": neg_freq
        }

    def clear(self):
        self.root = Node(None)


class trie_utils:
    def __init__(self):
        self.sentiment_trie = None

    def build_sentiment_trie(self):
        st = SentimentTrie()
        st.insert_words(positive_words, 1)
        st.insert_words(negative_words, -1)
        print(st)
        self.sentiment_trie = st

    def get_sentiment_trie(self):
        if self.sentiment_trie is None:
            return self.build_sentiment_trie()
        else:
            return self.sentiment_trie

    def pickle_dump_trie(self):
        pass

    def pickle_load_trie(self):
        pass


from articles import cn

if __name__ == '__main__':
    trie = SentimentTrie()
    trie.insert_words(positive_words, 1)
    trie.insert_words(negative_words, -1)
    # result = trie.search_article(cn.split())
    cn_arr = cn.split()
    res = trie.sentiment_search(cn_arr)
    res = trie.generate_sentiment_search_report(cn_arr)
    print(res)
