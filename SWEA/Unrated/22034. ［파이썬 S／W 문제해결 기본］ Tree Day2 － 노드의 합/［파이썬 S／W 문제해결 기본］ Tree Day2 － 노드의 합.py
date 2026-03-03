# swea Tree Day2 = 노드의 합

T = int(input())

for tc in range(1, T+1):
    N, M ,L = map(int, input().split())
    graph = [0]* (N+1)

    for _ in range(M):
        leaf, n = map(int, input().split())
        graph[leaf] = n

    # 역순으로 올라가면서
    # 자기 값을 부모에게 더해주기
    for i in range(N, 1, -1):

        graph[i//2] += graph[i] 

    print(f'#{tc} {graph[L]}')