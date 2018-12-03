#include <iostream>
#include <unordered_map>
#include <utility>
#include <queue>
using namespace std;
int main()
{
	int n,m,f,s,t;
	cin>>n>>m>>f>>s>>t;
	cout<<n<<m<<f<<s<<t;
	unordered_map<int,unordered_map<int,int> > graph;
	
	for (int a0 =0;a0<m;++a0)
	{
		int i,j,c;
		cin>>i>>j>>c;
		//if (graph.count(i)){
			graph[i][j] = c;
		graph[j][i] = c;
			//}
		//else
		//{
		//	graph[i] = unordered_map<int,int> sgraph;
		//}		
	}
	unordered_map<int, int> graphf;
	for (int a0 = 0;a0<f;++a0)
	{
		int u,v;
		cin>>u>>v;
		graphf[u] = v;		
	}
	if (f>0)
		int minn = 50001;
		
		for (auto const& a2:graphf)
		{
			int u = a2.first;
			int v = a2.second;
			unordered_map<int,unordered_map<int,int> > newgraph;
			
			newgraph = graph;
			//cout<<newgraph[1][3]<<endl;
			newgraph[u][v] = 0;
			newgraph[v][u] = 0;
			//cout<<newgraph[1][3]<<endl;
		}
		vector<int> t1(n,minn);
		pq = 
		 	

}
