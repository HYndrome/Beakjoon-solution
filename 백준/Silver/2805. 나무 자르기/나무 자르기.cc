#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<int> trees;
int height_cut;

void Input()
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		int tree;
		cin >> tree;
		trees.push_back(tree);
	}
}

void UpdateHeightCut(int start, int end)
{
	long long sum_tree = 0;
	int mid = (start + end) / 2;
	height_cut = mid;
	if (start > mid)
	{
		return;
	}
	for (int i = 0; i < trees.size(); i++)
	{
		if (trees[i] - mid > 0)
		{
			sum_tree += trees[i] - mid;
		}
	}
	if (sum_tree >= M)
	{
		UpdateHeightCut(mid + 1, end);
	}
	if (sum_tree < M)
	{
		UpdateHeightCut(start, mid - 1);
	}
}

int main()
{
	Input();
	UpdateHeightCut(1,2000000000);
	cout << height_cut;
	return 0;
}