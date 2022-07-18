# Handy string-manipulator functions:
import re

#Get sub-string contained within brackets in text
str_in_bracs = lambda s: re.search(r"\(([A-Za-z0-9_]+)\)", s)


# Multi-replace: Replace multiple sub-strings within a string
def mreplace(text, to_replace):
    # to_replace = dict -> {old_text : new_text, ...}
    
    # If "to_replace" passed as a list/tuple/set, remove
    # these items within the text automatically.
    if isinstance(to_replace, (list, tuple, set)): 
        to_replace = {item:'' for item in to_replace}
        
    for old, new in to_replace.items(): #Replace all substrings
        text = text.replace(old, new) #with new vals
        
    return text


# Get counts of unique sub-strings/words in a string
def word_counts(text):
    counts = {}

    for word in text.split():
        if word in counts.keys():
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
