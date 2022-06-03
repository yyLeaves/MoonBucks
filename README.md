Week 8:

preprocess the negative words and positive words in a python list in module 'moon_words.py' so that it can be imported
to be used easily.

write the code to preprocess the text.

Week 9:

Question 1 should be a multiple string match problem. I googled the problem, and found that aho-corasick algorithm can
satisfy the problem. AC algorithm is the combination of KMP and Trie structure. It has linear time complexity in
matching. We can store the Trie structure in previous, and save it in a pickle file for future use, so that it saves the
preprocess time.

Week 10

I implemented the AC algorithm, but there is a problem. The algorithm match all the existing patterns based on
characters instead of words. For example, in string 'apple tree' and pattern 'app', 'apple', the result will return
the 'app' and 'apple' together, and that is definately not what we want. Maybe Trie structure is simply what we want. We
can add the word's sentiment in trie node self.sentiment, in doing so, we can store all positive words and negative
words in one trie structure.

Week 11

I implemented the Trie algorithm, besides the positive and negative words, I also add the stopwords in the trie. It
turns out that the stopwords also takes a big part of the overall words in an article. For the task of simply counting
the pos, neg, stop, and neutral words, Instead of build an individual stopword trie, and filter the stopwords before the
sentiment analysis. It will be a little bit more efficient just to store them altogether in a single trie. Although the
complexities are about the same.

Besides, I also stored the trie in a pickle file of all the words, so that every time we need to analyse an article, we
don't have to build a trie. instead we simply load the trie from pickle file and that can save some time complexity

Since the positive and negative words already have -ed, -es form, there is no need to lemmatize them.

To calculated the score, we think only using positive subtract negative words may not be a good idea, since there are
long articles and short articles, long article definately have more positive words and more negative words, so we use (
positive words / negative words) / (neutral words) * 1000 to calculate the score
