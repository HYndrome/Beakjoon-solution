#include <iostream>
using namespace std;

int M, N;
int nums_not_prime[1000001];

int main()
{
	cin >> M >> N;
	for (int i = 2; i <= N; i++)
	{
		for (int j = 2; j <= N; j++)
		{
			if (i * j >= 1000000)
			{
				break;
			}
			nums_not_prime[i * j] = 1;
		}
	}
	nums_not_prime[1] = 1;
	for (int i = M; i <= N; i++)
	{
		if (nums_not_prime[i] != 1)
		{
			cout << i << "\n";
		}
	}
	return 0;
}