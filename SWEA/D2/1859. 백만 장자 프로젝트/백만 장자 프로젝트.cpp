#include <iostream>
using namespace std;

int prices[1000000];

int main()
{
	int cnt_test_case;
	cin >> cnt_test_case;
	for (int test_case = 0; test_case < cnt_test_case; test_case++)
	{
		int cnt_prices;
		cin >> cnt_prices; 
		// int prices[1000000]; c6262 에러 발생
		for (int i = 0; i < cnt_prices; i++)
		{
			cin >> prices[i];
		}
		int max_price = 0;
		// int sum_prices = 0; int가 담을 수 있는 최대 범위는 21억 정도
		long long sum_prices = 0;
		for (int current = cnt_prices - 1; current >= 0; current--)
		{
			if (prices[current] > max_price)
			{
				max_price = prices[current];
			}
			else
			{
				sum_prices += max_price - prices[current];
			}
		}
		cout << "#" << test_case + 1 << " " << sum_prices << "\n";
	}

	return 0;
}