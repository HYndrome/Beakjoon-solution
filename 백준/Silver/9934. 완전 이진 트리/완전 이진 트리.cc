#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath> // pow(base, exponent) base^exponent
using namespace std;

int K;
int buildings[1100];

void Input()
{
	// freopen("sample_input.txt", "r", stdin);
	cin >> K;
	for (int i = 0; i < pow(2, K) -1 ; i++)
	{
		cin >> buildings[i];
	}
}
 
void PrintBuiding(int level, int start, int end)
{
	int mid = (start + end) / 2;
	if (level == K)
	{
		cout << buildings[mid] << " ";
		return;
	}
	PrintBuiding(level + 1, start, mid - 1);
	PrintBuiding(level + 1, mid + 1, end);
}

void PrintLevel(int level)
{
	if (level == K)
	{
		return;
	}
	PrintBuiding(K - level, 0, pow(2, K) - 2);
	cout << "\n";
	PrintLevel(level + 1);
	cout << "\n";
}

int main()
{
	Input();
	if (K == 1)
	{
		cout << buildings[0];
	}
	else
	{
		PrintLevel(0);
	}
	return 0;
}