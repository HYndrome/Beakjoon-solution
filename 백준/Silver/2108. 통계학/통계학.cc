#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
vector<int> nums;
int n_sum;
int num_p[4001];
int num_n[4001];
int num_cnt_max;
int num_frequent;

void Input()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		nums.push_back(num);
		n_sum += num;
		if (num >= 0)
		{
			num_p[num]++;
		}
		else
		{
			num_n[-num]++;
		}
	}
}

int main()
{
	Input();
	// 산술평균
	double ans_1_proto = (double)n_sum / N;
	int ans_1 = round(ans_1_proto);
	// 중앙값
	sort(nums.begin(), nums.end());
	int ans_2 = nums[N / 2];
	// 최빈값
	int ans_3 = 0;
	int cnt_max = 0;
	int cnt_max_seq = 1;
	for (int i = 4000; i >= 0; i--)
	{
		if (num_n[i] == cnt_max)
		{
			cnt_max_seq++;
			if (cnt_max_seq == 2)
			{
				ans_3 = -i;
			}
		}
		else if (num_n[i] > cnt_max)
		{
			cnt_max = num_n[i];
			cnt_max_seq = 1;
			ans_3 = -i;
		}
	}
	for (int i = 0; i <= 4000; i++)
	{
		if (num_p[i] == cnt_max)
		{
			cnt_max_seq++;
			if (cnt_max_seq == 2)
			{
				ans_3 = i;
			}
		}
		else if (num_p[i] > cnt_max)
		{
			cnt_max = num_p[i];
			cnt_max_seq = 1;
			ans_3 = i;
		}
	}
	// 범위
	int num_min = nums[0];
	int num_max = nums[N - 1];
	int ans_4 = num_max - num_min;

	cout << ans_1 << "\n";
	cout << ans_2 << "\n";
	cout << ans_3 << "\n";
	cout << ans_4 << "\n";

	return 0;
}