#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Node
{
	int y, x;
};

int T;
int N, M, R, C, L;
vector<int> dy[8] = { {}, {1, 0, -1, 0 }, { 1, -1}, {0, 0}, {0, -1}, {1, 0}, {1, 0}, {-1, 0} }; // 파이프 종류
vector<int> dx[8] = { {}, {0, 1, 0, -1}, {0, 0}, {1, -1}, {1, 0}, {0, 1}, {0, -1}, {0, -1} };
int graph[51][51];
int visited[51][51];

void Init()
{
	for (int y = 0; y < 51; y++) // visited 초기화
	{
		for (int x = 0; x < 51; x++)
		{
			visited[y][x] = 0;
		}
	}
}

void Input()
{
	cin >> N >> M >> R >> C >> L;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < M; x++)
		{
			cin >> graph[y][x];
		}
	}
}

int Bfs(int y, int x, int move)
{
	visited[y][x] = 1; // 시작점
	int cnt = 1; // 탈주범이 위치할 수 있는 개수
	queue<Node> q;
	q.push({ y, x });
	while (!q.empty())
	{
		Node current = q.front();
		q.pop();
		int pipe_current = graph[current.y][current.x];
		if (visited[current.y][current.x] == move) // 소요시간만큼 탐색한 경우 종료
		{
			break;
		}
		for (int i = 0; i < dy[pipe_current].size(); i++) // 파이프 방향으로 탐색
		{
			int ny = current.y + dy[pipe_current][i];
			int nx = current.x + dx[pipe_current][i];
			if (ny >= N || nx >= M || ny < 0 || nx < 0) // 그래프 범위 밖 
			{
				continue;
			}
			if (visited[ny][nx] != 0) // 이미 방문한 곳
			{
				continue;
			}
			// 파이프 모양 비교 - 이어지는 곳은 현재 파이프가 향하고 있는 반대 방향이 열려있어야 함
			int pipe_next = graph[ny][nx];
			int flag_connected = 0; // true - 파이프 간 연결 됨
			for (int j = 0; j < dy[pipe_next].size(); j++)
			{
				if (dy[pipe_current][i] == -dy[pipe_next][j] && dx[pipe_current][i] == -dx[pipe_next][j])
				{
					flag_connected = 1;
					break;
				}
			}
			if (flag_connected == 0)
			{
				continue;
			}
			visited[ny][nx] = visited[current.y][current.x] + 1;
			cnt++;
			q.push({ ny, nx });
		}
	}
	return cnt;
}


int main()
{
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++)
	{
		Init();
		Input();
		int ans = Bfs(R, C, L);
		cout << "#" << test_case << " " << ans << "\n";
	}
	return 0;
}