class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """takes in parameters and makes two instance variables"""
        self.start = self.init_number = start

    def generate(self):
        """returns an incremented number"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """resets start value to initial value"""
        self.start = self.init_number

    #add __repr__(self):

