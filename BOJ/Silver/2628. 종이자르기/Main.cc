#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 백준 C++ 2628 종이자르기

int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	int n, m;
	cin >> n >> m;

	int a;
	cin >> a;

	int b, c;
	int max_y = 0;
	int max_x = 0;
	int y_border = m;
	int x_border = n;

	for (int cut = 0; cut < a; cut++) {
		cin >> b >> c;

		// 가로로 자르기
		if (b == 0) {
			if (c <= y_border / 2) 
				max_y = max(max_y, y_border - c);
			else 
				max_y = max(max_y, c);
			y_border = max_y;
		}
		// 세로로 자르기 ( b==1)
		else if (b==1) {
			if (c <= x_border / 2) 
				max_x = max(max_x, n - c);
			else 
				max_x = max(max_x, c);
			x_border = max_x;
		}

	}		
	cout << max_y * max_x;
}	