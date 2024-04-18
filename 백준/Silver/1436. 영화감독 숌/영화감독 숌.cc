#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>
using namespace std;

int N;

bool CheckShom(int num)
{
	int six_cont = 0;
	int six_cont_max = 0;
	char num_to_char[8];
	sprintf(num_to_char, "%d", num);
	for (int i = 0; i < strlen(num_to_char); i++)
	{
		if (num_to_char[i] == '6')
		{
			six_cont++;
		}
		else
		{
			six_cont = 0;
		}
		if (six_cont > six_cont_max)
		{
			six_cont_max = six_cont;
		}
	}
	if (six_cont_max >= 3)
	{
		return true;
	}
	return false;
}

int main()
{
	cin >> N;
	int series = 665;
	int cnt = 0;
	while (true)
	{
		bool flag_is_shom = CheckShom(series);
		if (flag_is_shom)
		{
			cnt++;
		}
		if (cnt == N)
		{
			cout << series << "\n";
			break;
		}
		series++;
	}
	return 0;
}