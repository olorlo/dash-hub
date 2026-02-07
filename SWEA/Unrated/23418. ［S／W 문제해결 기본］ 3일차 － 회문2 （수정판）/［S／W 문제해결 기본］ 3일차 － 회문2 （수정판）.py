# SWEA 23418번
# 가장 긴 회문 구하기
for _ in range(1,11):
    tc = int(input())
    arr = [input().strip() for _ in range(100)]
    
    save_palindrome=[]

    for i in range(100):
        # print('i: ', i)
        for j in range(100):
            check_garo = ''
            check_sero = ''

            # index j부터 99까지 검사
            for k in range(100):
                nx= j + k
                if nx <0 or nx >=100:
                    continue
                
                # 가로 검사
                check_garo += arr[i][nx]
                if check_garo == check_garo[::-1]:
                    save_palindrome.append(check_garo)

                # 세로 검사
                check_sero+=arr[nx][i]
                if check_sero == check_sero[::-1]:
                    save_palindrome.append(check_sero)
    # 최대값 구하기
    max =0
    for a in save_palindrome:
        if len(a) > max:
            max=len(a)

    # 출력
    print(f'#{tc} {max}')