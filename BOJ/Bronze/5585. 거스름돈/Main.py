# 백준 5585번
n = int(input())
n = 1000 - n
cnt = 0 
while n>0 :
    
    if n >= 500:
        cnt += 1
        n -= 500
    elif n >= 100:
        cnt += 1
        n -= 100
    elif n >= 50:
        cnt += 1
        n -= 50
    elif n >= 10:
        cnt += 1
        n -= 10
    elif n >= 5:
        cnt += 1
        n -= 5
    else:
        n -= 1
        cnt += 1
print(cnt)