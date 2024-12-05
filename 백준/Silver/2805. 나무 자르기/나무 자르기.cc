#include <iostream>
using namespace std;

int n, m;
int trees[1000000];
int tree_max;

void Input()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> trees[i];
		if (trees[i] > tree_max)
		{
			tree_max = trees[i];
		}
	}
}

long long CutTrees(int height)
{
	long long sum_trees = 0;
	for (int i = 0; i < n; i++)
	{
		int left_over = trees[i] - height;
		if (left_over > 0)
		{
			sum_trees += left_over;
		}
	}
	return sum_trees;
}

int Bisearch()
{
	int start = 0;
	int end = tree_max;
	while (start <= end)
	{
		int mid = (start + end) / 2;
		long long left_over = CutTrees(mid);
		if (left_over < m)// 나무가 적게 나오면 높이를 낮추고, 많이 나오면 높이를 높여야 함, 같게 나오면 높이를 높여봐야 함
		{
			end = mid - 1;
		}
		else if (left_over >= m)
		{
			start = mid + 1;
		}
	}
	return end;
}

int main()
{
	Input();
	int ans = Bisearch();
	cout << ans << "\n";
	return 0;
}