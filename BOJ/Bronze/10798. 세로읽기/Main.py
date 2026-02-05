# 10798번
arr = [input() for _ in range(5)]
result =[]
# print(arr)
for i in range(15):
    for j in range(5):
        # 각 줄의 i번째 문자가 존재하면 출력하고, 없으면 pass
        if i < len(arr[j]):
            result += arr[j][i]
print(''.join(result))




# 실패 코드 .. 예시는 맞는데 너무 복잡하게 짬 -> 간단하게 생각하기
# arr = [list(input().split()) for _ in range(5)]
# # print(arr)
# arr1=[]
# for i in range(5):
#     arr1.append(list(' '.join(arr[i])))
# # print(arr1)
# i_index =[]
# j_index =[]

# # 제일 긴 배열 찾기
# max_len =0
# for i in arr1:
#     if len(i) >= max_len:
#         max_len = len(i)
# # print(max_len)


# for i in range(5):
#     # 제일 긴 배열보다 작으면 그 위치 저장하고 나중에 건너뛸때 사용
#     if len(arr1[i]) < max_len:
#         for j in range(max_len - len(arr1[i])):
#             i_index.append(i)
#             j_index.append(len(arr1[i])+j)

# # print('i_index: ',i_index)
# # print('j_index', j_index)
# result = []
# for i in range(max_len):
#     break_i =0
#     break_j=0
#     for j in range(5):
#         for k in range(len(i_index)):
#             # ny = i + i_index
#             # nx = j + j_index
#             if i == j_index[k] and j == i_index[k]:
#                 break_i=i
#                 break_j=j
#                 break
#         if i == break_i and j == break_j:
#             continue
#         result += arr1[j][i]

# print(''.join(result))