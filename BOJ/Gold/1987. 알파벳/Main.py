import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")

from collections import deque

# 백준 1987번 알파벳

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    global max_value
    max_value = max(max_value, len(stack))
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue

        if arr[ny][nx] in stack:
            continue
        stack.append(arr[ny][nx])
        dfs(ny, nx)
        stack.pop()

max_value = 0
stack = []
stack.append(arr[0][0])

dfs(0, 0)
print(max_value)