#include <iostream>
#include <deque>

using namespace std;

int N;
deque<int> ans;
deque<int> nums;
deque<int> stack_1;
deque<int> stack_2;
deque<char> operators;

int main()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int ans_c;
		cin >> ans_c;
		ans.push_back(ans_c);
	}
	for (int i = 1; i <= N; i++)
	{
		nums.push_back(i);
	}
	while (stack_2.size() < N)
	{
		if (stack_1.empty())
		{ 
			if (nums.empty())
			{
				break;
			}
			stack_1.push_back(nums.front());
			nums.pop_front();
			// cout << "+\n";
			operators.push_back('+');
		}
		if (stack_1.back() != ans[stack_2.size()])
		{
			if (nums.empty())
			{
				break;
			}
			stack_1.push_back(nums.front());
			nums.pop_front();
			// cout << "+\n";
			operators.push_back('+');
		}
		if (stack_1.back() == ans[stack_2.size()])
		{
			stack_2.push_back(stack_1.back());
			stack_1.pop_back();
			// cout << "-\n";
			operators.push_back('-');
		}
	}
	if (stack_2.size() == N)
	{
		for (int i = 0; i < operators.size(); i++)
		{
			cout << operators[i] << "\n";
		}
	}
	else
	{
		cout << "NO\n";
	}
	return 0;
}