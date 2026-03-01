import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 2589 보물섬
N, M = map(int, input().split())
treasure = [list(input().strip()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[0] * M for _ in range(N)]

distance = 0
min_distance = 10000

def bfs(y, x):
    global distance
    dq = deque([(y, x)])
    visited[y][x] = 1

    while dq:
        now_y, now_x = dq.popleft()
        for k in range(4):
            ny = now_y + dx[k]
            nx = now_x + dy[k]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if not visited[ny][nx] and treasure[ny][nx] == 'L':
                visited[ny][nx] = 1
                distance += 1
                dq.append([ny, nx])

for y in range(N):
    for x in range(M):
        distance = 0
        if not visited[y][x] and treasure[y][x] == 'L':
            bfs(y, x)           
            # print(distance)
            min_distance = min(distance, min_distance)

print(min_distance)