#include <iostream>
#include <queue>
#include <string>
#include <cmath>

using namespace std;

int T;
int N, K;
queue<int> numbers;
priority_queue<long long> pq_num_comb;

void Init()
{
	while (!numbers.empty())
	{
		numbers.pop();
	}
	while (!pq_num_comb.empty())
	{
		pq_num_comb.pop();
	}
}

void Input()
{
	cin >> N >> K;
	string numbers_str;
	cin >> numbers_str;
	for (int i = 0; i < numbers_str.size(); i++)
	{
		if (numbers_str[i] == '0') numbers.push(0);
		if (numbers_str[i] == '1') numbers.push(1);
		if (numbers_str[i] == '2') numbers.push(2);
		if (numbers_str[i] == '3') numbers.push(3);
		if (numbers_str[i] == '4') numbers.push(4);
		if (numbers_str[i] == '5') numbers.push(5);
		if (numbers_str[i] == '6') numbers.push(6);
		if (numbers_str[i] == '7') numbers.push(7);
		if (numbers_str[i] == '8') numbers.push(8);
		if (numbers_str[i] == '9') numbers.push(9);
		if (numbers_str[i] == 'A') numbers.push(10);
		if (numbers_str[i] == 'B') numbers.push(11);
		if (numbers_str[i] == 'C') numbers.push(12);
		if (numbers_str[i] == 'D') numbers.push(13);
		if (numbers_str[i] == 'E') numbers.push(14);
		if (numbers_str[i] == 'F') numbers.push(15);
	}
}

void CombNumbers()
{
	int cutting = N / 4;
	long long combCurrent = 0;
	int cnt = 0;
	for (int i = 0; i < cutting; i++)
	{
		int firstDigit = numbers.front();
		numbers.pop();
		numbers.push(firstDigit);
		cnt = 0;
		while (cnt < N)
		{
			int currentDigit = numbers.front();
			numbers.pop();
			numbers.push(currentDigit);
			int  power = cnt % cutting;
			combCurrent += currentDigit * pow(16, cutting - 1 - power);
			if (cnt % cutting == cutting - 1)
			{
				pq_num_comb.push(combCurrent);
				combCurrent = 0;
			}
			cnt++;
		}
	}
}

long long FindPw()
{
	int num_before = -1;
	int cnt = 1;
	while (!pq_num_comb.empty())
	{
		long long current = pq_num_comb.top();
		pq_num_comb.pop();
		if (current == num_before)
		{
			continue;
		}
		if (cnt == K)
		{
			return current;
		}
		num_before = current;
		cnt++;
	}
}

int main()
{
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++)
	{
		Init();
		Input();
		CombNumbers();

		long long pw = FindPw();
		cout << "#" << test_case << " " << pw << "\n";
	}
	return 0;
}