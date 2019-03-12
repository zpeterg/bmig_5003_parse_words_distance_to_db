
def getFile(filename, on_word):
    rtn = []
    with open(filename, 'r') as file:
        # append each line with a space
        for line in file:
            for word in line.split(' '):
                new_word = on_word(word)
                # If is signaled with "none" to break, break the whole function
                if new_word is None:
                    return rtn
                # If not breaking, and not empty, add it
                if new_word != '':
                    rtn.append(on_word(word))
    return rtn
