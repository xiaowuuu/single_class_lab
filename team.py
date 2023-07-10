class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.point = 0
# add new player to the players list
    def add_player(self, new_player):
        self.players.append(new_player)
    
# check if the player in the players list
    def has_player(self, player):
        return player in self.players
            
# add 3 to the points property for a win
    def play_game(self, game_won):
        if game_won:
            self.point += 3