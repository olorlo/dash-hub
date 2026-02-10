# 백준 11399번
N = int(input())
time = list(map(int, input().split()))

# 카운트 정렬
cnt = [0] * 1001

for i in range(N):
    cnt[time[i]] += 1

for i in range(1,1001):
    cnt[i]+=cnt[i-1]

temp = [0]*N
for i in range(N-1, -1, -1):
    cnt[time[i]] -= 1
    temp[cnt[time[i]]] = time[i]

# 누적 합 계산
sum =0
sum1=0
for i in temp:
    sum += i
    sum1 += sum
print(sum1)