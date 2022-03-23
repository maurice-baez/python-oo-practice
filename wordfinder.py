class WordFinder:

    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_address):
        self.file_address = file_address
        self.word_list = self.open_and_read_file()
        self.words_read()

    def open_and_read_file(self):
        return open(self.file_address).readlines()

    def words_read(self):
        print(f"{len(self.word_list)} words read")

    def random(self):
        from random import choice
        return choice(self.word_list).removesuffix("\n")


class SpecialWordFinder(WordFinder):


    def __init__(self, file_address):
        super().__init__(file_address)
        self.word_list = self.words_list()


    def words_list(self):
       return [word for word in self.word_list if not word.startswith("#") and not word.startswith("\n")]



