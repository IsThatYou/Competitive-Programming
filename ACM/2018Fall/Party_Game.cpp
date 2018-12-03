#include <bits/stdc++.h>
using namespace std;
int check_pow_2(int x)
{
	if (x==0)
		return 0;
	return (x&(x-1))==0;	
}
int main()
{
	int n;
	cin>>n;
	//cout<<"sanity:"<<check_pow_2(4)<<endl;
	for (int i =0;i<n;++i)
	{
		int c;
		cin>>c;
		int visited[c+1] = {0};
		int graph[c+1];
		for (int j = 1;j<c+1;++j)
		{
			int t;
			cin>>t;
			graph[j] = t;
		}
		int good = 1;
		for (int j = 1;j<c+1;++j)
		{
			int start = j;
			if (!visited[start])
			{
				vector<int> pool;
				pool.push_back(start);
				int length = 0;
				//cout<<"start:"<<start<<endl;
				while (pool.size())
				{
					int cur = pool.back();
					pool.pop_back();
					int next = graph[cur];
					//cout<<next<<endl;
					visited[cur] = 1;
					length++;
					if (!visited[next])
					{
						pool.push_back(next);
					}
				}
				int is = check_pow_2(length);
				//cout<<is<<' '<<length<<endl;
				if (!is)
				{
					good = 0;
					break;
				}
			}
		}
		if (good)
			cout<<"All can eat."<<endl;
		else
			cout<<"Some starve."<<endl;
	}
}