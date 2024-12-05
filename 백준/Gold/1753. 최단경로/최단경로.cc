#define INF 2134567890
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Edge {
	int v_end, cost;
	bool operator < (Edge right) const
	{
		if (cost > right.cost)
			return true;
		return false;
	}
};

int v, e, s;
vector<Edge> edges[20000];
int min_cost[20000];

void Input()
{
	cin >> v >> e;
	int s_input;
	cin >> s_input;
	s = s_input - 1;
	for (int i = 0; i < e; i++)
	{
		int v_start, v_end, cost;
		cin >> v_start >> v_end >> cost;
		edges[v_start - 1].push_back({ v_end - 1, cost });
	}
}

void Dijk(int s)
{
	// 거리 초기화
	for (int i = 0; i < v; i++)
	{
		min_cost[i] = INF;
	}
	priority_queue<Edge> pq;
	min_cost[s] = 0; // 시작점
	pq.push({ s, 0 });
	while (!pq.empty())
	{
		Edge current = pq.top();
		pq.pop();
		for (int i = 0; i < edges[current.v_end].size(); i++)
		{
			Edge next = edges[current.v_end][i];
			int next_cost = min_cost[current.v_end] + next.cost;
			if (next_cost >= min_cost[next.v_end])
			{
				continue;
			}
			min_cost[next.v_end] = next_cost;
			pq.push({ next.v_end, next_cost });
		}
	}
}

int main()
{
	Input();
	Dijk(s);
	for (int i = 0; i < v; i++)
	{
		if (min_cost[i] == INF)
		{
			cout << "INF\n";
		}
		else
		{
			cout << min_cost[i] << "\n";
		}
	}
	return 0;
}