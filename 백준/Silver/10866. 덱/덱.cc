#include <iostream>
#include <deque>
using namespace std;

int main()
{
	int N;
	cin >> N;
	deque<int> dq;

	while (N--)
	{
		string command_in;
		cin >> command_in;
		if (!command_in.compare("push_front"))
		{
			int command_arg;
			cin >> command_arg;
			dq.push_front(command_arg);
		}
		if (!command_in.compare("push_back"))
		{
			int command_arg;
			cin >> command_arg;
			dq.push_back(command_arg);
		}
		if (!command_in.compare("pop_front"))
		{
			if (dq.empty())
			{
				cout << -1 << "\n";
			}
			else
			{
				cout << dq.front() << "\n";
				dq.pop_front();
			}
		}
		if (!command_in.compare("pop_back"))
		{
			if (dq.empty())
			{
				cout << -1 << "\n";
			}
			else
			{
				cout << dq.back() << "\n";
				dq.pop_back();
			}
		}
		if (!command_in.compare("size"))
		{
			cout << dq.size() << "\n";
		}
		if (!command_in.compare("empty"))
		{
			if (dq.empty())
			{
				cout << 1 << "\n";
			}
			else
			{
				cout << 0 << "\n";
			}
		}
		if (!command_in.compare("front"))
		{
			if (dq.empty())
			{
				cout << -1 << "\n";
			}
			else
			{
				cout << dq.front() << "\n";
			}
		}
		if (!command_in.compare("back"))
		{
			if (dq.empty())
			{
				cout << -1 << "\n";
			}
			else
			{
				cout << dq.back() << "\n";
			}
		}
	}
	return 0;
}