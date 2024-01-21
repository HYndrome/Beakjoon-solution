#include <iostream>
using namespace std;

int arr[15][15];

int main()
{
	int T;
	cin >> T;
	for (int test_case = 0; test_case < T; test_case++)
	{
		int N, M;
		cin >> N >> M;
		for (int y = 0; y < N; y++)
		{
			for (int x = 0; x < N; x++)
			{
				cin >> arr[y][x];
			}
		}
		int cnt_max = 0;
		for (int y = 0; y <= N - M; y++)
		{
			for (int x = 0; x <= N - M; x++)
			{
				int cnt_temp = 0;
				for (int y_m = 0; y_m < M; y_m++)
				{
					for (int x_m = 0; x_m < M; x_m++)
					{
						cnt_temp += arr[y + y_m][x + x_m];
					}
				}
				if (cnt_temp > cnt_max)
				{
					cnt_max = cnt_temp;
				}
			}
		}
		cout << "#" << test_case + 1 << " " << cnt_max << "\n";
	}
	return 0;
}