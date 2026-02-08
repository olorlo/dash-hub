# 백준 4796번
# 캠핑
tc=0
while(True):
    # 테스트 케이스
    tc +=1
    L, P, V =map(int,input().split())
    if L==0 and P ==0 and V ==0:
        break
    cnt=1
    # cnt 세기
    for i in range(1,V):
        for k in range(1,V//P+1):
            if k*P -2 <= i <= k*P:
                cnt-=1
        cnt+=1
    # 출력
    print(f'Case {tc}: {cnt}')