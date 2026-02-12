# 백준 2559번 수열
N, K = map(int, input().split())
temp = list(map(int, input().split()))

continuity = sum(temp[:K])
max_temp = continuity
for i in range(N-K):
    continuity = continuity - temp[i] + temp[i+K]
    max_temp = max(continuity, max_temp)

print(max_temp)