#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<int> graph[101];
int cnt_virus = 0;
int visited[101];

void Input()
{
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int node_1, node_2;
		cin >> node_1 >> node_2;
		graph[node_1].push_back(node_2);
		graph[node_2].push_back(node_1);
	}
}

void Virus(int node)
{
	for (int i = 0; i < graph[node].size(); i++)
	{
		int node_next = graph[node][i];
		if (visited[node_next] != 1)
		{
			visited[node_next] = 1;
			cnt_virus++;
			Virus(node_next);
		}
	}
}

int main()
{
	Input();
	visited[1] = 1;
	Virus(1);
	cout << cnt_virus << "\n";
	return 0;
}