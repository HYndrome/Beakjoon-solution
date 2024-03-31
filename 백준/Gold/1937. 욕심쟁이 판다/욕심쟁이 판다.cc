#include <iostream>
#include <algorithm>

using namespace std;

int dy[] = { 1, 0 , -1, 0 };
int dx[] = { 0, 1, 0, -1 };
int N;
int graph[500][500];
int dp[500][500]; // 해당 자리에서 가장 많이 움직일 수 칸 저장
int move_max = 0;


void Input()
{
	cin >> N;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			cin >> graph[y][x];
		}
	}
}

int Dfs(int y, int x)
{
	if (dp[y][x] == 0)
	{
		dp[y][x] = 1;
		for (int i = 0; i < 4; i++)
		{
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (ny >= N || ny < 0 || nx >= N || nx < 0)
			{
				continue;
			}
			if (graph[ny][nx] > graph[y][x])
			{
				dp[y][x] = max(dp[y][x], Dfs(ny, nx) + 1);
			}
		}
	}
	return dp[y][x];
}

void Print()
{
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			cout << dp[y][x] << " ";
		}
		cout << "\n";
	}
}
int main()
{
	Input();
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			move_max = max(move_max, Dfs(y, x));
		}
	}
	cout << move_max;

	// Print();
	return 0;
}