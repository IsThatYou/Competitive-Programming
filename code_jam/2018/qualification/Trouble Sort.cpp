#include <iostream>
#include <string>
#include<vector>
#include <algorithm>
using namespace std;

int main() 
{
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N;
		cin >> N;
		int next;
		int counter1 = 0;
		int counter2 = 0;
		vector<int> even;
		vector<int> odd;
		for (int j = 0; j < N; j++)
		{
			if (j % 2 == 0)
			{
				cin >> next;
				even.push_back(next);
				
			}
			else
			{
				cin >> next;
				odd.push_back(next);
				
			}
		}
		sort(even.begin(), even.end());
		sort(odd.begin(), odd.end());
		
		int first = even[0];
		int second = even[1];
		int notok = 0;
		int index = 1;
		vector<int> rua;
		int s = odd.size();
		for (int j = 0; j < s; j++)
		{
			rua.push_back(even[j]);
			rua.push_back(odd[j]);
		}
		if (N%2!=0)rua.push_back(even[even.size()-1]);

		for (int j = 0; j < N-1; j++)
		{
			if (rua[j] > rua[j + 1])
			{
				notok = 1;
				index = j;
				break;
			}
		}
		if (notok)
		{
			printf("Case #%d: %d\n", i + 1, index);
		}
		else {
			printf("Case #%d: OK\n", i + 1);
		}
	}
	
	return 0;

}

