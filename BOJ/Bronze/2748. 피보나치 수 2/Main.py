# sys.setrecursionlimit(10**7) < - 재귀 호출 한도 때문에 버그 났을때 재귀 한도 늘리는 방법 (백준에서만 해당됨) 

# 백준 2748번
# 같은 수를 두번 이상 계산할 필요없이 저장해놓고 가져다 씀
N = int(input())
def fibo(num):
    if num <= 1:
        return num
    
    # 한번이라도 계산했다면 딕셔너리에 기록 
    if dic.get(num):
        return dic[num]
    
    # 계산 결과 dic에 저장
    dic[num] = fibo(num -1) + fibo(num - 2)
    return dic[num]

dic={}
result = fibo(N)
print(result)