class Game:
    def __init__(self, title):
        self.title = title
        self._results = []

    def results(self):
        return self._results

    def players(self):
        return list(set(result.player for result in self._results))

    def average_score(self, player):
        player_results = [result.score for result in self._results if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        else:
            return 0

class Player:
    def __init__(self, username):
        self.username = username
        self._results = []

    def results(self):
        return self._results

    def games_played(self):
        return list(set(result.game for result in self._results))

    def played_game(self, game):
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        return sum(result.game == game for result in self._results)

class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        player.results().append(self)
        game.results().append(self)
