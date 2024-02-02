#include <vector>
#include <iostream>
using namespace std;

int N, K;
vector<int> numbers;
vector<int> numbers_odd;

void Input()
{
	cin >> N >> K;
	numbers_odd.push_back(-1);
	for (int i = 0; i < N; i++)
	{
		int number;
		cin >> number;
		numbers.push_back(i);
		if (number % 2 == 1)
		{
			numbers_odd.push_back(i);
		}
	}
	numbers_odd.push_back(numbers.size());
}


int CheckMaxLength()
{
	if (numbers_odd.size() - 2 <= K)
	{
		return numbers.size() - (numbers_odd.size() - 2);
	}
	else
	{
		int max_length = 0;
		for (int i = 0; i < numbers_odd.size() - K - 2; i++)
		{
			int current = numbers[numbers_odd[i + K + 1] - 1] - numbers[numbers_odd[i] + 1] + 1 - K;
			if (current > max_length)
			{
				max_length = current;
			}
		}
		return max_length;
	}
}

int main()
{
	Input();
	int ans = CheckMaxLength();
	cout << ans;
	return 0;
}