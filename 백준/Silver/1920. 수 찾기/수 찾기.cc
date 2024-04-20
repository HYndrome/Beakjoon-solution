#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, M;
vector<long long> nums_a;
vector<long long> nums_b;

void Input()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		long long num_a;
		cin >> num_a;
		nums_a.push_back(num_a);
	}
	cin >> M;
	for (int i = 0; i < M; i++)
	{
		long long num_b;
		cin >> num_b;
		nums_b.push_back(num_b);
	}
}

bool BiSearch(int num)
{
	int start = 0;
	int end = N - 1;
	while (start <= end)
	{
		int mid = (start + end) / 2;
		if (nums_a[mid] < num)
		{
			start = mid + 1;
		}
		else if (nums_a[mid] == num)
		{
			return true;
		}
		else if (nums_a[mid] > num)
		{
			end = mid - 1;
		}
	}
	return false;
}

int main()
{
	Input();
	sort(nums_a.begin(), nums_a.end());
	for (int i = 0; i < M; i++)
	{
		if (BiSearch(nums_b[i]))
		{
			cout << "1\n";
		}
		else
		{
			cout << "0\n";
		}
	}
	return 0;
}