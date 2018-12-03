//https://codeforces.com/problemset/problem/796/D
#include <bits/stdc++.h>
using namespace std;
unordered_map<int,vector<pair<int,int>>> graph;
int visited[300005];
int edge_visited[300005];
vector<int> police_arr;
unordered_set<int> polices;
int main(){
	int n,k,d;
	cin>>n>>k>>d;
	for (int i =0;i<k;++i)
	{
		int p;
		cin>>p;
		police_arr.push_back(p);
		polices.insert(p);
	}
	for (int i = 0;i<n-1;++i)
	{
		int f,t;
		cin>>f>>t;
		graph[f].push_back(make_pair(t,i+1));
		graph[t].push_back(make_pair(f,i+1));
	}
	int ans = 0;
	vector<int> result;
	queue<pair<int,int>> pool;
	for (int i = 0;i<k;++i)
	{
		int temp = police_arr[i];
		pool.push(make_pair(temp,0));
		visited[temp] = 1;
		//cout<<"police#: "<<temp<<endl;
	}
	while (pool.size())
	{
		pair<int,int> cur_pair = pool.front();
		int cur = cur_pair.first;
		//cout<<cur<<endl;
		int val = cur_pair.second;
		pool.pop();

		for (int j = 0;j < graph[cur].size();++j)
		{
			int node = graph[cur][j].first;
			int edge_ind = graph[cur][j].second;
			if (!visited[node] && !edge_visited[edge_ind])
			{
				if (polices.find(node) == polices.end() && val+1 <= d)
				{
					pool.push(make_pair(node,val+1));
					visited[node] = 1;
					edge_visited[edge_ind] = 1;
				}
				else
				{
					//if it it is a police station or if exceed the range
					ans+=1;
					result.push_back(edge_ind);
					edge_visited[edge_ind] = 1;
				}
			}
			if (visited[node] && !edge_visited[edge_ind])
			{
				ans+=1;
				result.push_back(edge_ind);
				edge_visited[edge_ind] = 1;
			}
		}
	}
	
	cout<<ans<<endl;
	if (ans)
	{
		sort(result.begin(),result.end());
		cout<<result[0];
		for (int j = 1;j<ans;++j)
		{
			cout<<' '<<result[j];
		}
	}

}