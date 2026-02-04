#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int num = 0;
	scanf("%d", &num);
	// 동적 할당
	int* x = (int*)malloc(sizeof(int) * num);
	int* y = (int*)malloc(sizeof(int) * num);

	// 도화지 초기화
	int background[100][100] = { 0 };

	// 색종이 좌표 입력
	for (int i = 0; i < num; i++) {
		scanf("%d %d", &x[i], &y[i]);
	}

	// 색종이 있는 부분 1로 설정
	for (int i = 0; i < num; i++)
		for (int k = y[i]; k < y[i] + 10; k++)
			for (int l = x[i]; l < x[i] + 10; l++)
				background[k][l] = 1;
	
	// 넓이 계산(색종이 있는 부분 다 더하기)
	int area = 0;
	for(int i=0;i<100;i++)
		for (int j = 0; j < 100; j++) {
			if (background[i][j] > 0) {
				area += 1;
			}
		}
	printf("%d", area);

	//동적 할당 메모리 해제
	free(x);
	free(y);
	return 0;
}