#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
vector<int> dijkstra(int start,int n,unordered_map<int,vector<pair<int,int>>>& graph)
{
	priority_queue<pair<int,int>, vector<pair<int,int>>,greater<pair<int,int>>> pq;
	vector<int> dist(n+1,INF);
	vector<int> visited(n+1,0);

	pq.push(make_pair(0,start));
	while (pq.size())
	{
		pair<int,int> temp = pq.top();
		int cur = temp.second;
		pq.pop();
		visited[cur]= 1;
		for (int i = 0;i<graph[cur].size();++i)
		{
			pair<int,int> neigh = graph[cur][i];

			if (!visited[neigh.first])
			{
				if ((dist[cur] + neigh.second)<dist[neigh.first])
				{
					dist[neigh.first] = dist[cur] + neigh.second;
					pq.push(make_pair(dist[neigh.first],neigh.first));
				}
				
			}
		}
	}
}
int main()
{
	int n;
	cin>>n;
	string line;
	unordered_map<int,vector<pair<int,int>>> graph;
	while (getline(cin,line))
	{
		string a, b,c;
		a = line.substr(0,1);
		b = line.substr(2,3);
		c = line.substr(4,5);
		cout<<a<<' '<<b<<' '<<c<<endl;
	}

	vector<int> dist = dijkstra(1,n,graph);
	printf("Vertex   Distance from Source\n"); 
    for (int i = 1; i < n+1; ++i) 
        printf("%d \t\t %d\n", i, dist[i]); 
}