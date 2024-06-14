"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary.

    >>> wf = WordFinder("words.txt")
    # words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'

    """

    def __init__(self, file_path):
        """

        Read words from file & evaluate # of words that are read

        """

        self.words = []
        self.read_words(file_path)

    def read_words(self, file_path):
        """

        Read words from the file and store them in self.words

        """

        file = open(file_path, 'r')
        for eachline in file:
            word = eachline.strip()
            self.words.append(word)
        file.close()

        num_words = len(self.words)
        print (f'{num_words} words read')

    def random(self):
        """
        Returns a random word from list of words

        - str: random word

        """

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """

    Read words from special_words file, filter out comments and blank lines,
    and store valid words in self.words using the superclass method.

    Args:
        - file_path (str): Path to the file containing words, one per line.

    Returns:
        - str: A string indicating the number of valid words read.

    """

    def read_words(self, file_path):
        super().read_words(file_path)
        self.words = [word for word in self.words
        if word.strip() and not word.startswith('#') ]


