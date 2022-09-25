from hilo import Hilo
# from hilo file import the class Hilo


class Hilo_Director():  # director of the game

    def __init__(self):  # initialised function, constractor code of the Hilo_Director class
        self.card = 0
        self.playing = True
        self.outcome = 300
        # parameters assigned to the director of the game (object)

        for i in range(1, 14):  # allows director to loop through series of numbers between 1 and 14
            i = self.card
            hilo = Hilo()  # variable for the imported Hilo class
            # shows the card randomly picked between 1 to 13
            print(f"Your card is: {self.card}")

    def start_game(self):  # function to start playing the game and still under the Hilo_Director

        while self.playing:  # allows us to loop through the block of code as long the playing condition is True
            self.user_guess()  # detects input that happend since the last iteration
            self.add_points()
            self.keep_playing()
            # methods assigned to the game loop

    def user_guess(self):  # function to allow the user to guess
        # player guesses if the next card is higher or lower
        guess = input("Guess if next card will be higher or lower: [h/l]")
        if guess == 'h':
            guess = self.playing
            score.outcome += 100
        elif guess == 'l':
            guess = self.playing
        else:
            self.playing = False
        # if the user correctly guesses high or low they continue playing
        # the result of the is stored as boolean value in the playing attribute

    def add_points(self):

        while self.playing:
            self.outcome += Hilo.points  # add 100points  or subtract 75 points
           

        # displays of the card number picked
        print(f"You picked {self.card}")
        # shows the calculated total of points
        print(f" Your points are {self.outcome}")

    # if a player had more than 0 points they decide if they want to keep playing or not.
    def keep_playing(self):
        while self.outcome > 0:
            play = input("Do you want to keep playing: [yes/ no]")
            if play == "yes":
                play = self.playing
            else:
                play != self.playing
                print("Game Over")
