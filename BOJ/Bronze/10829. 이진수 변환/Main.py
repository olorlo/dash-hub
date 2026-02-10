# 백준 10829번
N = int(input())

value =[]
def bin(num):
    if num <= 1:
        value.append(num)
        return value
    else:
        value.append(num % 2)
        return bin(num // 2)

result = bin(N)
for i in range(len(result)-1,-1,-1):
    print(result[i], end ='')