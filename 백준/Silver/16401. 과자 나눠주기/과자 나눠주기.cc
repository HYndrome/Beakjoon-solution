#include <iostream>
#include <algorithm>
using namespace std;

int m, n;
int cookies[1000000];
int cookie_max = 0;

void Input()
{
	cin >> m >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> cookies[i];
		cookie_max = max(cookies[i], cookie_max);
	}
}

int CntCookie(int size_cookie)
{
	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		cnt += cookies[i] / size_cookie;
	}
	return cnt;
}

int Bisearch()
{
	int start = 0;
	int end = cookie_max;
	while (start <= end)
	{
		int mid = (start + end) / 2;
		if (mid == 0)
		{
			if (m > n)
			{
				return 0;
			}
			return 1;
		}
		if (CntCookie(mid) < m) // 조카 수 보다 작다!
		{
			end = mid - 1;
		}
		else if (CntCookie(mid) >= m)
		{
			start = mid + 1;
		}
	}
	return end;
}

int main()
{
	Input();
	int ans = Bisearch();
	cout << ans << "\n";
	return 0;
}