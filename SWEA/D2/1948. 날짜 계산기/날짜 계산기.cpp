#include <iostream>
using namespace std;

int main()
{
	int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	int T;
	cin >> T;
	for (int test_case = 0; test_case < T; test_case++)
	{
		int m_start, d_start, m_end, d_end;
		cin >> m_start >> d_start >> m_end >> d_end;
		int cnt_date = -d_start + d_end + 1;
		for (int i = m_start; i < m_end; i++)
		{
			cnt_date += days[i];
		}
		cout << "#" << test_case + 1 << " " << cnt_date << "\n";
	}
	return 0;
}