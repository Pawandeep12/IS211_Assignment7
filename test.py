import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_to_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def __str__(self):
        return f"{self.name}: {self.score} points"


class Die:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.die = Die()
        self.turn_total = 0
        self.current_player = 0

    def switch_player(self):
        """Switch to the next player."""
        self.current_player = 1 - self.current_player

    def play_turn(self):
        """Handle a single turn for the current player."""
        player = self.players[self.current_player]
        self.turn_total = 0

        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled: {roll}")

            if roll == 1:
                print(f"{player.name} rolled a 1! No points added. Turn over.")
                self.turn_total = 0
                self.switch_player()
                break
            else:
                self.turn_total += roll
                print(f"Turn total: {self.turn_total}, Total score: {player.score}")

                decision = input(f"{player.name}, roll again (r) or hold (h)? ").lower()
                
                if decision == 'h':
                    player.add_to_score(self.turn_total)
                    print(f"{player.name}'s total score: {player.score}")
                    self.switch_player()
                    break

    def is_winner(self):
        """Check if any player has won the game by reaching 100 or more points."""
        return any(player.score >= 100 for player in self.players)

    def start_game(self):
        """Start and run the game until one player wins."""
        print("Welcome to the game of Pig!")

        while not self.is_winner():
            self.play_turn()

        winner = max(self.players, key=lambda p: p.score)
        print(f"Congratulations {winner.name}, you won with a score of {winner.score}!")


if __name__ == "__main__":
    random.seed(0)  # Ensures the random rolls are consistent for testing

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    game = Game(player1, player2)
    game.start_game()
