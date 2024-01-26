#include <iostream>
#include <string>
using namespace std;

int num[2000000]; // 임의로 돌려보니 100만보다 큰 가장 작은 소수이면서 펠린드롬인 수는 1003001

int IsPelin(int num) // 펠린드롬 수인지 확인하는 함수
{
	string str_num = to_string(num);
	int is_pelin = 1;
	for (int i = 0; i < str_num.size(); i++)
	{
		if (str_num[i] != str_num[str_num.size() -1 - i])
		{
			is_pelin = 0;
			break;
		}
	}
	return is_pelin;
}
int main()
{
	int N;
	cin >> N;
	// 소수 찾기 - 배수를 숫자 배열에서 제외
	num[1] = 1; // 1은 소수가 아님
	for (int i = 2; i < 1000000; i++)
	{
		int cnt = 2;
		while (i * cnt < 2000000)
		{
			num[i * cnt] = 1;
			cnt++;
		}
	}
	// 해당 조건에 맞는 수 찾기 - 소수 && 펠린드롬 수
	for (int i = N; i < 2000000; i++)
	{
		if (num[i] != 1 && IsPelin(i))
		{
			cout << i;
			break;
		}
	}

	return 0;
}