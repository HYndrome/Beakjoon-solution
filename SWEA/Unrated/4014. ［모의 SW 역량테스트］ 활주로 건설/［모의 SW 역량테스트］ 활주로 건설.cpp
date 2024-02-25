#include <iostream>
using namespace std;

int dy[] = { 1, 0 };
int dx[] = { 0, 1 };
int T;
int N, X;
int graph[21][21];
int cnt_airstrip;

void Init()
{
	for (int y = 0; y < 21; y++) // 그래프 초기화
	{
		for (int x = 0; x < 21; x++)
		{
			graph[y][x] = 0;
		}
	}
	cnt_airstrip = 0; // cnt_airstrip 초기화
}

void Input()
{
	cin >> N >> X;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			cin >> graph[y][x];
		}
	}
}

void CheckAirStrip(int y_start, int x_start, int direct)
{
	int y = y_start;
	int x = x_start;
	int flag_down = 0; // 내려갔다가 올라가는 경우에 대한 처리
	if (direct == 0) // y방향
	{
		while (y < N - X)
		{
			int ny = y + X * dy[direct];
			// 1 오르막처리 - 이건 안되면 종료되어야 함
			if (graph[ny][x] - graph[y][x] == 1) // 1칸 오르막
			{
				if (flag_down)
				{
					return;
				}
				for (int y_eval = y + 1; y_eval < ny; y_eval++)
				{
					if (graph[y_eval][x] == graph[y][x])
					{
						continue;
					}
					return;
				}
				y = ny;
				flag_down = 0;
			}
			// 2 오르막을 제외했을 때 평행한 길이면 직진해야함
			else if (graph[y + 1][x] - graph[y][x] == 0)
			{
				y++;
				flag_down = 0;
			}
			// 3 평행한 길이 아니면서 내리막길 처리를 할 수 있을 때 내려감
			else if (graph[ny][x] - graph[y][x] == -1) // 1칸 내리막
			{
				for (int y_eval = y + 1; y_eval < ny; y_eval++)
				{
					if (graph[y_eval][x] == graph[ny][x])
					{
						continue;
					}
					return; // 이미 평행한 길에 대해서 처리를 했으므로 못내려갈 경우 ret
				}
				y = ny;
				flag_down = 1;
			}
			else // 1 초과로 차이나는 경우
			{
				return;
			}
		}
		while (y < N - 1)
		{
			if (graph[y + 1][x] - graph[y][x] == 0)
			{
				y++;
			}
			else
			{
				break;
			}
		}
		if (y == N - 1)
		{
			cnt_airstrip++;
		}
	}
	if (direct == 1) // x방향
	{
		while (x < N - X)
		{
			int nx = x + X * dx[direct];
			// 1 오르막처리 - 이건 안되면 종료되어야 함
			if (graph[y][nx] - graph[y][x] == 1) // 1칸 오르막
			{
				if (flag_down)
				{
					return;
				}
				for (int x_eval = x + 1; x_eval < nx; x_eval++)
				{
					if (graph[y][x_eval] == graph[y][x])
					{
						continue;
					}
					return;
				}
				x = nx;
				flag_down = 0;
			}
			// 2 오르막을 제외했을 때 평행한 길이면 직진해야함
			else if (graph[y][x + 1] - graph[y][x] == 0)
			{
				x++;
				flag_down = 0;
			}
			// 3 평행한 길이 아니면서 내리막길 처리를 할 수 있을 때 내려감
			else if (graph[y][nx] - graph[y][x] == -1) // 1칸 내리막
			{
				for (int x_eval = x + 1; x_eval < nx; x_eval++)
				{
					if (graph[y][x_eval] == graph[y][nx])
					{
						continue;
					}
					return; // 이미 평행한 길에 대해서 처리를 했으므로 못내려갈 경우 ret
				}
				x = nx;
				flag_down = 1;
			}
			else // 1 초과로 차이나는 경우
			{
				return;
			}
		}
		while (x < N - 1)
		{
			if (graph[y][x + 1] - graph[y][x] == 0)
			{
				x++;
			}
			else
			{
				break;
			}
		}
		if (x == N - 1)
		{
			cnt_airstrip++;
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
		for (int i = 0; i < N; i++)
		{
			CheckAirStrip(0, i, 0); // y방향 탐색
			CheckAirStrip(i, 0, 1); // x방향 탐색
			int a = 0;
		}
		cout << "#" << test_case << " " << cnt_airstrip << "\n";
	}
	return 0;
}