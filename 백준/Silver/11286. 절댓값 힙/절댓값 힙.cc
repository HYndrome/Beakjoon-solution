#define _CRT_SECURE_NO_WARNINGS 
#include <iostream>
#include <queue> // priority_queue 사용, pq는 기본적으로 max heap
using namespace std;

int N;
priority_queue < pair<int, int>> pq;

void Input()
{
	// freopen("sample_input.txt", "r", stdin); // sample_input.txt 입력
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	cin >> N;
}

int RevAbs(int num) // 정수를 입력 받아 -절댓값 return
{
	if (num >= 0)
	{
		return -num;
	}
	else
	{
		return num;
	}
}

int main()
{
	Input();
	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		if (x == 0)
		{
			if (pq.empty()) // priority_queue::empty는 size가 0이면 true return
			{
				cout << 0 << "\n";
			}
			else
			{
				cout << -pq.top().second << "\n"; // 절댓값이 가장 작으면서 가장 작은 수 출력; *(-1)했던 값 되돌려 출력
				pq.pop(); // pop은 값을 리턴 x
			}
		}
		else
		{
			pq.push(make_pair(RevAbs(x), -x)); //pq에 값(-|x|, -x) 입력; min heap을 위해 *(-1)로 입력
		}
	}
	return 0;
}