# 백준 12847번 꿀 아르바이트

n, m = map(int, input().split())
arr = list(map(int, input().split()))
money = sum(arr[:m])
max_money = money
for i in range(n-m):
    money = money - arr[i] + arr[i+m]
    
    max_money = max(max_money, money)
    # if money > max_money:
    #     max_money = money
print(max_money)