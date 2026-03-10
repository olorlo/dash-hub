import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# 백준 1987번 알파벳

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    global max_value

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue

        if arr[ny][nx] in stack:
            continue

        if not visited[ny][nx]:
            stack.append(arr[ny][nx])
            visited[ny][nx] = visited[y][x] + 1
            result = dfs(ny, nx)
            max_value = max(result, max_value)
            visited[ny][nx] = 0
            stack.pop()
            
    return len(stack)

max_value = 0
visited = [[0]*C for _ in range(R)]
stack = []
stack.append(arr[0][0])
visited[0][0] = 1

dfs(0, 0)
print(max_value)