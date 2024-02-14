#include <iostream>
#include <vector>
using namespace std;

struct Area {
	int x_start, y_start, x_end, y_end;
};

int N, M;
int graph[1025][1025];
vector<Area> areas;

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
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		areas.push_back({ y1 - 1, x1 - 1, y2 - 1, x2 - 1 });
	}
}

void PrefixSum() // 누적합 구하기 - y, x는 해당 행과 열까지 모두 더한 합
{
	if (N >= 2)
	{
		for (int y = 0; y < N; y++)
		{
			for (int x = 1; x < N; x++)
			{
				graph[y][x] = graph[y][x] + graph[y][x - 1];
			}
		}
		for (int x = 0; x < N; x++)
		{
			for (int y = 1; y < N; y++)
			{
				graph[y][x] = graph[y][x] + graph[y - 1][x];
			}
		}
	}
}
int main()
{
	Input();
	PrefixSum();
	for (int i = 0; i < areas.size(); i++)
	{
		int sum = 0;
		sum += graph[areas[i].y_end][areas[i].x_end]; // 전체 영역 더하기
		if (areas[i].x_start >= 1)
		{
			sum -= graph[areas[i].y_end][areas[i].x_start - 1]; // 왼쪽 영역 빼기
		}
		if (areas[i].y_start >= 1)
		{
			sum -= graph[areas[i].y_start - 1][areas[i].x_end]; // 위쪽 영역 빼기
		}
		if (areas[i].x_start >= 1 && areas[i].y_start >= 1)
		{
			sum += graph[areas[i].y_start - 1][areas[i].x_start - 1]; // 중첩 영역 더하기
		}
		cout << sum << "\n";
	}
	return 0;
}