#include <iostream>
#include <vector>
using namespace std;

struct Node
{
	int y, x;
};


int dy[] = { 1, 0, -1, 0 };
int dx[] = { 0, 1, 0, -1 };
int T;
int N, K;
vector<Node> peaks;
int height_max;
int graph[9][9];
int visited[9][9];
int path_max;

void Init()
{
	height_max = 0;
	while (!peaks.empty())
	{
		peaks.pop_back();
	}
	path_max = 0;
}

void Input()
{
	cin >> N >> K;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			int height;
			cin >> height;
			graph[y][x] = height;
			if (height > height_max)
			{
				height_max = height;
			}
		}
	}
}

void FindHighest()
{
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			if (graph[y][x] == height_max)
			{
				peaks.push_back({ y, x });
			}
		}
	}
}

void InitVisited()
{
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			visited[y][x] = 0;
		}
	}
}

void DfsFindPath(int level, int y, int x, int punch)
{
	if (level > path_max)
	{
		path_max = level;
	}
	for (int i = 0; i < 4; i++)
	{
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (ny >= N || nx >= N || ny < 0 || nx < 0)
		{
			continue;
		}
		if (visited[ny][nx] == 1)
		{
			continue;
		}
		if (graph[ny][nx] < graph[y][x])
		{
			visited[ny][nx] = 1;
			DfsFindPath(level + 1, ny, nx, punch);
			visited[ny][nx] = 0;
		}
		else // 부숴야하는 경우
		{
			if (graph[ny][nx] - graph[y][x] + 1 <= punch) // 부술 수 있는 경우
			{
				visited[ny][nx] = 1;
				int height_ny_nx = graph[ny][nx];
				graph[ny][nx] = graph[y][x] - 1;
				DfsFindPath(level + 1, ny, nx, 0); // 이제 못부숨
				visited[ny][nx] = 0;
				graph[ny][nx] = height_ny_nx;
			}
		}
	}
}

int main()
{
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++)
	{
		Init();
		Input();
		FindHighest();
		for (int i = 0; i < peaks.size(); i++)
		{
			InitVisited();
			Node peak = peaks[i];
			visited[peak.y][peak.x] = 1;
			DfsFindPath(1, peak.y, peak.x, K);
		}
		cout << "#" << test_case << " " << path_max << "\n";
	}
	return 0;
}