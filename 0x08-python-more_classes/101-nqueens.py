#!/usr/bin/python3
"""
A module to solve the N queens challenge
"""

result = []


def isvalid(board, row, col):
    # check left side
    for col_prev in range(col):
        if board[row][col_prev] == 1:
            return False

    # check left upper diagonal
    row_dig = row
    col_dig = col
    while row_dig >= 0 and col_dig >= 0:
        if (board[row_dig][col_dig] == 1):
            return False
        row_dig -= 1
        col_dig -= 1

    # check left lower diagonal
    row_dig = row
    col_dig = col
    while col_dig >= 0 and row_dig < len(board):
        if (board[row_dig][col_dig] == 1):
            return False
        row_dig += 1
        col_dig -= 1

    return True


def solve(board, col):
    # base case
    if (col == len(board)):  # column exceeding the board, so let's stop
        path = []  # store the taken path
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 1:
                    path.append([row, col])
        result.append(path)
        return True

    # trying this column to find the best row
    flag = False
    for row in range(len(board)):
        if (isvalid(board, row, col)):
            board[row][col] = 1  # put forwards
            # search for valid row position in the next column
            flag = solve(board, col+1) or flag
            board[row][col] = 0  # remove backwards

    return flag


def main():
    import sys

    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for i in range(n)]
             for j in range(n)]

    solve(board, 0)  # start from left most column
    for solution in result:
        print(solution)


if __name__ == "__main__":
    main()
