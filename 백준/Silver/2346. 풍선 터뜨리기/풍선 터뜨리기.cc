#include <iostream>
#include <deque>
using namespace std;
int main()
{
	// 종이 입력
	int papers[1000];
	int cnt_papers;
	cin >> cnt_papers;
	for (int i = 0; i < cnt_papers; i++)
	{
		cin >> papers[i];
	}
	// 풍선 만들기 deque
	deque<int> dq;
	for (int i = 0; i < cnt_papers; i++)
	{
		dq.push_back(i);
	}
	// 시작
	int current_bal = dq.front();
	int current_paper = papers[current_bal];
	cout << current_bal + 1 << " ";
	dq.pop_front();
	// 풍선 파괴 while 반복문
	while (!dq.empty())
	{
		// 풍선 종이 숫자대로 찾아가기
		if (current_paper >= 0)
		{
			while (--current_paper)
			{
 				dq.push_back(dq.front()); // dq 왼쪽으로 회전
				dq.pop_front();
			}
		}
		else
		{
			while (current_paper++)
			{
				dq.push_front(dq.back()); // dq 오른쪽으로 회전
				dq.pop_back();
			}
		}
		// 찾아간 풍선 제거
		current_bal = dq.front();
		current_paper = papers[current_bal];
		cout << current_bal + 1 << " ";
		dq.pop_front();
	}

	return 0;
}