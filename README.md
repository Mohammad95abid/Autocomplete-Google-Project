# Autocomplete-Google-Project

Sentence auto-complete project in cooperation with Google.
We received more than 1.5 million lines of text in our dataset, the goal was to develop an Autocomplete Console Application of sentences that would be typed by users. 
We've encountered a lot of challenges:
1. How to upload this large amount of data into the ram and we achieved that using trie tree.
2. The process of building the Trie tree for all the data would require more than 12 GB, t
    herefore we were required to divide the dataset to more datasets according to the first character in the sentence, 
    the allowed characters just lowercase letters and one digits (0-9)
