#include <bits/stdc++.h>
using namespace std;
//https://open.kattis.com/problems/rainbowroads
int A[50001] ;
int dfs_help(unordered_map<int,vector<pair<int,int>>> &graph,int start,int get)
{
	set<int> visited;
	visited.insert(start);
	visited.insert(get);
	vector<int> pool;
	pool.push_back(start);
	A[start] = 1;
	while(pool.size())
	{
		int cur = pool.back();
		pool.pop_back();
		//cout<<cur<<endl;
		int length = graph[cur].size();
		for (int i = 0;i<length;++i)
		{
			pair<int,int> neigh = graph[cur][i];
			int t1 = neigh.first;
			int v1 = neigh.second;
			if (visited.find(t1) == visited.end())
			{
				pool.push_back(t1);
				A[t1] = 1;
				visited.insert(t1);
			}
		}
	}
}
int dfs(unordered_map<int,vector<pair<int,int>>> &graph, set<int> & visited,int start)
{
	visited.insert(start);
	vector<int> pool;
	pool.push_back(start);
	while (pool.size())
	{
		int cur = pool.back();
		pool.pop_back();
		//cout<<"cur:"<<cur<<endl;
		int length = graph[cur].size();
		int quick[length] = {0};
		set<int> test;
		set<int> test2;
		for (int i = 0;i<length;++i)
		{
			pair<int,int> neigh = graph[cur][i];
			int t1 = neigh.first;
			int v1 = neigh.second;
			if (test.find(v1)==test.end())
			{
				test.insert(v1);
			}
			else {
				quick[i] = 1;
				test2.insert(v1);
			}
		}
		// cout<<"start"<<endl;
		// for (int i = 0; i<length;++i)
		// {
		// 	cout<<graph[cur][i].first<<endl;
		// }
		// cout<<"end"<<endl;
		for (int i = 0;i<length;++i)
		{
			pair<int,int> neigh = graph[cur][i];
			int t1 = neigh.first;
			int v1 = neigh.second;
			if (test2.find(v1) !=test2.end())
			{
				//mark all not good
				//cout<<"t1:"<<t1<<endl;
				if (A[t1]==1)
				{
					//mark all not good
					return 0;
				}
				dfs_help(graph,t1,cur);
			}

			if (visited.find(t1) == visited.end())
			{
				visited.insert(t1);
				pool.push_back(t1);
			}

			
		}
	}
	return 1;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int n;
	cin>>n;
	// while (scanf("%d" , &n)!=EOF)
	// {
		//cout<<"n"<<n<<endl;
		unordered_map<int,vector<pair<int,int>>> graph;
		memset(A,0,sizeof(A[0])*50001);
		//cout<<"A"<<A[1]<<endl;
		for (int i = 0;i<n-1;++i)
		{
			int a,b,c;
			cin>>a>>b>>c;
			//cout<<a<<b<<c;
			graph[a].push_back(make_pair(b,c));
			graph[b].push_back(make_pair(a,c));
		}
		//cout<<graph[3][1].first<<endl;
		int start = 1;
		set<int> visited;

		int result = dfs(graph,visited,start);
		//cout<<result<<endl;
		if (!result)
		{
			printf("%d",result);
		} 
		else{
			int sums = 0;
			for (int j =1;j<=n;++j)
				if (!A[j])
					sums++;
			cout<<sums;
			for (int j =1;j<=n;++j)
				if (!A[j])
					cout<<endl<<j;
		}

	// }

	
}