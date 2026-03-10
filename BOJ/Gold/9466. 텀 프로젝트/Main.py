import sys
# sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque

# 백준 9466번 텀 프로젝트
T = int(input())

def dfs(node):
    visited = [0] * (n+1)
    stack.append(node)

    while stack:
        now = stack.pop()
        
        next=students[now]

        if visited[next]:
            return now

        visited[next] = 1
        stack.append(next)


for _ in range(T):
    n = int(input())

    a = list(map(int, input().split()))
    visited = [0] * (n+1)
    students = [0, *a]

    # dfs 돌려서 내 자신이 나오면 팀에 속한거임
    stack = []
    cnt = 0

    for start in range(1,n+1):
        if dfs(start) == start:
            continue
        else:
            cnt += 1

    print(cnt)