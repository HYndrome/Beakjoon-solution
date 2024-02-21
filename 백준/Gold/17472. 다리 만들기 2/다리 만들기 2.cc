#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct Node 
{
	int y, x;
};

struct Edge
{
	int n1, n2, cost;
};

int dy[] = { 1, 0, -1 , 0 };
int dx[] = { 0, 1, 0, -1 };
int N, M;
int graph[10][10];
int map_island[10][10];
int island_no = 0;
vector<Edge> edges;
int arr_islands[7];

void Input()
{
	cin >> N >> M;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < M; x++)
		{
			cin >> graph[y][x];
		}
	}
}

void PaintIsland(int y, int x)
{
	if (graph[y][x] == 0) // 섬이 아닌곳
	{
		return;
	}
	if (map_island[y][x] != 0) // 이미 탐색한 섬
	{
		return;
	}
	island_no += 1;
	map_island[y][x] = island_no;
	queue<Node> q;
	q.push({ y, x });
	while (!q.empty())
	{
		Node current = q.front();
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int ny = current.y + dy[i];
			int nx = current.x + dx[i];
			if (ny >= N || nx >= M || ny < 0 || nx < 0)
			{
				continue;
			}
			if (graph[ny][nx] != 1) // 탐색종료조건: 섬이 아닌 곳
			{
				continue;
			}
			if (map_island[ny][nx] != 0) // 탐색종료조건: 이미 섬으로 탐색된 곳
			{
				continue;
			}
			map_island[ny][nx] = island_no;
			q.push({ ny, nx });
		}
	}

}

void PaintIslands()
{
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < M; x++)
		{
			PaintIsland(y, x);
		}
	}
}

void CalCostIsland(int y, int x)
{
	if (map_island[y][x] == 0) // 섬 위가 아닌 경우 종료
	{
		return;
	}
	// 해당 지점에서 상하좌우 탐색, 빈곳이 있을 경우 해당 방향으로 쭉 확장해서
	// 제일 처음 만나는 섬과 거리 확인
	for (int i = 0; i < 4; i++)
	{
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (ny >= N || nx >= M || ny < 0 || nx < 0)
		{
			continue;
		}
		if (map_island[ny][nx] != 0)
		{
			continue;
		}
		int cost = 0;
		while (1)
		{
			ny = ny + dy[i];
			nx = nx + dx[i];
			cost++;
			if (ny >= N || nx >= M || ny < 0 || nx < 0)
			{
				break;
			}
			if (map_island[ny][nx] != 0)
			{
				edges.push_back({ map_island[y][x], map_island[ny][nx], cost });
				break;
			}
		}
	}
}

void CalCostIslands()
{
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < M; x++)
		{
			CalCostIsland(y, x);
		}
	}
}

bool CmpCost(Edge left, Edge right)
{
	return left.cost < right.cost;
}

void InitArr()
{
	for (int i = 0; i < 7; i++)
	{
		arr_islands[i] = i;
	}
}

int FindUnion(int tar)
{
	if (tar == arr_islands[tar])
	{
		return tar;
	}
	int ret = FindUnion(arr_islands[tar]);
	arr_islands[tar] = ret;
	return ret;
}

void SetUnion(int a, int b)
{
	int t1 = FindUnion(a);
	int t2 = FindUnion(b);
	if (t1 == t2)
	{
		return;
	}
	arr_islands[t2] = t1;
}

int Kruskal()
{
	int cnt = 0;
	int cost_sum = 0;
	InitArr();
	sort(edges.begin(), edges.end(), CmpCost); // edge들 cost별로 정렬
	for (Edge edge : edges)
	{
		if (FindUnion(edge.n1) == FindUnion(edge.n2))
		{
			continue;
		}
		if (edge.cost < 2) //다리의 길이는 2 이상
		{
			continue;
		}
		SetUnion(edge.n1, edge.n2);
		cnt++;
		cost_sum += edge.cost;
		if (cnt == island_no - 1)
		{
			return cost_sum;
		}
	}
	return -1;
}

int main()
{
	Input();
	// 섬에 번호를 붙이기
	PaintIslands();
	// 섬 간 거리 구하기
	CalCostIslands();
	// 크루스칼로 스패닝 트리 + 다리 길이는 1이될 수 없음
	int ans = Kruskal();
	cout << ans;
	return 0;
}