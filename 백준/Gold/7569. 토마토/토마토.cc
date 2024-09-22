#include <iostream>
#include <queue>
using namespace std;

struct Tomato
{
	int z, y, x;
};

int M, N, H;
int tomatoes[100][100][100];
int dz[] = {1, -1, 0, 0, 0, 0};
int dy[] = { 0, 0, 1, -1, 0, 0 };
int dx[] = { 0, 0, 0, 0, 1, -1 };

queue<Tomato> que;


void Input();
void Ripe();
int CheckTomatoes();

int main()
{
	Input();
	Ripe();
	int ans = CheckTomatoes();
	cout << ans << "\n";
	return 0;
}

void Input()
{
	cin >> M >> N >> H;
	for (int z = 0; z < H; z++)
	{
		for (int y = 0; y < N; y++)
		{
			for (int x = 0; x < M; x++)
			{
				int tomato;
				cin >> tomato;
				tomatoes[z][y][x] = tomato;
				if (tomato == 1)
				{
					que.push({ z, y, x });
				}
			}
		}
	}
}

void Ripe()
{
	while (!que.empty())
	{
		Tomato current = que.front();
		que.pop();
		for (int i = 0; i < 6; i++)
		{
			int nz = current.z + dz[i];
			int ny = current.y + dy[i];
			int nx = current.x + dx[i];
			if (nz < 0 || nz >= H || ny < 0 || ny >= N || nx < 0 || nx >= M)
				continue;
			if (tomatoes[nz][ny][nx] != 0)
				continue;
			que.push({ nz, ny, nx });
			tomatoes[nz][ny][nx] = tomatoes[current.z][current.y][current.x] + 1;
		}
	}
}

int CheckTomatoes()
{
	int date_max = 0;
	for (int z = 0; z < H; z++)
	{
		for (int y = 0; y < N; y++)
		{
			for (int x = 0; x < M; x++)
			{
				int tomato = tomatoes[z][y][x];
				if (tomato > date_max)
				{
					date_max = tomato;
				}
				if (tomato == 0)
				{
					return -1;
				}
			}
		}
	}
	return date_max - 1;
}