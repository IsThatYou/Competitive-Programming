#include <bits/stdc++.h>
#define ll long long 
using namespace std;
ll arr[100005];
int main()
{
	int n;
	cin>>n;
	for (int i = 2;i < n+1;++i)
	{
		ll count = 0;
		for (int j = 2;j<floor(sqrt(i))+1; ++j)
		{
			if (i%j == 0)
			{
				int score = i/j;
				if (score !=1)
				{
					count+=4*score;
					if (j!=score)
					{
						count += 4 * j;
					}
				}
			}
		}
		arr[i] = arr[i-1]+count;
	}

	cout<<arr[n];
}