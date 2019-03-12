from getFile import getFile

class dealArgs:
    # A class that filters, validates, and returns arguments
    def __init__(self, args):
        self.start = ''
        self.stop = ''
        self.finish = ''
        self.clear = False

        for a in args:
            a = a.split('=')
            if a[0] == '--input':
                # If one input go ahead with that
                self.files = [a[1]]
            elif a[0] == '--inputs':
                # If multiple inputs, go ahead and get them
                self.files = getFile(a[1], lambda x: x.strip())
            elif a[0] == '--start':
                self.start = a[1]
            elif a[0] == '--stop':
                self.stop = a[1]
            elif a[0] == '--finish':
                self.finish = a[1]

        # throw error if no input files supplied
        if not hasattr(self, 'files') or len(self.files) <= 0:
            raise ValueError('You must supply a file with --input or a list of space-separated files with --inputs')

        if '-c' in args:
            self.clear = True

    # FILE
    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, files):
        if files == '':
            raise ValueError('You must supply files')

        self.__files = files

    # STATS
    @property
    def clear(self):
        return self.__stats

    @clear.setter
    def clear(self, clear):
        if not isinstance(clear, bool):
            clear = False
        self.__stats = clear


    def to_object(self):
        """
        Returns a dictionary with each item expected
        """
        return {
            "files": self.files,
            "start": self.start,
            "stop": self.stop,
            "finish": self.finish,
            "clear": self.clear,
        }


def cleanWord(word):
    # Cleans words by making them lowercase, removing new-lines, and stripping symbols from ends of words.
    # Returns the word provided.
    word = word.lower()
    word = word.replace('\n', '')
    return word.strip("~`!@#$%^&*()_-+={[}]|\\:;\"' <,>.?/")
