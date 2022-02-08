import pandas as pd

def main():
    gp = GamePicker()
    gp.setup()
    gp.check_games()

class GamePicker():

    def __init__(self):
        self.data = pd.read_csv("cse310-module2/bgg_dataset.csv", decimal='.')
        self.age = 0
        self.play_time = 9999
        self.player_count = 4
        self.rating = 0
        self.complexity = 0
        self.complexity_high = self.complexity + 1

        self.name_i = 'name'
        self.age_i = 'min_age'
        self.min_players_i = 'min_players'
        self.max_players_i = 'max_players'
        self.play_time_i = 'play_time'
        self.rating_i = 'user_rating'
        self.complexity_i = 'complexity'

    def setup(self):    
        
        # display
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

    def check_games(self):
        
        # filters for each category- data column at category index compared to user input
        self.age_filt = self.data[self.age_i] <= self.age
        self.play_time_filt = self.data[self.play_time_i] <= self.play_time
        self.max_player_filt = self.data[self.max_players_i] >= self.player_count
        self.min_player_filt = self.data[self.min_players_i] <= self.player_count
        self.rating_filt = self.data[self.rating_i] >= self.rating
        self.complexity_high_filt = self.data[self.complexity_i] >= (self.complexity - 0.1)
        self.complexity_low_filt = (self.data[self.complexity_i] <= self.complexity_high)
        # self.all_filt = (self.data['min_age'] <= self.age) & (self.data[self.play_time_i] <= self.play_time) & (self.data[self.max_players_i] >= self.player_count) & (self.data[self.min_players_i] <= self.player_count) & (self.data[self.rating_i] >= self.rating) & (self.data[self.complexity_i].between(self.complexity, self.complexity_high))
        
        # apply filters to dataframe
        games_available = self.data[self.age_filt & self.play_time_filt & self.max_player_filt & self.min_player_filt & self.rating_filt & self.complexity_high_filt]
        # self.data = self.data[self.play_time_filt]
        # self.data = self.data[self.max_player_filt]
        # self.data = self.data[self.min_player_filt]
        # self.data = self.data[self.rating_filt]
        # self.data = self.data[self.complexity_filt]
        # self.data = self.data[self.age_filt]


        display_info = games_available[['name', 'min_players', 'max_players', 'user_rating', 'play_time', 'complexity']]

        # print user's top 5 game recommendations
        print('Top 5 Recommendations:\n\n')
        print(display_info.head())
        print("\n\n=========================================\n\n")

if __name__ == '__main__':
    main()