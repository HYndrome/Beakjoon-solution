#include <iostream>
#include <vector>
#include <deque>
using namespace std;

struct Move
{
	int direction, size;
};
struct Cloud
{
	int y, x;
};

int dy[] = { 0, 0, -1, -1, -1, 0, 1, 1, 1 };
int dx[] = { 0, -1, -1, 0, 1, 1, 1, 0, -1 };
int dy_dup[] = { 1, -1, -1, 1 };
int dx_dup[] = { 1, 1, -1, -1 };
int N, M;
int graph[51][51];
vector<Move> moves;
deque<Cloud> clouds;
int clouds_before[51][51];


void Input()
{
	cin >> N >> M;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			cin >> graph[y][x];
		}
	}
	for (int i = 0; i < M; i++)
	{
		int direction, size;
		cin >> direction >> size;
		moves.push_back({ direction, size });
	}
}

void Bibaragi() // 4칸에 구름 생성
{
	clouds.push_back({ N - 1, 0 });
	clouds.push_back({ N - 1, 1 });
	clouds.push_back({ N - 2, 0 });
	clouds.push_back({ N - 2, 1 });
}

void MoveClouds(int direction, int size) // 모든 구름이 di 방향으로 si칸 이동한다
{
	for (int i = 0; i < clouds.size(); i++)
	{
		Cloud current = clouds.front();
		clouds.pop_front();
		int ny = (current.y + dy[direction] * size) % N;
		if (ny < 0) // -를 % 연산자로 처리할 경우 - 값이 나온다...!
		{
			ny += N;
		}
		int nx = (current.x + dx[direction] * size) % N;
		if (nx < 0)
		{
			nx += N;
		}
		clouds.push_back({ ny, nx });
	}
}

void Rain() // 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
{
	for (int i = 0; i < clouds.size(); i++)
	{
		graph[clouds[i].y][clouds[i].x]++;
	}
}

void DupWater() // 물복사버그 마법
{
	for (int i = 0; i < clouds.size(); i++)
	{
		int cnt = 0;
		for (int d = 0; d < 4; d++)
		{
			int ny = clouds[i].y + dy_dup[d];
			int nx = clouds[i].x + dx_dup[d];
			if (ny >= N || ny >= N || ny < 0 || nx < 0) // 대각선 범위 내
			{
				continue;
			}
			if (graph[ny][nx] == 0) // 대각선 물 확인
			{
				continue;
			}
			cnt++;
		}
		graph[clouds[i].y][clouds[i].x] += cnt;
	}
}

void MakeClouds()
{
	for (int i = 0; i < clouds.size(); i++) // 3에서 구름이 사라진 칸 기록
	{
		clouds_before[clouds[i].y][clouds[i].x] = 1;
	}
	int cnt_cloud_before = clouds.size();
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			if (graph[y][x] >= 2)
			{
				if (clouds_before[y][x] == 1) // 3에서 구름이 사라진 칸
				{
					continue;
				}
				clouds.push_back({ y, x }); // 구름 생성
				graph[y][x] -= 2; // 물의 양 2 줄어듦
			}
		}
	}
	// 구름 초기화
	for (int i = 0; i < cnt_cloud_before; i++)
	{
		clouds.pop_front();
	}
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			clouds_before[y][x] = 0;
		}
	}
}

int CountWater()
{
	int cnt = 0;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			cnt += graph[y][x];
		}
	}
	return cnt;
}

int main()
{
	Input();
	Bibaragi();
	for (int i = 0; i < moves.size(); i++)
	{
		MoveClouds(moves[i].direction, moves[i].size);
		Rain();
		DupWater();
		MakeClouds();
		int complete = 1;
	}
	cout << CountWater();
	return 0;
}