
def getPairs(words, depth=4):
    """
    Pair-off the words in format [(word, word1, distance)].
    The pair is created both directions (flipping "word" and "word2") in order to ease recall of all words for "word"
    """
    rtn = []
    for i, word in enumerate(words):
        word = word.lower()
        words_len = len(words)-1
        # Store the word itself for word-count
        rtn.append((word, '', -1))
        # Store the word relative to words following it (controlled by 'depth' variable)
        for d in range(depth):
            # add next, if exists
            if i+d+1 <= words_len:
                # add forward and reverse
                rtn.append((word, words[i+d+1].lower(), d))
                rtn.append((words[i+d+1].lower(), word, d))

    return rtn
