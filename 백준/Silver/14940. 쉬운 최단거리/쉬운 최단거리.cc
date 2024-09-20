#include <iostream>
#include <queue>

using namespace std;

struct Node
{
	int y;
	int x;
};

int N, M;
int graph[1000][1000];
int graph_distance[1000][1000];
int start_y, start_x;
int dy[] = { 1, 0, -1, 0 };
int dx[] = { 0, 1, 0, -1 };

void Input();
void CalDistance(int start_y, int start_x);
void PrintDistance();

int main()
{	
	Input();
	CalDistance(start_y, start_x);
	PrintDistance();
	return 0;
}

void Input()
{
	cin >> N >> M;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < M; x++)
		{
			int ground_status;
			cin >> ground_status;
			graph[y][x] = ground_status;
			if (ground_status != 0)
			{
				graph_distance[y][x] = -1;
			}
			if (ground_status == 2)
			{
				start_y = y;
				start_x = x;
			}
		}
	}
}

void CalDistance(int start_y, int start_x)
{
	graph_distance[start_y][start_x] = 0;
	queue<Node> que;
	que.push({ start_y, start_x });
	while (!que.empty())
	{
		Node current = que.front();
		que.pop();
		for (int i = 0; i < 4; i++)
		{
			int ny = current.y + dy[i];
			int nx = current.x + dx[i];
			if (ny < 0 || ny >= N || nx < 0 || nx >= M)
			{
				continue;
			}
			if (graph_distance[ny][nx] != -1)
			{
				continue;
			}
			que.push({ ny, nx });
			graph_distance[ny][nx] = graph_distance[current.y][current.x] + 1;
		}
	}
}

void PrintDistance()
{
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < M; x++)
		{
			cout << graph_distance[y][x] << " ";
		}
		cout << "\n";
	}
}