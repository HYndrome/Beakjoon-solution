#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Node
{
	int y, x;
};

int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};
int n, m;
int graph[1000][1000];
int n_team = 0;
int graph_visited[1000][1000];
int graph_cnt[1000][1000];
int graph_result[1000][1000];

void Input()
{
	cin >> n >> m;
	for (int y = 0; y < n; y++)
	{
		string line_current;
		cin >> line_current;
		for (int x = 0; x < m; x++)
		{
			graph[y][x] = line_current[x] - '0';
		}
	}
}

void BfsAdjacent(int y, int x)
{
	if (graph[y][x] != 0 || graph_visited[y][x] != 0)
	{
		return;
	}
	n_team += 1;
	graph_visited[y][x] = n_team;
	int cnt_team = 1;
	queue<Node> que;
	que.push({ y, x });
	vector<Node> team_visited;
	team_visited.push_back({ y, x });
	while (!que.empty())
	{
		Node current = que.front();
		que.pop();
		for (int i = 0; i < 4; i++)
		{
			int ny = current.y + dy[i];
			int nx = current.x + dx[i];
			if (ny < 0 || ny >= n || nx < 0 || nx >= m)
			{
				continue;
			}
			if (graph[ny][nx] != 0)
			{
				continue;
			}
			if (graph_visited[ny][nx] != 0)
			{
				continue;
			}
			cnt_team += 1;
			que.push({ ny, nx });
			graph_visited[ny][nx] = n_team;
			team_visited.push_back({ ny, nx });
		}
	}
	for (int i = 0; i < team_visited.size(); i++)
	{
		Node node_cnt = team_visited[i];
		graph_cnt[node_cnt.y][node_cnt.x] = cnt_team;
	}
}

void FindAdjacent()
{
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < m; x++)
		{
			BfsAdjacent(y, x);
		}
	}
}

void BreakWall(int y, int x)
{
	if (graph[y][x] != 1)
	{
		return;
	}
	int cnt = 1;
	vector<int> team_visited;
	for (int i = 0; i < 4; i++)
	{
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (ny < 0 || ny >= n || nx < 0 || nx >= m)
		{
			continue;
		}
		// 방문했던 팀인지
		bool flag_visited = false;
		int team_current = graph_visited[ny][nx];
		for (int j = 0; j < team_visited.size(); j++)
		{
			if (team_current == team_visited[j])
			{
				flag_visited = true;
				break;
			}
		}
		if (flag_visited)
		{
			continue;
		}
		cnt += graph_cnt[ny][nx];
		team_visited.push_back(team_current);
	}
	graph_result[y][x] = cnt;
}

void BreakWalls()
{
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < m; x++)
		{
			BreakWall(y, x);
		}
	}
}

void Print()
{
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < m; x++)
		{
			cout << graph_result[y][x] % 10;
		}
		cout << "\n";
	}
}

int main()
{
	Input();
	FindAdjacent();
	BreakWalls();
	Print();
	return 0;
}