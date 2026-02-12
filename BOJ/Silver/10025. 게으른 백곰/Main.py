# 백준 10025번 게으른 백곰
N, K = map(int,input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

arr = [0] * 1000001
for i in range(N):
    arr[ice[i][1]]+=ice[i][0]

temp =0
# 초기 상태 지정
for i in range(2 * K + 1):
    temp += arr[i]

max_ice = temp
for i in range(1000000 - 2 * K):
    temp = temp - arr[i] + arr[i + 2 * K+1] 

    max_ice = max(temp, max_ice)

print(max_ice)