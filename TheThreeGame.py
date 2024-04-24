# Author: Heather Bullard
# Date Began: 12/2/2021
# Description: TheThreeGame that allows two players to play a game in which they alternately choose numbers from 1-9.
# They may not choose a number that has already been selected by either player. If at any point exactly three of a
# player's numbers sum to exactly 15, then that player has won. If all numbers from 1-9 are chosen, but neither player
# has won, then the game ends in a draw. Player "first_player" has the first turn.

class TheThreeGame:
    """
    Two players alternating choose numbers 1 to 9, a number can not be chosen twice
    If 3 of the players numbers sum to exactly 15, then the player wins
    If all numbers 1 to 9 are chosen and neither has won, then the game is a draw.
    Player first_player goes first
    """

    def __init__(self):
        """
        The constructor for TheThreeGame class.
        Initializes the private data members.
        first_nums and second_nums keeps a set of each players chosen numbers
        the current state holds one of four values
        Player keeps track of whose turn it is
        Takes no parameters.
                """
        self._turn = 0                      # keeps track of which players turn
        self._total_chosen = ["-", "n", "n", "n", "n", "n", "n", "n", "n", "n"]       # keeps the numbers that are chosen by everyone 1-9
        self._current_state = "GAME UNFINISHED"
        self._newNum = 0

    def validate(self):
        """
        Validates the number has not been previously chosen, the has not been won or drawn,
        Makes sure the number is within the valid range
        :return False:
        """
        if self._total_chosen[self._newNum] != "n" and 1 > self._newNum > 9:
            return print("wrong number") and False
        if self._current_state == "FIRST_PLAYER_WON" or self._current_state == "SECOND_PLAYER_WON" or self._current_state == "IT_IS_A_DRAW":
            return print(self._current_state) and False

    def check_sum(self):
        """
        Checks if there are three numbers chosen by the same player, which
        Equal 15 , if so updates current state
        :return:
        """
        player1, player2 = "f", "s"
        difference = 15 - self._newNum
        half1, half2 = (difference // 2) + 1, (difference // 2) - 1
        if difference % 2 == 1:
            half2 += 1
        if self._total_chosen[self._newNum] == player1 and self._total_chosen[half1] == player1 and self._total_chosen[half2] == player1:
            self._current_state = "FIRST_PLAYER_WON"

        elif self._total_chosen[self._newNum] == player2 and self._total_chosen[half1] == player2 and self._total_chosen[half2] == player2:
            self._current_state = "SECOND_PLAYER_WON"

    def get_winner(self):                       # returns the current value of the winner
        """
        When a player reaches the sum of 15 with 3 distinct number turns, a winner is declared.
        The method will return which player won the game.
        For instance, FIRST_PLAYER_WON, SECOND_PLAYER_WON, or None
        """
        if self._current_state == "FIRST_PLAYER_WON":
            return self._current_state
        elif self._current_state == "SECOND_PLAYER_WON":
            return self._current_state
        else:
            return None


    def is_it_a_draw(self):
        """
        Two players will exhaust all the available numbers and a draw is called, 'IT_IS_A_DRAW'
        If not a draw, it will return 'GAME_UNFINISHED' If a player has won and is_it_a_draw
        is called, then it should return "FIRST_PLAYER_WON" or "SECOND_PLAYER_WON" accordingly.
        """
        TheThreeGame.validate(self)
        if self._turn == 9:
            if self.get_winner() is None:
                self._current_state = "IT_IS_A_DRAW"
                return self._current_state
            if self.get_winner() == "FIRST_PLAYER_WON" or self.get_winner() == "SECOND_PLAYER_WON":
                return self.get_winner()
        else:
            self._current_state = "GAME_UNFINISHED"
            return self._current_state

    def make_move(self, active_player, chosen_number):
        """
        Each player takes a turn choosing numbers 1 to 9. Each number can not be chosen previously.
        Player: a string designating the player making the move, either "first_player" or "second_player",
        and an integer giving their number choice (in that order)
        Chosen_number: The parameter chosen_number will be the input each player chooses to continue the game.
        Return False: Only valid number are allowed, if it is not that player's turn, or if the integer is not
        in the correct range, or if that integer has already been chosen, or if the game has already been won or drawn.
        """
        if self._turn % 2 == 0 and active_player == "second_player":
            return print("wrong player") and False
        self._newNum = chosen_number
        TheThreeGame.validate(self)
        self._total_chosen[self._newNum] = active_player[0]
        TheThreeGame.check_sum(self)

        if self._current_state == "FIRST_PLAYER_WON" or self._current_state == "SECOND_PLAYER_WON":
            return print("game over") and self._current_state and False
        self._turn += 1
        if self._turn == 10:
            self._current_state = "IT_IS_A_DRAW"
            return self._current_state
        return print("Successful Turn, Next Player") and True


game = TheThreeGame()

game.make_move("first_player", 6)
game.make_move("second_player", 5)
result = game.make_move("first_player", 7)
player_won = game.get_winner()
draw = game.is_it_a_draw()
