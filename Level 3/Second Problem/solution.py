from collections import deque

def shortest_path(sx, sy, maze):
    # Initialize the dimensions of the maze
    w = len(maze[0])
    h = len(maze)

    # Create a 2D array to store the shortest path lengths from the starting point
    board = [[None for i in range(w)] for i in range(h)]
    board[sx][sy] = 1  # Mark the starting point

    arr = [(sx, sy)]  # Initialize a queue for BFS starting with the starting point
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] is None:
                    board[nx][ny] = board[x][y] + 1
                    if maze[nx][ny] == 1:
                        continue
                    arr.append((nx, ny))  # Add valid neighbors to the queue

    return board

def solution(maze):
    # Get the dimensions of the maze
    w = len(maze[0])
    h = len(maze)

    # Find the shortest paths from the top-left and bottom-right corners
    tb = shortest_path(0, 0, maze)
    bt = shortest_path(h - 1, w - 1, maze)

    ans = 2 ** 32 - 1  # Initialize the answer to a large value
    for i in range(h):
        for j in range(w):
            if tb[i][j] and bt[i][j]:
                ans = min(tb[i][j] + bt[i][j] - 1, ans)  # Calculate the minimum path length

    return ans

# # Test cases
# maze1 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]  # Answer 11
# maze2 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]  # Answer 7
# maze3 = [[0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0]]  # Answer 7
# maze4 = [[0, 1, 1, 1], [0, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0]]  # Answer 7

# # Print the results for the test cases
# print(solution(maze1))
# print(solution(maze2))
# print(solution(maze3))
# print(solution(maze4))
