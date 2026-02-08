# 백준 4796번
# 캠핑
tc=0
while(True):
    # 테스트 케이스
    tc +=1
    L, P, V =map(int,input().split())
    if L==0 and P ==0 and V ==0:
        break
    arr = [0] * (V+1)
    cnt=0
    # 리스트에 넣기
    for i in range(len(arr)):
        for k in range(1,V//P+1):
            if k*P -2 <= i <= k*P:
                arr[i] = 0
                cnt-=1
                break
            arr[i]=cnt
        cnt+=1

    # 출력
    print(f'Case {tc}: {arr[-1]}')