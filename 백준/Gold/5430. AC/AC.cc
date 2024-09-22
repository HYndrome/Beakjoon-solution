#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <deque>
#include <string>
using namespace std;

int T;
char P[100001];
int N;
int X[100];
deque<int> dq;
bool is_reverse = false;

void Init();
void Input();
void Command();

int main()
{
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		Init();
		Input();
		Command();
	}
	return 0;
}

void Init()
{
	dq.clear();
	is_reverse = false;
}

void Input()
{
	char x[400000];
	char x_current[4];
	int x_int;
	cin >> P;
	cin >> N;
	cin >> x;
	int i = 0;
	int i_start = 0;
	int i_end = 0;
	int cnt = 0;
	while (cnt < N)
	{
		if (x[i] == ',' || x[i] == ']')
		{
			i_end = i;
			memset(x_current, 0, sizeof(x_current));
			strncpy(x_current, x + i_start + 1, i_end - i_start - 1);
			dq.push_back(stoi(x_current));
			i_start = i_end;
			cnt++;
		}
		i++;
	}
}

void Command()
{
	int len_str = strlen(P);
	// 함수 실행
	for (int i = 0; i < len_str; i++)
	{
		if (P[i] == 'R')
		{
			is_reverse = !is_reverse;
		}
		else if (P[i] == 'D')
		{
			// 빈 배열일 때 D를 사용한 경우 에러
			if (dq.empty())
			{
				cout << "error\n";
				return;
			}
			if (!is_reverse)
			{
				dq.pop_front();
			}
			else
			{
				dq.pop_back();
			}
		}
	}
	// 최종 결과
	cout << "[";
	if (!is_reverse)
	{
		for (int i = 0; i < dq.size(); i++)
		{
			if (i == dq.size() - 1)
			{
				cout << dq[i];
			}
			else
			{
				cout << dq[i] << ",";
			}
		}
	}
	else
	{
		for (int i = dq.size() - 1; i >= 0; i--)
		{
			if (i == 0)
			{
				cout << dq[i];
			}
			else
			{
				cout << dq[i] << ",";
			}
		}
	}
	cout << "]\n";
}