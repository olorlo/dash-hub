import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 백준 1068번 트리
N = int(input())

parent = list(map(int, input().split()))
child = [[] for _ in range(N)]
delete_node = int(input())

# 일단 parent를 child 리스트로 바꿈
# 전체 leaf 수를 세기
# 삭제하면 그 idx와 연결된 child와 연결된 leaf 세기
# 두개를 빼서 남은 leaf 수 세기

# parent가 값인 리스트를 child가 값인 리스트로 바꿈
for i in range(N):
    if parent[i] == -1:
        continue
    child[parent[i]].append(i)
for i in range(N):
    if not child[i]:
        child[i].append(-1) 

cnt = 0
visited = [0] * (N+1) 

def leaf(node):
    global cnt
    if child[node] == [-1]:
        cnt += 1
        return
    for next in child[node]:
        if visited[next]:
            continue
        visited[next] = 1
        leaf(next)

# 전체 leaf 수를 셈
for i in range(N):
    if not visited[i]:
        leaf(i)
total = cnt

# delete할 node와 연결된 leaf 수를 셈
cnt = 0
visited = [0] * (N+1) 
leaf(delete_node)

# 남은 leaf의 수: 전체 leaf 수 - delete된 leaf 수
print(total - cnt)