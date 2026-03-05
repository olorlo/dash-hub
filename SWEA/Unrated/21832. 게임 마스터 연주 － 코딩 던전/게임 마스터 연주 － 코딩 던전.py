# swea 게임마스터 연주 - 코딩 던전

import heapq

T = int(input())

def dijkstra(node):
    heap = [(0, 0)]
    
    while heap:
        # heap 중 cost가 작은 것 부터 pop함
        cost, now = heapq.heappop(heap)
        # print(cost, now)

        # 지금 길이보다 cost가 더 길 떄 무시
        if cost > distance[now]:
            continue

        for next, weight in graph[now]:
            new = cost + weight
            
            if new < distance[next]:
                distance[next] = new
                heapq.heappush(heap, (new, next))

    return distance

for tc in range(1, T+1):
    # 던전 개수, 던전 경로 개수, 보유한 골드 
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    distance =[float('inf')]*(N)

    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))

    result = []
    dist = dijkstra(0)
    for i in range(1, N):
        if dist[i] <= K:
            result.append(i)
    print(f'#{tc}', *result)