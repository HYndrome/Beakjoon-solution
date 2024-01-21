#include <iostream>
using namespace std;

int current = 0;

void Print_origin(char Ci, int Ki)
{ 
	while (Ki)
	{
		if (current == 10)
		{
			cout << "\n";
			current = 0;
		}
		cout << Ci;
		Ki--;
		current++;
	}
}

int main()
{
	int cnt_test_case;
	cin >> cnt_test_case;
	for (int T = 0; T < cnt_test_case; T++)
	{
		int N;
		cin >> N;
		char Ci[10];
		int Ki[10];
		current = 0;
		for (int i = 0; i < N; i++)
		{
			cin >> Ci[i] >> Ki[i];
		}
		// 출력
		cout << "#" << T + 1 << "\n";
		for (int i = 0; i < N; i++)
		{
			Print_origin(Ci[i], Ki[i]);
		}
		cout << "\n";
	}
	return 0;
}