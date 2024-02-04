#include <iostream>
#include<deque>
using namespace std;

int T;
int N;
int D;
int graph[500][500];
deque<int> dq[500];

void Init()
{
}

void Input()
{
	cin >> N >> D;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			cin >> graph[y][x];
		}
	}
}

void CutBoundary(int size) // graph 테두리를 잘라서 level 별로 deque에 push하는 함수
{
	int mid = size / 2;
	int level = mid;
	while (level > 0)
	{
		for (int x = mid - level; x < mid + level; x = x + level)
		{
			dq[level].push_back(graph[mid - level][x]);
		}
		for (int y = mid - level; y < mid + level; y = y + level)
		{
			dq[level].push_back(graph[y][mid + level]); 
		}
		for (int x = mid + level; x > mid - level; x = x - level)
		{
			dq[level].push_back(graph[mid + level][x]);
		}
		for (int y = mid + level; y > mid - level; y = y - level)
		{
			dq[level].push_back(graph[y][mid - level]);
		}
		level--;
	}
	// 가운데 부분 처리
	dq[0].push_back(graph[mid][mid]);
}

void Rotate(int size, int degree)
{
	// 회전 처리
	int level_in = size / 2;
	if (degree < 0)
	{
		degree = 360 + degree;
	}
	int move = degree / 45;
	int mid = size / 2;
	for (int level = 0; level <= level_in; level++)
	{
		int rotate_dq = move;
 		while (rotate_dq)
		{
			int num_last = dq[level].back();
			dq[level].pop_back();
			dq[level].push_front(num_last);
			rotate_dq--;
		}
	}
	// graph rewrite
	while (level_in > 0)
	{
		for (int x = mid - level_in; x < mid + level_in; x = x + level_in)
		{
			graph[mid - level_in][x] = dq[level_in].front();
			dq[level_in].pop_front();
		}
		for (int y = mid - level_in; y < mid + level_in; y = y + level_in)
		{
			graph[y][mid + level_in] = dq[level_in].front();
			dq[level_in].pop_front();
		}
		for (int x = mid + level_in; x > mid - level_in; x = x - level_in)
		{
			graph[mid + level_in][x] = dq[level_in].front();
			dq[level_in].pop_front();
		}
		for (int y = mid + level_in; y > mid - level_in; y = y - level_in)
		{
			graph[y][mid - level_in] = dq[level_in].front();
			dq[level_in].pop_front();
		}
		level_in--;
	}
	// 가운데 부분 처리
	graph[mid][mid] = dq[0].front();
	dq[0].pop_front();
}

void PrintGraph(int size)
{
	for (int y = 0; y < size; y++)
	{
		for (int x = 0; x < size; x++)
		{
			cout << graph[y][x] << " ";
		}
		cout << "\n";
	}
}
int main()
{
	cin >> T;
	for (int test_case = 0; test_case < T; test_case++)
	{
		Init();
		Input();
		CutBoundary(N);
		Rotate(N, D);
		PrintGraph(N);
	}
	return 0;
}