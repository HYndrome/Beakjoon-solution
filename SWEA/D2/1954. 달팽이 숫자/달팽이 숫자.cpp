#include <iostream>;
using namespace std;


int arr_N[10][10];
int N;
int path_x[4] = { 1, 0 , -1, 0 };
int path_y[4] = { 0, 1, 0, -1 };

void Snail(int x, int y, int current, int path)
{	
	arr_N[y][x] = current;
	int nx = x + path_x[path];
	int ny = y + path_y[path];
	if (nx >= 0 && nx < N && ny >= 0 && ny < N && arr_N[ny][nx] == 0)
	{
		Snail(nx, ny, ++current, path);
	}
	else
	{
		int d = 1;
		while (d <= 3)
		{
			path = (path + 1) % 4;
			nx = x + path_x[path];
			ny = y + path_y[path];
			if (nx >= 0 && nx < N && ny >= 0 && ny < N && arr_N[ny][nx] == 0)
			{
				Snail(nx, ny, ++current, path);
			}
			d++;
		}
	}
}

int main()
{
	int cnt_T;
	cin >> cnt_T;
	for (int T = 0; T < cnt_T; T++)
	{
		cin >> N;
		// 배열 초기화
		for (int x = 0; x < N; x++)
		{
			for (int y = 0; y < N; y++)
			{
				arr_N[y][x] = 0;
			}
		}
		// DFS
		Snail(0, 0, 1, 0);
		// 출력
		cout << "#" << T + 1 << "\n";
		for (int y = 0; y < N; y++)
		{
			for (int x = 0; x < N; x++)
			{
				cout << arr_N[y][x] << " ";
			}
			cout << "\n";
		}
	}

	return 0;
}