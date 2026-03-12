#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

// 백준 C++ 10815번 숫자카드
int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	int N;
	cin >> N;

	vector<int>arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	int M;
	cin >> M;

	vector<int>b(M);
	for (int i = 0; i < M; i++)
		cin >> b[i];

	vector<int>result(M);

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			result[i] = 0;
			if (b[i] == arr[j]) {
				result[i] = 1;
				break;
			}

		}
	}
	for (int i = 0; i < M; i++) {
		cout << result[i] << " ";

	}

}	