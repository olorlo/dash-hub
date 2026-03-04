import sys
# sys.stdin = open("python/input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 1916번 최소비용 구하기
def bfs(s):
    dq = deque([a])
    visited[s] = 0
    prev_visited = 1000000
    while dq:
        now = dq.popleft()
             
        for next, weight in graph[now]:
            
            if visited[next]:
                prev_visited = visited[next]
            visited[next] = min(prev_visited, (visited[now] + weight))

            dq.append(next)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)] 
visited = [0] * (N+1)

for _ in range(M):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))

a, b = map(int,input().split())

bfs(a)

print(visited[b])