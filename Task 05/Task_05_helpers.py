from typing import List, Optional, Tuple

"""
This function finds the path of a given word in a 2D board of letters using depth-first search (DFS).
If interested, you can explore DFS further here: https://www.youtube.com/watch?v=by93qH4ACxo

Parameters:
board (list of list of str): The 2D board of letters. Each item represents a letter in the board.
word (str): The word to find in the board.

Returns:
list of tuple or None: A list of tuples representing the coordinates (row, column) of the letters in the word's path.
If the word is not found in the board, the function returns None.
"""


def get_word_path(board: List[List[str]], word: str) -> Optional[List[Tuple[int, int]]]:
    directions = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1)]

    def dfs(board, word, i, j, index, visited, path):

        if index == len(word):
            return path[:]  # Return a copy of the current path

        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or
                word[index] != board[i][j] or visited[i][j]):
            return None

        visited[i][j] = True
        path.append((i, j))

        for di, dj in directions:
            ni, nj = i + di, j + dj
            result = dfs(board, word, ni, nj, index + 1, visited, path)
            if result:
                return result

        # Backtrack
        visited[i][j] = False
        path.pop()
        return None

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                visited = [[False] * len(board[0]) for _ in range(len(board))]
                path = dfs(board, word, i, j, 0, visited, [])
                if path:
                    return path

    return None


"""
Prints a 2D board of letters in a formatted manner.

Parameters:
board (List[List[str]]): The 2D board of letters. Each item represents a letter in the board.

Returns:
None: The function does not return any value. It instead prints the board to the console.
"""


def print_board(board: List[List[str]]) -> None:
    for row in board:
        print()
        print("  ".join(row))
    print()
