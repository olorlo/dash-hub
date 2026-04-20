import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque

# 백준 17471 게리맨더링

def dfs(idx, A):
    global min_pop

    # 종료 조건: 끝까지 갔다
    if idx == N:
        if 0 < len(A) < N:
            B = [i for i in range(N) if i not in A]
            # print('A:', A, 'B:', B)
            if check(A) and check(B):
                diff = abs(sum(population[i] for i in A) 
                           - sum(population[i] for i in B))
                min_pop = min(min_pop, diff)
        return 

    # A에 포함
    dfs(idx+1, A + [idx])

    # A에 포함 x
    dfs(idx+1, A)

def check(arr):
    # 두 선거구가 각각 연결되어있는지 확인 
    visited = set()
    dq = deque([arr[0]])
    visited.add(arr[0])

    while dq:
        now = dq.popleft()
        
        for next in graph[now]:
            if next in arr and next not in visited:
                visited.add(next)
                dq.append(next)
    return len(visited) == len(arr)
    

# 구역의 개수 N
N = int(input())

# 구역의 인구 배열
population = list(map(int, input().split()))

graph = []

for i in range(N):
    a = list(map(int, input().split()))
    graph.append([x-1 for x in a[1:]])

min_pop = float('inf')

dfs(0, [])
if min_pop == float('inf'):
    print(-1)
else:
    print(min_pop)