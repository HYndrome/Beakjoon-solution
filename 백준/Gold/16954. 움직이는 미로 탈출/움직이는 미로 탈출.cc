#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

// 벽이 이동한 기록을 담는 벡터배열 그래프를 그리고
// 해당 그래프의 숫자와 욱제가 bfs 이동 수가 같으면 이동을 못함

struct Node {
	int y, x;
};

int dy[] = { 1, 1, 0, -1, -1, -1, 0, 1, 0 };
int dx[] = { 0, 1, 1, 1, 0, -1, -1, -1, 0 };
vector<int> graph_wall[8][8];
int flag_win;

void RecordWalls()
{
	for (int y = 0; y < 8; y++)
	{
		string walls;
		cin >> walls;
		for (int x = 0; x < 8; x++)
		{
			if (walls[x] == '#')
			{
				int cnt = 0;
				int y_current = y;
				while (y_current < 8)
				{
					graph_wall[y_current][x].push_back(cnt);
					cnt++;
					y_current++;
				}
			}
		}
	}
}

void Dfs(int y, int x, int level)
{
	if (level == 8) // 8턴이 지날 동안 생존하면 무조건 도착 가능
	{
		flag_win = 1;
		return;
	}

	int flag_on_wall = 0; // 지금 벽 위에 있을 경우
	{
		for (int i = 0; i < graph_wall[y][x].size(); i++)
		{
			if (graph_wall[y][x][i] == level)
			{
				flag_on_wall = 1;
				break;
			}
		}
	}
	if (flag_on_wall)
	{
		return;
	}

	for (int delta = 0; delta < 9; delta++)
	{
		int ny = y + dy[delta];
		int nx = x + dx[delta];
		if (ny >= 8 || nx >= 8 || ny < 0 || nx < 0)
		{
			continue;
		}
		int flag_block_wall = 0; // 지금 턴에 벽인 곳은 이동 불가능
		for (int i = 0; i < graph_wall[ny][nx].size(); i++)
		{
		
			if (graph_wall[ny][nx][i] == level)
			{
				flag_block_wall = 1;
				break;
			}
		}
		if (flag_block_wall)
		{
			continue;
		}
		Dfs(ny, nx, level + 1);
	}
}

int main()
{
	RecordWalls();
	Dfs(7, 0, 0);
	if (flag_win)
	{
		cout << 1;
	}
	else
	{
		cout << 0;
	}
	
	return 0;
}


				