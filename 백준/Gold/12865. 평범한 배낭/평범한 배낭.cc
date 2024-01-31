#include <iostream>
using namespace std;

// KnapSack 알고리즘 - 그림을 그리고 푸는게 간단
struct Item
{
	int W, V;
};

int backpack[100 + 1][100000 + 1 ]; // dp용 배열 설정
int N, K;
Item items[100 + 1];
int v_max = 0;

void Input()
{
	cin >> N >> K;
	for (int i = 1; i <= N; i++)
	{
		Item current;
		cin >> current.W >> current.V;
		items[i] = current;
	}
}

int Bigger(int a, int b)
{
	return (a > b) ? a : b;
}

int main()
{
	Input();
	for (int i = 1; i <= N; i++)
	{
		for (int w = 0; w < items[i].W; w++) // 해당 아이템의 무게 이전까지는 위의 아이템 행의 값을 그대로 가져옴
		{
			backpack[i][w] = backpack[i - 1][w];
		}
		for (int w = items[i].W; w <= K; w++)
		{
			// 해당 아이템을 사용하지 않은 값 vs 해당 아이템의 무게를 뺀 값 + 해당 아이템의 값
			backpack[i][w] = Bigger(backpack[i - 1][w], backpack[i - 1][w - items[i].W] + items[i].V);
		}
		// 무게를 모두 소진할 경우 중에서 최댓값이 존재
		if (backpack[i][K] > v_max)
		{
			v_max = backpack[i][K];
		}
	}
	cout << v_max;
	return 0;
}