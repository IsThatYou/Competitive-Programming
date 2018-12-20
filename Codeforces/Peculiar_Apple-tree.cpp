#include <bits/stdc++.h>
using namespace std;
unordered_map<int,vector<int>> tree;
// vector<int> dfs(int cur,int last)
// {
// 	int length = tree[cur].size();
// 	if (length == 1)
// 	{
// 		vector<int> cmp;
// 		cmp.push_back(1);
// 		return cmp;
// 	}
// 	vector<vector<int>> histo;
// 	for (int i = 0;i < length;++i)
// 	{
// 		if (tree[cur][i] != last)
// 		{
// 			vector<int> temp = dfs(tree[cur][i], cur);
// 			histo.push_back(temp);
// 		}
// 	}
// 	int maxx = 0;
// 	for (int i = 0;i<histo.size();++i)
// 	{
// 		if (maxx< histo[i].size())
// 			maxx = histo[i].size()
// 	}
// 	vector<int> new_vol;
// 	for (int i = 0;i<maxx;++i)
// 	{
// 		int value = 0;
// 		for (int j = 0;j <histo.size();++j)
// 		{
// 			int tempsize=histo[j].size();
// 			if (histo[j].size() >i)
// 			{
// 				if (histo[j][tempsize-i-1]==1)
// 				{
// 					value++;
// 				}	
// 			}
// 		}
// 	}
// }
int main()
{
	int n;
	cin>>n;
	for (int i = 2;i<n+1;++i)
	{
		int in;
		cin>>in;
		//tree[i].push_back(in);
		tree[in].push_back(i);
	}
	queue<pair<int,int>> pool;
	pool.push(make_pair(1,1));
	//visited
	int ans[100005]={0};
	while (pool.size())
	{
		pair<int,int> cur = pool.front();
		int val = cur.first;
		//cout<<val<<endl;
		int ind = cur.second;
		pool.pop();
		for (int i =0; i< tree[val].size();++i)
		{
			pool.push(make_pair(tree[val][i],ind+1));
			ans[ind]++;
		}	
	}
	int i = 1;
	int result = 1;
	while (ans[i])
	{
		if (ans[i] % 2!=0)
		{
			result++;
		}
		i++;
	}
	cout<<result;
}