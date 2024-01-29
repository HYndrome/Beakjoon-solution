#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue> // 우선순위 큐 max heap
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, int>> classes;
priority_queue<int> pq;

void Input()
{
	// freopen("sample.txt", "r", stdin);
	cin.tie(NULL); // 빠른 입출력
	ios_base::sync_with_stdio(false); // 빠른 입출력
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int class_start, class_end;
		cin >> class_start >> class_end;
		classes.push_back(make_pair(class_start, class_end));
	}
	sort(classes.begin(), classes.end()); // 시작 시간, 끝나는 시간 순으로 정렬
}

int main()
{
	Input();
	for (int i = 0; i < N; i++)
	{
		int class_start = classes[i].first;
		int class_end = classes[i].second;
		if (pq.size() == 0) // 첫 강의실일 경우 heap에 그냥 삽입
		{
			pq.push(-class_end);
		}
		else
		{
			int class_earliest_end = -pq.top(); 
			if (class_start >= class_earliest_end) // 새로운 강의가 강의실 중 가장 일찍 끝나는 강의보다 늦게 시작할 경우
			{
				pq.pop();
				pq.push(-class_end); // heap에 가장 일찍 끝나는 강의실 제거하고 새로운 강의실 추가 (강의실 수 변화 x)
			}
			else // 새로운 강의가 강의실 중 가장 일찍 끝나는 강의보다 일찍 시작할 경우
			{
				pq.push(-class_end); // heap에 해당 강의실 추가 (강의실 + 1)
			}
		} 
	}
	cout << pq.size(); // 강의실 수 출력
	return 0;
}

