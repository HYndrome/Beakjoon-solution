#include <iostream>
#include <vector>
using namespace std;

int n, k;
vector<int> coins;
int dp[10000 + 1];

void Input()
{
	cin >> n >> k;
	for (int i = 0; i < n; i++)
	{
		int coin;
		cin >> coin;
		coins.push_back(coin);
	}
}

int main()
{
	Input();
	dp[0] = 1; // 0이 되는 경우의 수는 1
	for (int i_c = 0; i_c < coins.size(); i_c++) // 각 동전에 대해서 점화식
	{
		for (int i = coins[i_c]; i <= k; i++)
		{
			dp[i] = dp[i] + dp[i - coins[i_c]]; // dp에서 찾아야하는 핵심 점화식
		}
	}

	cout << dp[k];

	return 0;
}