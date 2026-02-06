#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {

	int N = 0;
	scanf("%d", &N);
	int* arr = (int*)malloc(sizeof(int)*N);
	// 입력
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);
	
	// cnt 인덱스를 위해서 arr 최대값 찾기
	int max_arr = 0;
	for (int i = 0; i < N; i++)
		if (arr[i] > max_arr) {
			max_arr = arr[i];
		}

	// 카운팅 정렬
	// calloc으로 동적할당하면 0으로 자동 초기화
	int* cnt = (int*)calloc(max_arr+1,sizeof(int));
	int* temp = (int*)malloc(sizeof(int)*N);

	// 발생 횟수 기록
	for (int i = 0; i < N; i++)
		cnt[arr[i]] += 1;

	// 누적 카운티 배열
	for (int i = 1; i < max_arr + 1; i++)
		cnt[i] += cnt[i - 1];

	// cnt 값 1씩 빼고, 뺸 값을 temp 인덱스로 접근해서 arr 값 삽입
	for (int i = N - 1; i > -1; i--) {
		cnt[arr[i]] -= 1;
		temp[cnt[arr[i]]] = arr[i];
	}

	// 출력
	for (int i = 0; i < N; i++)
		printf("%d\n", temp[i]);

	free(arr);
	free(cnt);
	free(temp);
	return 0;
}