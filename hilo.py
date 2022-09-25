import random


class Hilo():

    def __init__(self):  # constructor funtion of the Hilo class
        self.cardNum = 0
        
        # cardNum, points and guessing are instance attribute that is accessible in the scope of this object

    def guess(self):  # If the user guess the randomly picked card correctly, they get 100 but if they guess the card incorrectly they are deducted 75 points
        self.cardNum = random.randint(1, 14)
        