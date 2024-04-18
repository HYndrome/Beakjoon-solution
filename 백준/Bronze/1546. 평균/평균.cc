#include <iostream>
using namespace std;

int main()
{
	int N;
	int scores[1000];
	int score_sum = 0;
	double score_max = 0;
	double ans;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> scores[i];
		score_sum += scores[i];
		if (scores[i] > score_max)
		{
			score_max = scores[i];
		}
	}
	ans = score_sum / score_max * 100 / N;
	cout << ans << "\n";

	return 0;
}