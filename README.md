# bmig_5003_parse_words_distance_to_db
A command-line script by Peter Granderson that loads one or more files, splits/filters them by 
word and saves them to a SQLite database.
A separate script allows output of all words (or a particular word) and the count of words and 
surrounding words up to distance of 3 intervening words.

# Design docs
See docs/ directory.

# Install
1. Setup environment: ```conda env create -f environment.yml```
2. Activate it: ```conda activate zpeterg```
3. ```git clone git@github.com:zpeterg/bmig_5003_parse_words_distance_to_db```

# Run
1. cd into the directory
2. ```python
    python index.py \
        --input=<filename> \
        <optional: "--inputs" in place of "--input" for multiple files>
        --start=<start word> \
        --stop=<stop word> \
        --finish=<finish word> \
        <optional: "-c" for clearing database prior to run>
     ```
## Examples
To record words to database:
```python index.py --input=testfiles/small_test.txt --start=foo --stop=bar --finish=enough -c```

To add another set, this time from a list of inputs:
```python index.py --inputs=testfiles/small_test_list.txt --start=foo --stop=bar --finish=enough```

# Read
1. ```python
    python read.py \
        <optional: the name of the word you want to obtain a count about>
     ```

## Examples
Read the count of a particular word from the database:
    ```python read.py cow```

Read the count of all words (ordered by descending count) from the database:
```python read.py```

The output looks like the below. Distance 'self' means that these entries are counts of word-occurrence.
```
    WORD             ASSOC            DISTANCE         COUNT
    cow                               self             2
    flight-manual                     self             1
    ...
    cow              cow              0                2
    cow              siamese          0                1
    flight-manual    milky            0                1
    flight-manual    toothpick        0                1 
    ...
```
# Run Unit Tests
```python -m unittest discover -p "*_test.py"```