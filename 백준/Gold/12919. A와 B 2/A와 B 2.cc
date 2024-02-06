#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string str_in, str_check;
int len_str_in, len_str_check;
int flag_possible = 0;

void Input()
{
	cin >> str_in >> str_check;
	len_str_in = str_in.size();
	len_str_check = str_check.size();
}

string Method2(string str_in)
{
	str_in.push_back('B');
	reverse(str_in.begin(), str_in.end());
	return str_in;
}

string Method2Rev(string str_in)
{
	reverse(str_in.begin(), str_in.end());
	str_in.pop_back();
	return str_in;
}


void Dfs(int len_str_in)
{
	if (flag_possible) // 성공한 케이스를 찾았을 경우 나머지 다 return 처리
	{
		return;
	}
	int flag_in = 0; // 가지치기 - 원래 상태나 뒤집은 상태는 최종 문자열의 중간 부분과 일치해야함
	// 일부분인지 확인
	for (int i = 0; i <= str_check.size() - str_in.size(); i++)
	{
		if (str_check.compare(i, str_in.size(), str_in) == 0)
		{
			flag_in = 1;
			break;
		}
	}
	// 뒤집어서 일부분인지 확인
	if (flag_in == 0)
	{
		reverse(str_in.begin(), str_in.end());
		for (int i = 0; i <= str_check.size() - str_in.size(); i++)
		{
			if (str_check.compare(i, str_in.size(), str_in) == 0)
			{
				flag_in = 1;
				break;
			}
		}
		reverse(str_in.begin(), str_in.end());
	}
	// 일부분이 아니라면 가지치기
	if (flag_in == 0)
	{
		return;
	}
	if (len_str_in == len_str_check) // 길이가 같을 때 최종 비교
	{
		// 같은지 비교
		if (str_in.compare(str_check) == 0)
		{
			flag_possible = 1;
		}
		return;
	}
	// 1. 문자열 뒤에 A를 추가
	str_in.push_back('A');
	Dfs(len_str_in + 1);
	str_in.pop_back();
	// 2. 문자열 뒤에 B를 추가하고 문자열을 뒤집
	str_in = Method2(str_in);
	Dfs(len_str_in + 1);
	str_in = Method2Rev(str_in);
}

int main()
{
	Input();
	Dfs(len_str_in);
	cout << flag_possible;
	return 0;
}