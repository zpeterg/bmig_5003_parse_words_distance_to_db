# Design

# Design reasoning
I intentionally kept the words in a single database along with their distance and their count. This was for 2 reasons:
- Little Benefit: Since words are not much longer than integers would be (depending on length), there is little advantage in space-savings.
- Faster: 
    - Because it avoids a massive JOIN between the words and the word locations, the speed should be much greater in a single table.
    - Additionally, it would have required more processing (and possibly multiple calls to the DB) to store each word in one table (if it didn't exist), and then store the distances in a separate table.
- Ease-of-use: Splitting the words, distances and counts between tables would have made it unnecessarily complex to run unit-tests and retrieve the actual list.


# Design
## Entry points
- index.py
- read.py

## Index.py
- Has a dealArgs() function that pulls out the command-line arguments via a class.
- The results are extracted as a dictionary Options.
- Calls a Filter class and then extracts a function from it called Filter().
The function is then passed into the GetFile() function. 
- The GetFile() shatters the in-coming document into words, and then keeps or discards (or stops running completely) based on what that Filter function returns when it is called on each word.
    - This allowed 2 things:
        - I could re-use the GetFile() (as I do elsewhere) to get completely different results by just passing a different Filter() to it.
        - It also filters everything up-front so there is as little a load as possible running through the rest of the program. For example, as soon as the "halt" word is reached, the rest of the file is not even accessed and the program moves on.
- Then index.py takes that list as Words, passes it to a GetPairs() function that organizes it into a format that the database will want.
    - The words are paired-off and stored in a list along with distance from each other.
    - They are added both forward and backward (eg., word1-word2-distance and word2-word1-distance).
    This allows easy and fast insertion and retrieval from the database.
- The word-pairs are passed to Add_Words(), which simply stores them into the database as Word-Word2-Position.
    - Two notes on that:
        - I used a Word-Word2-Position table column structure because I expect to need it in the next assignment.
        - The entire list of paired-words is stored in one database command to maximize speed (though, of course, limited by memory if it were really huge). 

## Read.py
- Has a dealArgs() function that pulls out the word argument (if there is one).
- Calls GetWord() or GetWords() (depending on whether a word argument was passed) and returns a list of words.
    - Two notes:
        - To speed export, it uses SQLite to do the counting - eg., it takes the inputted word, looks up all occurrences and gets the count of them. That way the list of all occurrences never leaves SQLite and hopefully it moves faster.
        If no word is passed, it just exports all the words (grouped and counted).
- The read.py file then sends the results to a FormatToLines() function that adds spacing for presentation.

