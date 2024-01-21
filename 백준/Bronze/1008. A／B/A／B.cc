#include <iostream>
using namespace std;

int main()
{
	double  num_1, num_2;
	cin >> num_1 >> num_2;

	cout << fixed; // 고정 소수점 표기로 전환
	cout.precision(12); // 실수 전체 자리수 중 n 자리까지 표현
	cout << (double)(num_1 / num_2);
	
	return 0;
}