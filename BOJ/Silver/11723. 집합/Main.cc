#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <cstdio>
#include <string>
using namespace std;

// 백준 C++ 11723 집합

int main() {
	//freopen("input.txt", "r", stdin);

	int M;
	cin >> M;

	set<int>S;

	string a;
	int b;

	for (int i = 0; i < M; i++) {
		cin >> a;
		if (a == "all") {
			S.clear();
			for (int j = 0; j < 20; j++)
				S.insert(j + 1);

		}
		else if (a == "empty")
			S.clear();
		else cin >> b;

		if (a == "add")
			S.insert(b);
		else if (a == "remove")
			S.erase(b);
		else if (a == "check") {
			if (S.find(b) != S.end())
				cout << 1 << '\n';
			else
				cout << 0 << '\n';
		}

		else if (a == "toggle") {
			if (S.find(b) != S.end())
				S.erase(b);
			else
				S.insert(b);
		}		
	}
}