import pandas as pd

def main():
    GamePicker.setup()
    # get data

class GamePicker():
    
    def __init__(self):
        self.data = pd.read_csv("bgg_dataset.csv")
        self.games_available = []
        self.age = 0
        self.difficulty = 0
        self.play_time = 0
        self.player_count = 0
        self.rating = 0

    def setup(self):    
        # get input from user
        print("Please enter the following values. If one value doesn't matter to you, leave it blank and press enter. ")
        self.age = int(input(print("How old is the youngest person playing? ")))
        self.difficulty = float(input(print("How difficult do you want it to be (1-10)? ")))
        self.play_time = int(input(print("Approximately how much time do you want it to take (in minutes)? ")))
        self.player_count = int(input(print("How many people will be playing? ")))
        self.rating = int(input(print("How high do you want it to be rated by users (1-10)? ")))
        print("Finding games that fit...")


    def check_games(self):
        for i in self.data:
            if (self.get_age(i)):
                if self.get_difficulty(i):
                    if self.get_play_time(i):
                        if self.get_player_count(i):
                            if self.get_rating(i):
                                # print info
                                pass


    # function for each category
    def get_age(self, i):
        if i['age_column'] <= self.age():
            return True
    
    def get_difficulty(self, i):
        pass

    def get_play_time(self, i):
        pass

    def get_player_count(self, i):
        pass

    def get_rating(self, i):
        pass

if __name__() == "__main__":
    main()
