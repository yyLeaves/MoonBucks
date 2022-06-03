Week 8:

preprocess the negative words and positive words in a python list in module 'moon_words.py' so that it can be imported to be used easily.

write the code to preprocess the text.



Week 9:

Question 1 should be a multiple string match problem. I googled the problem, and found that aho-corasick algorithm can satisfy the problem. AC algorithm is the combination of KMP and Trie structure. It has linear time complexity in matching. We can store the Trie structure in previous, and save it in a pickle file for future use, so that it saves the preprocess time.



Week 10

I implemented the AC algorithm, but there is a problem. The algorithm match all the existing patterns based on characters instead of words. For example, in string 'apple tree' and pattern 'app', 'apple', the result will return the 'app' and 'apple' together, and that is definately not what we want. Maybe Trie structure is simply what we want. We can add the word's sentiment in trie node self.sentiment, in doing so, we can store all positive words and negative words in one trie structure.



Week 11