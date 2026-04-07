# SWEA 문제풀이3 하나로
import heapq
T = int(input())

def solve(node):
    global min_dist
    
    heap = []
    visited[node] = 1
    
    # 현재 노드에서 갈 수 있는 모든 거리 넣기 
    for next_node in range(N):
        dist = (y_coor[node] - y_coor[next_node])**2 + (x_coor[node] - x_coor[next_node])**2
        heapq.heappush(heap, (dist, next_node))
        
    while heap:
        d, now_node = heapq.heappop(heap)
        
        # 이미 방문한 노드라면 continue
        if visited[now_node]:
            continue
        
        # 방문 처리 밖에서 해줌 (now_node로 가는 최소 비용이 선택되었음)
        visited[now_node] = 1
        min_dist += d
        
        for next_node in range(N):
            if visited[next_node]:
                continue
            
            # 거리 계산
            next_dist = (y_coor[now_node] - y_coor[next_node])**2 + (x_coor[now_node] - x_coor[next_node])**2
            
            heapq.heappush(heap, (next_dist, next_node))
        
    # 1. 거리 계산
    # 2. MST 수행
    # 3. 총 비용 계산 


for tc in range(1, T+1):
    # 섬의 개수
    N = int(input())
    
    # 섬의 좌표
    x_coor = list(map(int, input().split()))
    y_coor = list(map(int, input().split()))
    
    # 환경 부담 세율 실수
    E = float(input())
    
    # 방문했는지 체크
    visited = [0] * N
    
    # 최소 환경 부담금
    min_dist = 0
    
    # 총 환경 부담금을 최소로 지불하며,
    # N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계
    # 일단 노드 0 부터 시작
    solve(0)
    
    # 반올림 대문에 + 0.5 해줌
    print(f'#{tc} {int(min_dist * E + 0.5)}')