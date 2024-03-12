# class Game:
#     def __init__(self, title):
#         self.title = title
#         self._results = []

#     def results(self):
#         return self._results

#     def players(self):
#         return list(set(result.player for result in self._results))

#     def average_score(self, player):
#         player_results = [result.score for result in self._results if result.player == player]
#         if player_results:
#             return sum(player_results) / len(player_results)
#         else:
#             return 0

# class Player:
#     def __init__(self, username):
#         self.username = username
#         self._results = []

#     def results(self):
#         return self._results

#     def games_played(self):
#         return list(set(result.game for result in self._results))

#     def played_game(self, game):
#         return any(result.game == game for result in self._results)

#     def num_times_played(self, game):
#         return sum(result.game == game for result in self._results)

# class Result:
#     def __init__(self, player, game, score):
#         self.player = player
#         self.game = game
#         self.score = score
#         player.results().append(self)
#         game.results().append(self)

class Game:

    def __init__(self, title):
        self._title = None
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if self._title is None and isinstance(title, str) and len(title) > 0:
            self._title = title
        # else:
        #     raise Exception("Title is immutable")

    def results(self, new_result=None):
        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results

    def players(self, new_player=None):
        if new_player and isinstance(new_player, Player) and new_player not in self._players:
            self._players.append(new_player)
        return self._players

    def average_score(self, player):
        player_scores = [each_r.score for each_r in self._results if each_r.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0



class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 1 <= len(username) <= 16:
            self._username = username
        # else:
        #     raise Exception("Invalid username")

    def results(self, new_result=None):
        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        if new_game and isinstance(new_game, Game):
            if new_game not in self._games_played:
                self._games_played.append(new_game)
        return self._games_played

    def played_game(self, game):
        return game in self._games_played

    def num_times_played(self, game):
        return len([re for re in self._results if re.game == game])


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)

        # Append the current instance to the 'all' list
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score
        # else:
        #     raise Exception("Invalid score")
