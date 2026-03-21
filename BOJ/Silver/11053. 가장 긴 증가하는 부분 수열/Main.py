import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque

# 백준 11053 가장 긴 증가하는 부분 수열
N = int(input())
A = list(map(int, input().split()))
cnt =0
dp = [0]*(N+1)

dp[1] = 1

for i in range(2, N+1):
    if A[i-1] >= A[i-2]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]


print(dp[N])
