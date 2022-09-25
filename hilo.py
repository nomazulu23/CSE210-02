import random


class Hilo():

    def __init__(self):  # constructor funtion of the Hilo class
        self.cardNum = 0

    def guess(self):  # The card randomly picked
        self.cardNum = random.randint(1, 14)
