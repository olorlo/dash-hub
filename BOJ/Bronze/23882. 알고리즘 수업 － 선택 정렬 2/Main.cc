#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int N = 0;
	int K = 0;
	scanf("%d %d", &N, &K);
	int* arr = (int*)malloc(sizeof(int)*N);
	for (int k = 0; k < N; k++) {
		scanf("%d ", &arr[k]);
	}
	int cnt = 0;
	for (int i = N-1; i > 0; i--) {
		int start = i;
		int temp = 0;
		for (int j = 0; j < i; j++) { //정렬이 안된 상태
			if (arr[start] < arr[j]) {
				temp = arr[start];
				arr[start] = arr[j];
				arr[j] = temp;
				cnt += 1;
			}
			//printf("arr: %d\n", arr[j]);
		}
		if (cnt == K) {
			break;
		}
	}
	if (cnt < K)
		printf("-1");
	else {
		for (int i = 0; i < N; i++) {
			printf("%d ", arr[i]);
		}
	}

	free(arr);
	return 0;
}
