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

    # 이분 그래프 확인할 집합과 스택 -> 시간초과
    # set1 = set()
    # set2 = set()
    # stack = []

    color = [0] * (V+1)

    is_bipartite = True

    # 이분그래프 만들기
    for start in range(1, V+1):
        # 이미 start 정점이 집합에 들어있으면 패스
        if color[start] != 0:
            continue
        
        stack = [start]
        # 집합 1에 넣었다고 생각
        color[start] = 1
        # set1.add(start)

        # stack이 빌때까지 반복
        while stack:
            i = stack.pop()

            # 현재 정점과 연결된 정점
            for next in graph[i]:

                # 이 그래프가 충돌인지 확인 -> 집합으로 했는데 시간초과남
                # if i in set1 and next in set1:
                #     is_bipartite = False
                #     break
                # if i in set2 and next in set2:
                #     is_bipartite = False
                #     break
                
                if color[i] == color[next]:
                    is_bipartite = False
                    break

                # 이미 집합 속에 들어있는지 확인 (중복 방지)
                if color[next] == 0:
                    color[next] -= color[i]
                    stack.append(next)

            if not is_bipartite:
                break

    if is_bipartite:
        print("YES")
    else:
        print("NO")