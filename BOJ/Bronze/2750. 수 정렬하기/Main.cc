#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int N;
	scanf("%d", &N);
	//배열 동적 할당
	int* arr = (int*)malloc(sizeof(int)*N);
	//배열 입력
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	// 배열 정렬
	int max_arr = 0;
	int temp = 0;
	for (int i = 0; i <N-1; i++) {
		for (int j = 0; j <N-1-i; j++) {
			if (arr[j] > arr[j+1]) {
				temp=arr[j];
				arr[j] = arr[j+1];
				arr[j + 1] = temp;
		}
		}
	}

	// 배열 출력
	for (int i = 0; i < N; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}
