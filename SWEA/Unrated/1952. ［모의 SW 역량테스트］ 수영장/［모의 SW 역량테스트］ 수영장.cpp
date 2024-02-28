#include <iostream>
using namespace std;

int INF = 213456789;
int T;
int month[13];
int monthly_use[13];
int price_d_1m_3m_y[4];

void Init()
{
	for (int i = 1; i < 13; i++)
	{
		month[i] = INF;
	}
	month[0] = 0;
}

void Input()
{
	for (int i = 0; i < 4; i++)
	{
		cin >> price_d_1m_3m_y[i];
	}
	for (int i = 0; i < 12; i++)
	{
		cin >> monthly_use[i];
	}
}
 
void CheckPrice()
{
	for (int i = 0; i < 12; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (j == 0)
			{
				if (i + 1 <= 12)
				{
					int next_cost = month[i] + monthly_use[i] * price_d_1m_3m_y[j];
					month[i + 1] = month[i + 1] > next_cost ? next_cost : month[i + 1];
				}
			}
			if (j == 1)
			{
				if (i + 1 <= 12)
				{
					int next_cost = month[i] + price_d_1m_3m_y[j];
					month[i + 1] = month[i + 1] > next_cost ? next_cost : month[i + 1];
				}
			}
			if (j == 2)
			{
				if (i + 3 <= 12)
				{
					int next_cost = month[i] + price_d_1m_3m_y[j];
					month[i + 3] = month[i + 3] > next_cost ? next_cost : month[i + 3];
				}
			}
			if (j == 3)
			{
				if (i + 12 <= 12)
				{
					int next_cost = month[i] + price_d_1m_3m_y[j];
					month[i + 12] = month[i + 12] > next_cost ? next_cost : month[i + 12];
				}
			}
		}
	}
}

int main()
{
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++)
	{
		Init();
		Input();
		CheckPrice();
		cout << "#" << test_case << " " << month[12] << "\n";
	}
	return 0;
}