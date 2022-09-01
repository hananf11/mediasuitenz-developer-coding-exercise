"""Helper functions for working with markdown."""
from io import TextIOWrapper
from collections import Counter
import re

STOP_WORDS = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]

def read_markdown_meta_data(file: TextIOWrapper):
    """This takes a markdown file and reads the meta-data off the top of the file.
    It will leave the file position set to after the meta-data block, 
    so then an html render can be used.
    """
    meta = {}

    current_line = file.readline().strip()
    # check if the file begins with the opening symbol
    if current_line == "===":  
        # consume and process the next lines until the break symbol is found
        found_end = False
        while not found_end:
            current_line = file.readline().strip()
            if current_line == "===":
                found_end = True
            else:
                # otherwise this is part of the metadata in the format Key: Value
                key, value = current_line.split(": ")
                meta[key.lower()] = value
    else:
        # oops it wasn't a opening ===
        # seek back to the start of the file.
        file.seek(0)
    return meta

def read_markdown_tags(file: TextIOWrapper, revert_position=False):
    """This takes a markdown file and returns the tags from that file. 
    If revert_position is True the file position will be reverted to the 
    position it was when passed into this function. """
    if revert_position:
        # save the file position for later.
        initial_position = file.tell()
    
    # read and lower all words because 'This' should be the same as 'this'
    words = file.read().lower()
    # remove all non alpha characters excluding space, \n, and "'" (because you'd won't ...)
    words = re.sub(r"[^a-z'\s]", "", words)
    words_split = words.split()
    # use Counter to count the number of duplicates in the list
    word_count = Counter(words_split)
    for stop_word in STOP_WORDS:
        del word_count[stop_word]

    # most_common_5 = word_count.most_common(5)
    # originally I was using word_count.most_common(5) but this doesn't sort alphabetically and by the count.
    # so i am sorted with a key function, word_count.items() => [(word, count), ...]
    most_common_5 = sorted(
        word_count.items(),
        key=lambda item: (-item[1], item[0])  # sort the count descending and the word ascending 
    )[:5] # first 5 only

    tags = [word for word, count in most_common_5]
    
    if revert_position:
        file.seek(initial_position)
    return tags

