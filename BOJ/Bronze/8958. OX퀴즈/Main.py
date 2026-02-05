# 8958번

tc=int(input())
for _ in range(tc):
    quiz = list(input())
    # print(quiz)
    cnt = 0
    sum_cnt = 0
    for i in quiz:
        if i == "O":
            cnt+=1
        elif i == "X":
            cnt = 0
        sum_cnt += cnt
    print(sum_cnt)