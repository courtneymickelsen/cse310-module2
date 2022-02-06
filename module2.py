from numpy import true_divide
import pandas as pd

def main():
    GamePicker().setup()
    # get data

class GamePicker():
    
    def __init__(self):
        self.data = None
        self.games_available = []
        self.age = 0
        self.difficulty = 0
        self.play_time = 0
        self.player_count = 0
        self.rating = 0
        self.numgames = 0

        self.name_i = 1
        self.age_i = 6
        self.min_players_i = 3
        self.max_players_i = 4
        self.play_time_i = 5
        self.rating_i = 8
        self.difficulty_i = 10

        # [ '1Name','3Min Players', '4Max Players', '5Play Time', '6Min Age', '8Rating Average', '10Complexity Average', '12Mechanics']

    def setup(self):    
        # get input from user
        print("Please enter the following values. If one value doesn't matter to you, leave it blank and press enter. ")
        self.age = int(input("How old is the youngest person playing? "))
        self.difficulty = float(input("How difficult do you want it to be (1-10)? "))
        self.play_time = int(input("How much time do you have (in minutes)? "))
        self.player_count = int(input("How many people will be playing? "))
        self.rating = int(input("What's the lowest rating you would be okay with (1-10)? "))
        print("Finding games that fit...")
        
        self.data = pd.read_csv("cse310-module2/bgg_dataset.csv", skiprows=1, decimal='.')
        self.check_games()


    def check_games(self):
        # for i in self.data:
        # print(i)
        # list = i.split(';')

        # fits_age = filter(self.get_age, self.data)
        # fits_difficulty = filter(self.get_difficulty, fits_age)
        # fits_play_time = filter(self.get_play_time, fits_difficulty)
        # fits_player_count = filter(self.get_player_count, fits_play_time)
        # fits_rating = list(filter(self.get_rating, fits_player_count))

        # games_possible = list(fits_rating)
        '''maybe add it to a new file?'''
        for i in self.data:
            list = i.split(';')

            if (self.get_age(list)):
                if self.get_difficulty(list):
                    if self.get_play_time(list):
                        if self.get_player_count(list):
                            if self.get_rating(list):
                                # print info
                                print(list[0])
                                # self.numgames += 1


    # function for each category
    def get_age(self, list):
        # list = list.split(';')
        if int(list[self.age_i]) <= self.age:
            return True
        else:
            return False
    
    def get_difficulty(self, list):
        # list = list.split(';')
        if float(list[self.difficulty_i]) <= (self.difficulty + 1):
            if int(list[self.difficulty_i]) >= (self.difficulty - 1):
                return True
        else:
            return False

    def get_play_time(self, list):
        # list = list.split(';')
        if int(list[self.play_time_i]) <= self.play_time:
            return True
        else:
            return False

    def get_player_count(self, list):
        # list = list.split(';')
        if int(list[self.max_players_i]) >= self.player_count:
            if int(list[self.min_players_i]) <= self.player_count:
                return True
        else:
            return False

    def get_rating(self, list):
        # list = list.split(';')
        if float(list[self.rating_i]) >= self.rating:
            return True
        else:
            return False

if __name__ == '__main__':
    main()
