import sys
# sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**6)


def isComplete(num,acc, lst):
    # 시작 점: 1 
    # 끝점: N//2
    # 누적값: 약수(리스트)
    # num 이 1일 때 
    if acc > num//2:
        return 
    if num % acc == 0:
        lst.append(acc)
    isComplete(num, acc+1,lst)
    return lst
    # return lst

# 백준 9506번
while True:
    n = int(input())
    lst = [] 
    if n == -1:
        break
    result = isComplete(n,1, lst)
    if sum(result) == n:
        print(f'{n} = {' + '.join(map(str, result))}')
        
    else:
        print(f'{n} is NOT perfect.')
