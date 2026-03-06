import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# 1697번 숨바꼭질
def bfs(n, k):
    global cnt, min_cnt 
    dq = deque([(n, k)])
    visited[n] = 0

    while dq:
        subin, dongseang = dq.popleft()
        
        if subin == dongseang:
            return visited[dongseang]
        
        if visited[subin*2] == -1:
            visited[subin*2] = visited[subin] + 1
        dq.append((subin*2, dongseang))

        if visited[subin-1] == -1:
            visited[subin -1] = visited[subin] + 1
        dq.append((subin-1, dongseang))

        if visited[subin+1] == -1:
            visited[subin +1] = visited[subin] + 1
        dq.append((subin+1, dongseang))
 
N, K = map(int,input().split())
visited = [-1] * 1000000
print(bfs(N, K))