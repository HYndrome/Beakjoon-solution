#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

struct Node
{
	int y, x;
};

struct Bridge
{
	int start, end, cost;
};

int n, m;
int graph[10][10];
int island[10][10];
int island_no = 0;
int dy[] = { 1, 0, -1, 0 };
int dx[] = { 0, 1, 0, -1 };
vector<Bridge> bridges;
int team[7];
int sum_cost = 0;
int sum_island = 0;


void Init()
{
	for (int i = 0; i < 7; i++)
	{
		team[i] = i;
	}
}

void Input()
{
	cin >> n >> m;
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < m; x++)
		{
			cin >> graph[y][x];
		}
	}
}

void FindIsland(int y_in, int x_in)
{
	if (graph[y_in][x_in] == 0 || island[y_in][x_in] != 0)
	{
		return;
	}
	island_no += 1;
	island[y_in][x_in] = island_no;
	queue<Node> que;
	que.push({ y_in, x_in });
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
			if (graph[ny][nx] != 1)
			{
				continue;
			}
			if (island[ny][nx] != 0)
			{
				continue;
			}
			island[ny][nx] = island_no;
			que.push({ ny, nx });
		}
	}
}

void FindIslands()
{
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < m; x++)
		{
			FindIsland(y, x);
		}
	}
}

void Print()
{
	for (int i = 0; i < bridges.size(); i++)
	{
		cout << bridges[i].start << " " << bridges[i].end << " " << bridges[i].cost << "\n";
	}
}

void FindRoute(int y_in, int x_in)
{
	if (island[y_in][x_in] == 0)
	{
		return;
	}
	int start = island[y_in][x_in];
	int cost;
	for (int i = 0; i < 4; i++) // 4방향 탐색
	{
		cost = 1;
		while (1)
		{
			int ny = y_in + cost * dy[i];
			int nx = x_in + cost * dx[i];
			if (ny < 0 || ny >= n || nx < 0 || nx >= m)
			{
				break;
			}
			if (island[ny][nx] == start)
			{
				break;
			}
			if (island[ny][nx] == 0)
			{
				cost += 1;
			}
			if (island[ny][nx] > 0)
			{
				cost -= 1;
				if (cost < 2)
				{
					break;
				}
				bridges.push_back({ start, island[ny][nx], cost });
				break;
			}
		}
	}
}

void FindRoutes()
{
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < m; x++)
		{
			FindRoute(y, x);
		}
	}
}

bool SortBridge(Bridge left, Bridge right)
{
	return left.cost < right.cost;
}

int Find(int member)
{
	if (member == team[member])
	{
		return member;
	}
	int boss = Find(team[member]);
	team[member] = boss;
	return boss;
}

void SetUnion(int member_1, int member_2)
{
	int boss_1 = Find(member_1);
	int boss_2 = Find(member_2);
	if (boss_1 == boss_2)
	{
		return;
	}
	team[boss_2] = boss_1;
}


int main()
{
	Init();
	Input();
	FindIslands();
	FindRoutes();
	sort(bridges.begin(), bridges.end(), SortBridge);
	// Print();
	for (Bridge bridge : bridges)
	{
		if (Find(bridge.start) == Find(bridge.end))
		{
			continue;
		}
		sum_cost += bridge.cost;
		SetUnion(bridge.start, bridge.end);
		sum_island += 1;
		// cout << bridge.start << " " << bridge.end << " " << bridge.cost << "\n";
		if (sum_island == island_no - 1)
		{
			break;
		}
	}
	if (sum_island == island_no - 1)
	{
		cout << sum_cost << "\n";
	}
	else
	{
		cout << -1 << "\n";
	}
	return 0;
}