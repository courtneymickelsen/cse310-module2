import pandas as pd

def main():
    # instatiate the class
    gp = GamePicker()

    # start the program
    gp.setup()
    gp.check_games()

class GamePicker():

    def __init__(self):
        # get data
        self.data = pd.read_csv("cse310-module2/bgg_dataset.csv", decimal='.')

        # variables for user preferences
        self.age = 0
        self.play_time = 9999
        self.player_count = 4
        self.rating = 0
        self.complexity = 0

        # keep the complexity close to their entry
        self.complexity_high = self.complexity + 1

        # column index values
        self.name_i = 'name'
        self.age_i = 'min_age'
        self.min_players_i = 'min_players'
        self.max_players_i = 'max_players'
        self.play_time_i = 'play_time'
        self.rating_i = 'user_rating'
        self.complexity_i = 'complexity'

    # sets up the program by collecting all parameters for filtering the data
    def setup(self):    
        
        # display for user
        print("\n\n=========================================\n\n")
        print('\t~ BOARD GAME SELECTOR ~\n')
        print("Please enter the following values: ")
        
        # get input from user
        self.age = int(input("How old is the youngest person playing? "))
        self.play_time = int(input("How much time do you have (in minutes)? "))
        self.player_count = int(input("How many people want to play? "))
        self.rating = float(input("What's the lowest user rating you would be okay with (1-10)? "))
        self.complexity = float(input("How complex do you want it to be? "))
        print('\n\n')

    # filters the data to find matches for the users preferences
    def check_games(self):

        # filters for each category- data column at category index compared to user input
        self.age_filt = self.data[self.age_i] <= self.age
        self.play_time_filt = self.data[self.play_time_i] <= self.play_time
        self.max_player_filt = self.data[self.max_players_i] >= self.player_count
        self.min_player_filt = self.data[self.min_players_i] <= self.player_count
        self.rating_filt = self.data[self.rating_i] >= self.rating

        # two filters for complexity to keep it close above and below
        self.complexity_high_filt = self.data[self.complexity_i] >= (self.complexity - 0.1)
        self.complexity_low_filt = (self.data[self.complexity_i] <= self.complexity_high)
        
        # apply filters to dataframe
        games_available = self.data[self.age_filt & self.play_time_filt & self.max_player_filt & self.min_player_filt & self.rating_filt & self.complexity_high_filt]

        # choose which columns to display
        display_info = games_available[['name', 'min_players', 'max_players', 'user_rating', 'play_time', 'complexity']]

        # print user's top 5 game recommendations and their info
        print('Top 5 Recommendations:\n\n')
        print(display_info.head())
        print("\n\n=========================================\n\n")

if __name__ == '__main__':
    main()