from hilo import Hilo
# from hilo file import the class Hilo


class Hilo_Director():  # director of the game

    def __init__(self):  # initialised function, constractor code of the Hilo_Director class
        self.card = 0
        self.playing = True
        self.outcome = 300
        self.guess = None
        # parameters assigned to the director of the game (object)
        self.hilo = Hilo()  # variable for the imported Hilo class
        self.hilo.guess()

    def start_game(self):  # function to start playing the game and still under the Hilo_Director

        while self.playing:  # allows us to loop through the block of code as long the playing condition is True
            self.user_guess()  # detects input that happend since the last iteration
            self.add_points()
            self.keep_playing()
            # methods assigned to the game loop

    def user_guess(self):  # function to allow the user to guess
        # player guesses if the next card is higher or lower
        print(f"The card number is {self.hilo.cardNum}")
        self.guess = input("Guess if card picked is high or low: [h/l]")
        if self.guess.lower() == "h":
            self.playing = True
        elif self.guess.lower() == "l":
            self.playing = True
        else:
            self.playing = False
        # if the user correctly guesses high or low they continue playing
        # the result of the is stored as boolean value in the playing attribute

    def add_points(self):
        
        if self.playing:
              # add 100points  or subtract 75 points
            old_num = self.hilo.cardNum
            self.hilo.guess()
            if self.guess == "l" and old_num > self.hilo.cardNum:
                self.outcome += 100
            elif self.guess == "h" and old_num < self.hilo.cardNum:
                self.outcome += 100
            else:
                self.outcome -= 75


        # displays of the card number picked
        print(f"The card was {self.hilo.cardNum}")
        # shows the calculated total of points
        print(f" Your points are {self.outcome}")

    # if a player had more than 0 points they decide if they want to keep playing or not.
    def keep_playing(self):
        play = input("Do you want to keep playing: [yes/ no]")
        if play == "yes":
            self.playing = True
        else:
            self.playing = False
            print("Game Over")
