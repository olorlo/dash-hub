# 백준 10872번
N = int(input())
def factorial(num):
    if num <=1:
        return 1
    else:
        return num * factorial(num-1)
    
result = factorial(N)
print(result)