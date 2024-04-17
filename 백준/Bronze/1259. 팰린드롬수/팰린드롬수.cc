#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>
using namespace std;

void CheckPalindrome(int num)
{
	char phase_int[6];
	sprintf(phase_int, "%d", num);
	int phase_int_len = strlen(phase_int);
	for (int i = 0; i < phase_int_len; i++)
	{
		if (phase_int[i] != phase_int[phase_int_len - i - 1])
		{
			cout << "no\n";
			return;
		}
	}
	cout << "yes\n";
}

int main()
{	
	while (true)
	{
		int num;
		cin >> num;
		if (num == 0)
		{
			break;
		}
		else
		{
			CheckPalindrome(num);
		}
	}
	return 0;
}