#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct Node
{
	int y, x;
};

struct PersonDist
{
	int person, dist;
	bool operator < (PersonDist right) const
	{
		if (dist < right.dist) return false;
		if (dist > right.dist) return true;
		if (person < right.person) return false;
		if (person > right.person) return true;
		return false;
	}
};

int T;
int N;
vector<Node> people;
Node stairs[2];
int time_stairs[2];
int dat[10];
int dists[2][10];
int time_min;

void Init()
{
	people.clear();
	for (int i = 0; i < 10; i++)
	{
		dat[i] = 0;
	}
	time_stairs[0] = 0;
	time_stairs[1] = 0;
	time_min = 213456789;
}

void Input()
{
	cin >> N;
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			int cur;
			cin >> cur;
			if (cur == 0)
			{
				continue;
			}
			else if (cur == 1)
			{
				people.push_back({ y, x });
			}
			else
			{
				if (time_stairs[0] == 0)
				{
					stairs[0] = { y, x };
					time_stairs[0] = cur;
				}
				else
				{
					stairs[1] = { y, x };
					time_stairs[1] = cur;
				}
			}
		}
	}
}

void CalDist()
{
	for (int i = 0; i < people.size(); i++)
	{
		for (int j = 0; j < 2; j++)
		{
			int dist = abs(people[i].y - stairs[j].y) + abs(people[i].x - stairs[j].x);
			dists[j][i] = dist;
		}
	}
}

int CalTime()
{
	priority_queue<PersonDist> personDist[2];
	for (int i = 0; i < people.size(); i++)
	{
		if (dat[i] == 0)
		{
			personDist[0].push({ i, dists[0][i] });
		}
		else
		{
			personDist[1].push({ i, dists[1][i] });
		}
	}
	vector<int> time_end[2];
	int time_total[2] = { 0, 0 };
	int time_wait[2] = { 0, 0 };
	for (int i = 0; i < 2; i++)
	{
		while (!personDist[i].empty())
		{
			int current_dist = personDist[i].top().dist;
			personDist[i].pop();
			time_total[i] = current_dist + time_stairs[i];
			if (time_end[i].size() >= 3)
			{
				time_wait[i] = time_end[i][time_end[i].size() - 3] - current_dist;
			}
			if (time_wait[i] < 1) // 대기시간의 최솟값은 1
			{
				time_wait[i] = 1;
			}
			time_total[i] += time_wait[i];
			time_end[i].push_back(time_total[i]);
		}
	}
	return max(time_total[0], time_total[1]);
}

void Dfs(int level)
{
	if (level == people.size())
	{
		int time_current = CalTime();
		if (time_current < time_min)
		{
			time_min = time_current;
		}
		return;
	}
	for (int i = 0; i < 2; i++)
	{
		dat[level] = i;
		Dfs(level + 1);
	}
}

int main()
{
	// freopen("sample.txt", "r", stdin);
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++)
	{
		Init();
		Input();
		CalDist();
		Dfs(0);
		cout << "#" << test_case << " " << time_min << "\n";
	}
	return 0;
}