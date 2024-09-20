#include <iostream>
#include <cmath>
using namespace std;

int N, R, C;
int ans = 0;

void Input();
void FuncZ(int y, int x, int n);

int main()
{
	Input();
	FuncZ(R, C, N);
	cout << ans << "\n";
	return 0;
}

void Input()
{
	cin >> N >> R >> C;
}

void FuncZ(int y, int x, int n)
{
	if (n == 0)
	{
		return;
	}
	if (y < pow(2, n - 1))
	{
		if (x < pow(2, n - 1))
		{
			FuncZ(y, x, n - 1);
		}
		else
		{
			ans += 1 * pow(4, n - 1);
			FuncZ(y, x - pow(2, n - 1), n - 1);
		}
	}
	else
	{
		if (x < pow(2, n - 1))
		{
			ans += 2 * pow(4, n - 1);
			FuncZ(y - pow(2, n - 1), x, n - 1);
		}
		else
		{
			ans += 3 * pow(4, n - 1);
			FuncZ(y - pow(2, n - 1), x - pow(2, n - 1), n - 1);
		}
	}
}