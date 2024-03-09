#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
using namespace std;

struct Edge
{
	int num, cnt;
	bool operator < (Edge right) const
	{
		if (cnt < right.cnt) return false;
		if (cnt > right.cnt) return true;
		return false;
	}
};
int T;
int N, O, M;
vector<int> numbers;
vector<int> operations;
int W;
int visited[1000];
int datCombNums[3];
int max_digit;

void Init()
{
	numbers.clear();
	operations.clear();
	for (int i = 0; i < 1000; i++)
	{
		visited[i] = 0;
	}
}

void Input()
{
	cin >> N >> O >> M;
	for (int i = 0; i < N; i++)
	{
		int number;
		cin >> number;
		numbers.push_back(number);
	}
	for (int i = 0; i < O; i++)
	{
		int operation;
		cin >> operation;
		operations.push_back(operation);
	}
	cin >> W;
}

void DfsComb(int level, int level_max)
{
	if (level == level_max)
	{
		if (datCombNums[level_max - 1] == 0) // 최대 자리수가 0인 경우 제외
		{
			return;
		}
		int num_comb = 0;
		for (int i = 0; i < level_max; i++)
		{
			num_comb += datCombNums[i] * pow(10, i);
		}
		visited[num_comb] = level_max;
		return;
	}
	for (int i = 0; i < numbers.size(); i++)
	{
		datCombNums[level] = numbers[i];
		DfsComb(level + 1, level_max);
	}
}

void CombNums()
{ 
	max_digit = 3; // 숫자는 최대 3자리 수
	for (int i = 1; i <= max_digit; i++)
	{
		DfsComb(0, i);
	}
	// 0 하나 체크
	for (int i = 0; i < numbers.size(); i++)
	{
		if (numbers[i] == 0)
		{
			visited[0] = 1;
		}
	}
}

int DijkNums()
{
	priority_queue<Edge> pq;
	int INF = 213456789;
	vector<Edge> numDists;
	for (int i = 0; i < 1000; i++)
	{
		if (visited[i] == 0)
		{
			visited[i] = INF;
		}
		else
		{
			numDists.push_back({ i, visited[i] });
			pq.push({ i, visited[i]});
		}
	}
	while (!pq.empty())
	{
		Edge current = pq.top();
		pq.pop();
		for (int i = 0; i < numDists.size(); i++)
		{
			for (int o = 0; o < operations.size(); o++)
			{
				int n_value; // 연산 후의 수
				if (operations[o] == 1)
				{
					n_value = current.num + numDists[i].num;
				}
				if (operations[o] == 2)
				{
					n_value = current.num - numDists[i].num;
				}
				if (operations[o] == 3)
				{
					n_value = current.num * numDists[i].num;
				}
				if (operations[o] == 4)
				{
					if (numDists[i].num == 0)
					{
						n_value = INF;
					}
					else
					{
						n_value = current.num / numDists[i].num;
					}
				}
				if (n_value > 999 || n_value < 0) // 범위 밖의 수
				{
					continue;
				}
				int n_cnt; // 누르는 횟수 이 조건 때문에 시간 초과 피할 수 있을 듯
				n_cnt = current.cnt + numDists[i].cnt + 1;
				if (n_cnt > M - 1) // 누르는 횟수 넘어가는 경우 마지막에 = 추가 -1
				{
					continue;
				}
				if (n_cnt >= visited[n_value]) // 기존 값보다 더 많이 누른 경우
				{
					continue;
				}
				pq.push({ n_value, n_cnt });
				visited[n_value] = n_cnt;
			}
		}
	}
	if (visited[W] == INF)
	{
		return -1;
	}
	return visited[W] + 1; // = 계산 포함
}

int main()
{
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++)
	{
		Init();
		Input();
		CombNums(); // 연산자 없이 숫자 경우의 수
		if (visited[W] != 0)
		{
			int ans = visited[W];
			if (ans > M)
			{
				ans = -1;
			}
			cout << "#" << test_case << " " << ans << "\n";
			continue;
		}
		int ans = DijkNums();
		cout << "#" << test_case << " " << ans << "\n";
	}
	return 0;
}