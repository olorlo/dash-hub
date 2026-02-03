#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int T;
	int a = 0;
	int b = 0;
	int c = 0;
	scanf("%d", &T);

	while (T != 0) {
		if (T >= 300) {
			a += 1;
			T -= 300;
		}
		else if (T >=60 && T < 300) {
			b += 1;
			T -= 60;
		}
		else if (T >= 10 && T < 60) {
			c += 1;
			T -= 10;
		}
		else if ( T< 10){
			T=-1;
			break;
		}
		
	}

	if (T == -1)
		printf("%d", T);
	else
		printf("%d %d %d", a, b, c);
	return 0;
}