"""
Tic Tac Toe Game
"""
import copy
import math


class TicTacToe:

    def __init__(self):
        self.X_Player = "X"
        self.O_Player = "O"
        self.Empty = None

    def initial_state(self):
        """
        Returns starting state of the game
        :return:
        """
        return [[self.Empty, self.Empty, self.Empty], [self.Empty, self.Empty, self.Empty],
                [self.Empty, self.Empty, self.Empty]]

    def player(self, board):
        """
        Returns the player who has the next turn on the board
        :param board:
        :return:
        """
        xs = 0
        os = 0

        for x in board:
            for y in x:
                if y == self.X_Player:
                    xs += 1
                elif y == self.O_Player:
                    os += 1

        if xs <= os:
            return self.X_Player
        else:
            return self.O_Player

    def actions(self, board):
        """
        Returns all the possible actions available (i, j) on the board
        :param board:
        :return:
        """
        possible_actions = set()
        for x, x_axis in enumerate(board):
            for y, y_axis in enumerate(x_axis):
                if y_axis == self.Empty:
                    possible_actions.add((x, y))
        return possible_actions

    def result(self, board, action):
        """
        Returns the resulted board after the move (i, j) performed by the player on the board
        :param board:
        :param action:
        :return:
        """
        if len(action) != 2:
            raise Exception("result function - incorrect move")

        if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[0] > 2:
            raise Exception("result function - incorrect move by player")

        x, y = action[0], action[1]

        board_copy = copy.deepcopy(board)

        if board_copy[x][y] != self.Empty:
            raise Exception("suggested action already taken")
        else:
            board_copy[x][y] = self.player(board)

        return board_copy

    def winner(self, board):
        """
        Returns the winner of the game if there is one
        :param board:
        :return:
        """
        for x in range(3):
            # Check horizontal lines
            if (board[x][0] == board[x][1] == board[x][2]) and (board[x][0] != self.Empty):
                return board[x][0]
            # Check vertical lines
            if (board[0][x] == board[1][x] == board[2][x]) and (board[0][x] != self.Empty):
                return board[0][x]

        # Check diagonals
        if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and board[1][
            1] != self.Empty:
            return board[1][1]

        return None

    def terminal(self, board):
        """
        Returns True if game is over else False
        :param board:
        :return:
        """
        if self.winner(board) is not None:
            return True
        elif self.Empty not in board[0] and self.Empty not in board[1] and self.Empty not in board[2]:
            return True
        else:
            return False

    def utility(self, board):
        """
        Returns 1 if X_Player is the winner else if returns -1 if O_Player is the winner else returns 0 if it's a
        tie/draw.
        :param board:
        :return:
        """
        if self.winner(board) == self.X_Player:
            return 1
        elif self.winner(board) == self.O_Player:
            return -1
        else:
            return 0

    def minimax(self, board):
        """
        Returns the optimal action for the current player on the board
        :param board:
        :return:
        """
        if self.terminal(board):
            return None

        if self.player(board) == self.X_Player:
            score = -math.inf
            action_to_take = None

            for action in self.actions(board):
                min_value = self.minvalue(self.result(board, action))

                if min_value > score:
                    score = min_value
                    action_to_take = action

            return action_to_take

        elif self.player(board) == self.O_Player:
            score = math.inf
            action_to_take = None

            for action in self.actions(board):
                max_value = self.maxvalue(self.result(board, action))

                if max_value < score:
                    score = max_value
                    action_to_take = action

            return action_to_take

    def minvalue(self, board):
        """
        Returns minimum value out of all the maximum values
        :param board:
        :return:
        """
        if self.terminal(board):
            return self.utility(board)

        max_value = math.inf
        for action in self.actions(board):
            max_value = min(max_value, self.maxvalue(self.result(board, action)))

        return max_value

    def maxvalue(self, board):
        """
        Returns maximum value out of all the minimum value
        :param board:
        :return:
        """
        if self.terminal(board):
            return self.utility(board)

        min_value = -math.inf
        for action in self.actions(board):
            min_value = max(min_value, self.minvalue(self.result(board, action)))

        return min_value
