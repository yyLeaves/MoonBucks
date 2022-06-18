# Algo-assignment

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/76979429?s=48&amp;v=4" alt="@yyLeaves" class=" avatar-user" width="24" height="24"> [@yyLeaves](https://github.com/yyLeaves): Chief Algorithm Engineer

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/49346779?s=48&amp;v=4" alt="@Koukotsukan" class=" avatar-user" width="24" height="24"> [@Koukotsukan](https://github.com/Koukotsukan): Developer

## Week 8:

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/76979429?s=48&amp;v=4" alt="@yyLeaves" class=" avatar-user" width="24" height="24"> @yyLeaves:

In order to process the articles later, I suppose to prepare a word list about positive and negative words

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/76979429?s=48&amp;v=4" alt="@yyLeaves" class=" avatar-user" width="24" height="24"> @yyLeaves:

I write the code to preprocess the negative words and positive words in a python list in module 'moon_words.py' so that it can be imported
to be used easily. 

## Week 9:

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/76979429?s=48&amp;v=4" alt="@yyLeaves" class=" avatar-user" width="24" height="24"> @yyLeaves:

Question 1 should be a multiple string match problem. I googled the problem, and found that aho-corasick algorithm can
satisfy the problem. AC algorithm is the combination of KMP and Trie structure. It has linear time complexity in
matching. We can store the Trie structure in previous, and save it in a pickle file for future use, so that it saves the
preprocess time.

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/49346779?s=48&amp;v=4" alt="@Koukotsukan" class=" avatar-user" width="24" height="24"> @Koukotsukan:

Using Trie, search complexities can be brought to optimal limit. Unlike a binary search tree, nodes in the trie do not 
store their associated key. Instead, a node's position in the trie defines the key with which it is associated. 

## Week 10:

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/76979429?s=48&amp;v=4" alt="@yyLeaves" class=" avatar-user" width="24" height="24"> @yyLeaves:

I implemented the AC algorithm, but there is a problem. The algorithm match all the existing patterns based on
characters instead of words. For example, in string 'apple tree' and pattern 'app', 'apple', the result will return
the 'app' and 'apple' together, and that is definately not what we want. Maybe Trie structure is simply what we want. We
can add the word's sentiment in trie node self.sentiment, in doing so, we can store all positive words and negative
words in one trie structure.

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/49346779?s=48&amp;v=4" alt="@Koukotsukan" class=" avatar-user" width="24" height="24"> @Koukotsukan):

For the graph for the results of our sentimental analysis, I was asked to use a visualization tool named plotly. I find 
it can run in 2 modes, which are online and offline. For our project, it is more convinient to run it in offline mode.

## Week 11:

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/76979429?s=48&amp;v=4" alt="@yyLeaves" class=" avatar-user" width="24" height="24"> @yyLeaves:

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
positive words - negative words) / (neutral words) * 100 to calculate the score

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/49346779?s=48&amp;v=4" alt="@Koukotsukan" class=" avatar-user" width="24" height="24"> @Koukotsukan:

In order to visualize the results of the sentimental analysis, I need to pass country names and their corresponding 
results about positive, negative, neutral and stop words from the results dict to plotly function so the result can be 
seen in a visual way, so I use oop knowledge to create a Graph object, which can store all the attributes of the results
of different countries. and Also, I make a score-rank bar graph to show the score of each country in ascending order. 
This part is implemented by using plotly package, which is an efficient tool to draw graphs, and numpy, which is used to 
sort the array and transpose the matrix. 

## Week 13:

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/76979429?s=48&amp;v=4" alt="@yyLeaves" class=" avatar-user" width="24" height="24"> @yyLeaves:

I add pick country method to let user pick top 5 countries, and I update articles for the top 5 countries.

<img style="border-radius:50% !important;" src="https://avatars.githubusercontent.com/u/49346779?s=48&amp;v=4" alt="@Koukotsukan" class=" avatar-user" width="24" height="24"> @Koukotsukan:

@yyLeaves update her code to pass parameters in a better way, so I decide to abort using oop for the graph.py to make the code more concise.
