
def formatToLines(arr, targetCol=2):
    targetLen = 17
    rtn = []
    onLine = 0
    onCol = 0
    for row in arr:
        for word in row:
            word = str(word)
            wordLen = len(word)
            # if line doesn't exist yet in return, add it
            if onLine > (len(rtn) - 1):
                rtn.append('')
            # create padding string of spaces
            padding = ' ' * (targetLen - wordLen)
            # add padding and push to array
            rtn[onLine] += f'{word}{padding}'
            # move to next column
            onCol += 1
            # If maxed-out on lines, start new line
            if onCol >= targetCol:
                onCol = 0
                onLine += 1
    return rtn
