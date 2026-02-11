#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void)
{
	int n=0;
	int a = 0; int n1 = 0, n2 = 0, n3 = 0, n4 = 0, n5 = 0, n6 = 0;
	int count = 0;
	scanf("%d", &n);
	
	a = 1000 - n;
	n1 = a / 500;
	n2 = (a % 500) / 100;
	n3 = ((a % 500) % 100) / 50;
	n4 = (((a % 500) % 100) % 50) / 10;
	n5 = ((((a % 500) % 100) % 50) % 10) / 5;
	n6 = ((((a % 500) % 100) % 50) % 10) % 5;

	count = n1 + n2 + n3 + n4 + n5 + n6;
	printf("%d",count);
}