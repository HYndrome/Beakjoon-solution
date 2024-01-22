#include <iostream>
#include <vector> // 스택을 vector로 구현
#include <string>
#include <iomanip> // 소수점 고정
using namespace std;

int N;
string str_in;
double values['Z' - 'A' + 1];

void input()
{
	cin >> N;
	cin >> str_in;
	for (int i = 0; i < N; i++)
	{
		cin >> values[i];
	}
}

int main()
{
	input();
	vector<double> stack; // 숫자를 저장할 스택

	// 후위 표기식은 연산자를 만났을 때 연산자 앞의 두 숫자로 연산 진행
	for (int i = 0; i < str_in.length(); i++)
	{
		if (str_in[i] >= 'A' && str_in[i] <= 'Z')
		{
			stack.push_back(values[str_in[i] - 'A']);
		}
		else if (str_in[i] == '+')
		{
			double num_1, num_2;
			num_1 = stack.back();
			stack.pop_back();
			num_2 = stack.back();
			stack.pop_back();
			stack.push_back(num_2 + num_1);
		}
		else if (str_in[i] == '-')
		{
			double num_1, num_2;
			num_1 = stack.back();
			stack.pop_back();
			num_2 = stack.back();
			stack.pop_back();
			stack.push_back(num_2 - num_1);
		}
		else if (str_in[i] == '/')
		{
			double num_1, num_2;
			num_1 = stack.back();
			stack.pop_back();
			num_2 = stack.back();
			stack.pop_back();
			stack.push_back(num_2 / num_1);
		}
		else if (str_in[i] == '*')
		{
			double num_1, num_2;
			num_1 = stack.back();
			stack.pop_back();
			num_2 = stack.back();
			stack.pop_back();
			stack.push_back(num_2 * num_1);
		}
	}
	cout << setprecision(2) << fixed; // 소수점 아래 2자리 표기 고정
	cout << stack.front();

	return 0;
}