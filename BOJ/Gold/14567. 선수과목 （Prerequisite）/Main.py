import sys
# from collections import deque
# sys.stdin = open("python/input.txt", 'r')
input = sys.stdin.readline

# 백준 14567번 선수과목
def dfs(node):
    global cnt
    if not graph[node]:
        stack[node] = cnt + 1
        return
    visited[node] = 1
    for next in graph[node]:
        if visited[next]:
            continue
        cnt += 1
        dfs(next)
        stack[node] = cnt
        cnt -= 1
        visited[next] = 0

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cnt = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

stack = [1] * (N+1)
visited = [0] * (N+1)

dfs(1)
for i in range(1, N+1):
    print(stack[i], end=' ')