#include <iostream>
using namespace std;

int main()
{
	int cnt_test_case;
	cin >> cnt_test_case;
	for (int test_case = 0; test_case < cnt_test_case; test_case++)
	{
		int test_case_no;
		cin >> test_case_no;
		int students[1000];
		for (int i = 0; i < 1000; i++)
		{
			cin >> students[i];
		}
		int scores[101] = { 0 };
		for (int i = 0; i < 1000; i++)
		{
			scores[students[i]]++;
		}
		int score_common;
		int cnt_max = 0;
		for (int i = 0; i < 101; i++)
		{
			if (scores[i] >= cnt_max)
			{
				cnt_max = scores[i];
				score_common = i;
			}
		}

		cout << "#" << test_case_no << " " << score_common << "\n";
	}
	return 0;
}
