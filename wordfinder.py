from random import choice

class WordFinder:

    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):

        file = open(path)

        self.word_list = self.parse(file)

        print(f"{len(self.word_list)} words read")


    def parse(self, file):

       return [line.strip() for line in file]


    def random(self):

        return choice(self.word_list)


class SpecialWordFinder(WordFinder):

    def parse(self, file):

      return [word for word in super().parse(file) if word != "" and not word.startswith("#")]



