import sys
input = sys.stdin.readline

from collections import deque

# 백준 게리멘더링
N = int(input())
population = list(map(int, input().split()))

arr = []
for i in range(N):
    a = list(map(int,input().split()))
    arr.append([x-1 for x in a[1:]])
min_result = float('inf')

# 선거구를 2개로 나눔
def dfs(now, A):
    global min_result
    
    # 종료 조건:
    if now == N:
        if 0 < len(A) < N:
            
            # B 만들기
            B = []
            for i in range(N):
                if i not in A:
                    B.append(i)
            
            if check(A) and check(B):
                result = abs(sum(population[i] for i in A) - sum(population[i] for i in B))
                min_result = min(min_result, result)
        return 

    # 선거구 넣음
    dfs(now+1, A+[now])
    
    # 안넣음
    dfs(now+1, A)

# group 내에 구역들이 모두 이어져있는지 체크 
def check(group):
    visited = set()
    dq = deque([group[0]])
    visited.add(group[0])
    
    while dq:
        now = dq.popleft()
        for next in arr[now]:
            if next in group and next not in visited:
                visited.add(next)
                dq.append(next)
    return len(visited) == len(group)

dfs(0, [])

if min_result == float('inf'):
    min_result = -1

print(min_result)