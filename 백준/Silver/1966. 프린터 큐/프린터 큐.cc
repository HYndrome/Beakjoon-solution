#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

struct Document
{
	int index;
	int weight;
};

int T;
int N, M;
deque<Document> docs;
deque<int> weights;

void Init()
{
	docs.clear();
	weights.clear();
}

void Input()
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		int weight;
		cin >> weight;
		docs.push_back({ i, weight });
		weights.push_back(weight);
	}
}

bool CmpWeight(int left, int right)
{
	if (left < right) return false;
	if (left > right) return true;
	return false;
}

int FIFOPrint()
{
	int seq_print = 1;
	while (!docs.empty())
	{
		if (docs.front().weight == weights.front())
		{
			if (docs.front().index == M)
			{
				return seq_print;
			}
			docs.pop_front();
			weights.pop_front();
			seq_print++;
		}
		else
		{
			Document doc_cur = docs.front();
			docs.pop_front();
			docs.push_back(doc_cur);
		}
	}
}

int main()
{
	cin >> T;
	for (int test_case = 0; test_case < T; test_case++)
	{
		Init();
		Input();
		sort(weights.begin(), weights.end(), CmpWeight);

		int b = 0;
		int seq = FIFOPrint();
		cout << seq << "\n";
		int a = 0;
	}
	return 0;
}