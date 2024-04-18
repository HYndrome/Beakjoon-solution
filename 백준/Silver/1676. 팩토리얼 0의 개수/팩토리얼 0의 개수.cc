#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	int cnt_2 = 0;
	int cnt_5 = 0;
	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		int num = i;
		while (num % 2 == 0)
		{
			num /= 2;
			cnt_2++;
		}
		while (num % 5 == 0)
		{
			num /= 5;
			cnt_5++;
		}
	}
	cout << min(cnt_2, cnt_5) << "\n";
	return 0;
}