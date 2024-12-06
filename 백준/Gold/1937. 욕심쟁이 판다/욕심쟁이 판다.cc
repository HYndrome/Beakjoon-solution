#include <iostream>
#include <algorithm>
using namespace std;

int n;
int graph[500][500];
int dp[500][500];
int dy[] = { -1, 1, 0, 0 };
int dx[] = { 0, 0, -1, 1 };
 
void Input()
{
	cin >> n;
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < n; x++)
		{
			cin >> graph[y][x];
		}
	}
}

int Dfs(int y, int x)
{
	if (dp[y][x] != 0)
	{
		return dp[y][x];
	}
	dp[y][x] = 1;
	for (int i = 0; i < 4; i++)
	{
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (ny < 0 || ny >= n || nx < 0 || nx >= n)
		{
			continue;
		}
		if (graph[ny][nx] <= graph[y][x])
		{
			continue;
		}
		dp[y][x] = max(dp[y][x], Dfs(ny, nx) + 1);
	}
	return dp[y][x];
}

int main()
{
	int move_max = 0;
	Input();
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < n; x++)
		{
			int move_current = Dfs(y, x);
			move_max = max(move_max, move_current);
		}
	}
	cout << move_max << "\n";
	return 0;
}