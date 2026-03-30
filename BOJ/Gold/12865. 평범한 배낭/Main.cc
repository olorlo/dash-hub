#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

// 백준 C++ 12865 평범한 배낭

int main() {
	// input.txt 연결
	// freopen("input.txt", "r", stdin);

	// 빠른 입력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// N: 물품의 수, K: 버틸 수 있는 무게
	int N, K;
	cin >> N >> K;
	int W, V;
	vector<pair<int, int>>bag;

	// dp[i][w]: i번째 물건까지 고려했을 때, 무게 w에서 얻을 수 있는 최대 가치
	vector<vector<int>>dp(N+1, vector<int>(K+1, 0));

	// 물건 별 무게 및 가치 입력
	for (int i = 0; i < N; i++) {
		// W: 무게, V: 가치
		cin >> W >> V;
		bag.push_back({ W, V });
	}

	// i: 현재 고려하는 물건 번호
	for (int i = 1; i <= N; i++) {

		// 현재 물건의 무게와 가치
		int weight = bag[i - 1].first;
		int value = bag[i - 1].second;

		// w: 현재 배낭에 남은 용량
		for (int w = 0; w <= K; w++) {

			// 배낭에 물건을 못 넣는 경우
			if (weight > w)
				dp[i][w] = dp[i - 1][w];

			// 물건을 넣었음(용량 w에서 weight을 뺌)
			else {
				// 물건을 넣지 않는 경우와 물건을 넣은 경우의 가치 중 큰 가치 선택
				dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value);
			}
		}
	}

	int result = *max_element(dp[N].begin(), dp[N].end());
	cout << result;
}