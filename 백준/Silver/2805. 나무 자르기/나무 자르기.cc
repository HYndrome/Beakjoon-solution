#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<int> trees;

void Input();

long long CutTree(int height);

int BiSearch();

int main()
{
	int ans;
	Input();
	ans = BiSearch();
	cout << ans << "\n";
	return 0;
}

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

long long CutTree(int height)
{
	long long cnt = 0;
	for (int i = 0; i < N; i++)
	{
		int tree_taken = trees[i] - height;
		if (tree_taken > 0)
		{
			cnt += tree_taken;
		}
	}

	return cnt;
}

int BiSearch()
{
	int start = 0;
	int end = 2000000000;
	while (start <= end)
	{
		int mid = (start + end) / 2;
		long long cnt_current = CutTree(mid);
		if (cnt_current < M)
			end = mid - 1;
		else if (cnt_current >= M)
			start = mid + 1;
	}
	return end;
}