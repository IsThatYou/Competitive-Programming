#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int graph[100005];
int main()
{
	int n;
	cin>>n;
	for (int i =0;i<n;++i)
		cin>>graph[i+1];
	vector<int> cclist;
	int visited[100005]={0};
	for (int i = 1;i<n+1;++i)
	{

		if (!visited[i])
		{
			int length = 0;
			vector<int> pool;
			pool.push_back(i);
			while (pool.size())
			{
				int cur = pool.back();
				//cout<<cur<<endl;
				//cout<<graph[cur]<<endl;
				pool.pop_back();
				visited[cur] =1;
				length++;
				if (!visited[graph[cur]])
					pool.push_back(graph[cur]);
			}
			cclist.push_back(length);
		}

	}
	//cout<<"rua?"<<graph[98]<<endl;
	// for (int i = 0;i<cclist.size();++i)
	// 	cout<<cclist[i]<<endl;
	if (cclist.size()==1)
	{
		ll ans = (ll)cclist[0] * (cclist[0]-1);
		cout<<ans+n;
	}
	else{
		sort(cclist.rbegin(),cclist.rend());
		ll temp =cclist[0] + cclist[1];
		//cout<<temp<<endl;
		ll ans = (ll) temp *(temp-1)+n;
		for (int i = 2; i<cclist.size();++i)
		{
			ans += (ll) cclist[i]*(cclist[i]-1);
		}
		cout<<ans;
	}
}