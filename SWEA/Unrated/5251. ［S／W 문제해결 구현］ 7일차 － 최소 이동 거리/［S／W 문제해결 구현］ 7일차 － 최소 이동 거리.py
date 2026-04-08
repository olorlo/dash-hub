import heapq

# SWEA 최소 이동 거리
T = int(input())

def connect(node):
    global min_dist
    
    # 힙 만들기
    heap = []
    for i, j in graph[node]:
        heapq.heappush(heap, (j, i))
    
    while heap:
        w, now_node = heapq.heappop(heap)
        
        # 방문 처리 + 최소 거리 계산
        visited[now_node] = 1
        min_dist += w
        
        # 종료 조건
        if now_node == N:
            return min_dist 
        
        # 힙에 다음 노드 넣기
        for next_node, we in graph[now_node]:        
            if visited[next_node]:
                continue
            
            heapq.heappush(heap, (we, next_node))

for tc in range(1, T+1):
    # N: 마지막 연결 지점 번호
    # E: 도로의 개수
    N, E = map(int, input().split())
    
    # 구간 시작 s, 구간의 끝점 e, 구간 거리 w 
    arr = [list(map(int, input().split())) for _ in range(E)]

    # 그래프 만들기
    graph = [[] for _ in range(N)]
    for s, e, w in arr:
        graph[s].append((e, w))
        
    # 방문했는지 체크
    visited = [0] * (N+1)
    

    # 함수 실행
    min_dist = 0
    connect(0)
    
    print(f'#{tc} {min_dist}')