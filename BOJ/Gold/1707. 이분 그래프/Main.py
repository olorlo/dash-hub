import sys
# sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")

from collections import deque

# 백준 1707번 이분그래프

# 테스트 케이스
K = int(input())
for _ in range(K):

    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    # 그래프 입력
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 이분 그래프 확인할 집합과 스택
    set1 = set()
    set2 = set()
    stack = []

    is_bipartite = True

    # 이분그래프 만들기
    for start in range(1, V+1):
        # 이미 start 정점이 집합에 들어있으면 패스
        if start in set1 or start in set2:
            continue
        
        # 시작: start, set1에 start 넣음
        stack = [start]
        set1.add(start)

        # stack이 빌때까지 반복
        while stack:
            i = stack.pop()

            # 현재 정점과 연결된 정점
            for next in graph[i]:

                # 이 그래프가 충돌인지 확인
                if i in set1 and next in set1:
                    is_bipartite = False
                    break
                if i in set2 and next in set2:
                    is_bipartite = False
                    break
                
                # 이미 집합 속에 들어있는지 확인 (중복 방지)
                if next in set1 or next in set2:
                    continue

                stack.append(next)

                if i in set1:
                    set2.add(next)
                else:
                    set1.add(next) 

            if not is_bipartite:
                break

    if is_bipartite:
        print("YES")
    else:
        print("NO")