from utils import cleanWord


class Filter:
    """
    A class that receives arguments, and then provides a call-back function that filters each word
    """
    def __init__(self, options):
        self.start = options['start'].lower()
        self.stop = options['stop'].lower()
        self.finish = options['finish'].lower()
        self.recording = False

    def filter(self, word):
        """
        Take one word and returns None, the word, or an empty string, depending on the arguments provided above.
        Used as a call-back in getFile().
        """
        word = cleanWord(word)
        # Only DON'T record the start word if not already recording
        if word == self.finish:
            self.recording = False
            # None is the flag to stop the file-read
            return None
        if word == self.start and not self.recording:
            self.recording = True
            return ''
        elif word == self.stop:
            self.recording = False
        if self.recording:
            return word
        # Blank-string does not get saved in file-read
        return ''

