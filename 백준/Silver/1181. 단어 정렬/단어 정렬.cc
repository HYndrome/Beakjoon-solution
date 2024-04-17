#include <iostream>
#include <string.h>
#include <algorithm>
#include <unordered_set>
#include <queue>
using namespace std;

int N;
unordered_set<string> words;

void Input()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		string word;
		cin >> word;
		words.insert(word);
	}
}

bool CmpWords(string left, string right)
{
	if (left.size() < right.size()) return true;
	if (left.size() > right.size()) return false;
	if (left < right) return true;
	if (left > right) return false;
	return false;
}

vector<string> SortWords()
{
	vector<string> vwords(words.begin(), words.end());
	sort(vwords.begin(), vwords.end(), CmpWords);
	return vwords;
}

int main()
{
	Input();
	vector<string> sortedWords = SortWords();
	for (string word : sortedWords)
	{
		cout << word << "\n";
	}
	return 0;
}