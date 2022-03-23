class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_address):
        self.file_address = file_address
        self.word_list = self.open_and_read_file()
        print(self.words_read())



#opening up the file 
    def open_and_read_file(self):
        return open(self.file_address).readlines() #returns array
        
        

    def words_read(self):
        return f"{len(self.word_list)} words read"

    def random(self):
        from random import choice
        return choice(self.word_list).removesuffix("\n")


"""def random(self):


file = open("random_words.txt")
"""

