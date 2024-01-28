#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
using namespace std;

int N;
int arr_primary[1000000 + 1] = { 0 };
int arr_N[100000] = { 0 };
set<long long>  set_primary;

void Input() 
{
	// freopen("sample.txt", "r", stdin);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr_N[i];
	}
}

void CalPrimary()
{
	for (int i = 0; i < 1000000 + 1; i++)
	{
		arr_primary[i] = 1;
	}
	arr_primary[0] = 0;
	arr_primary[1] = 0;
	for (int i = 2; i <= 500000; i++)
	{
		int cnt = 2;
		while (i * cnt <= 1000000)
		{
			arr_primary[i * cnt] = 0;
			cnt++;
		}
	}
}

void RemainOnlyPrimary()
{ 
	for (int i = 0; i < N; i++) 
	{
		if (arr_primary[arr_N[i]] == 1)
		{
			set_primary.insert(arr_N[i]);
		}
	}
}

int main()
{
	Input(); // 입력
	CalPrimary(); // 0부터 1000000까지의 int 배열을 생성하고 소수이면 1 아니면 0인 배열 생성 - 수가 여러번 입력되기 때문에 배열로 확인
	RemainOnlyPrimary();
 	if (set_primary.size() == 0)
	{
		cout << -1;
	}
	else
	{
		long long least_common_multiple = 1; // 답이 2^63 미만인 형태
		for (set<long long>::iterator it = set_primary.begin(); it != set_primary.end(); ++it)
		{
			least_common_multiple *= *it; // 중복되는 숫자가 없을 때(set) 소수끼리 곱하면 최대공배수가 됨
		}
		cout << least_common_multiple;
	}
	return 0;
}