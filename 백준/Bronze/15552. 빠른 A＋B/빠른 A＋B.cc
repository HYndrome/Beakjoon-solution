#include <iostream>
using namespace std;

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int test_case = 0; test_case < T; test_case++)
	{
		int a, b;
		cin >> a >> b;
		cout << a + b << "\n";
	}
	return 0;
}