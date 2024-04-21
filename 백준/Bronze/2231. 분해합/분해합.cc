#include <iostream>
using namespace std;

int FindCreator(int num)
{	
	int digit = 1;
	int divider = 10;
	// 몇 자리수 인지 확인
	while (num / divider > 0)
	{
		divider *= 10;
		digit++;
	}
	int num_to_find_min = num - 9 * digit;
	if (num_to_find_min < 0) num_to_find_min = 0;
	for (int i = num_to_find_min; i <= num; i++)
	{
		int num_search = i;
		int num_sum = num_search;
		while (num_search > 0)
		{
			num_sum += num_search % 10;
			num_search /= 10;
		}
		if (num_sum == num)
		{
			return i;
		}
	}
	return 0;
}

int main()
{
	int N;
	cin >> N;
	int ans = FindCreator(N);
	cout << ans;
	return 0;
}