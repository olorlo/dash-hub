# 백준 12847번 꿀 아르바이트

n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_money = 0 
for i in range(n):
    money = 0
    for j in range(m):
        nj = i + j # i일로부터 계속 일한 날짜
        if nj <0 or nj >=n:
            continue
        money += arr[nj]
    if money > max_money:
        max_money = money
print(max_money)