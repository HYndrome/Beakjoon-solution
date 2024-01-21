#include <iostream>;
using namespace std;

int main()
{
	int hr, min, time_cooking;
	cin >> hr >> min >> time_cooking;
	int min_total = hr * 60 + min + time_cooking;
	int hr_out = (min_total / 60) % 24;
	int min_out = min_total % 60;
	cout << hr_out << " " << min_out;
	return 0;
}