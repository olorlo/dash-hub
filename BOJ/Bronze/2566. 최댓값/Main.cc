#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int arr[9][9] ;
	
	int max_arr = 0;
	int max_index1 = 0;
	int max_index2 = 0;
	for (int i = 0; i < 9; i++) 
		for (int j=0;j < 9; j++)
			scanf("%d", &arr[i][j]);
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (arr[i][j] > max_arr) {
				max_arr = arr[i][j];
				max_index1 = i;
				max_index2 = j;
			}

		}
	}
	printf("%d\n%d %d", max_arr, max_index1+1, max_index2+1);
	return 0;
}