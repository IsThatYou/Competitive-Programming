#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
vector<int> dijkstra(int start,int n,unordered_map<int,vector<pair<int,int>>>& graph)
{
	priority_queue<pair<int,int>, vector<pair<int,int>>,greater<pair<int,int>>> pq;
	vector<int> dist(n+1,INF);
	vector<int> visited(n+1,0);
	dist[start] = 0;
	pq.push(make_pair(0,start));
	while (pq.size())
	{
		pair<int,int> temp = pq.top();
		int cur = temp.second;
		pq.pop();
		visited[cur]= 1;
		cout<<endl;
		cout<<cur<<endl;
		for (int i = 0;i<graph[cur].size();++i)
		{
			pair<int,int> neigh = graph[cur][i];
			if (!visited[neigh.first])
			{
				if ((dist[cur] + neigh.second)<dist[neigh.first])
				{
					cout<<neigh.first<<endl;
					cout<<dist[neigh.first]<<endl;
					dist[neigh.first] = dist[cur] + neigh.second;
					cout<<dist[neigh.first]<<endl;
					pq.push(make_pair(dist[neigh.first],neigh.first));
				}
				
			}
		}
	}
	return dist;
}

vector<string> split(const string& s, char delimiter)
{
   vector<string> tokens;
   string token;
   istringstream tokenStream(s);
   while (getline(tokenStream, token, delimiter))
   {
      tokens.push_back(token);
   }
   return tokens;
}
int main()
{
	int n = 0;
	
	string line;
	unordered_map<int,vector<pair<int,int>>> graph;
	char * delim;

	while (getline(cin,line))
	{
		if (!n)
			n = stoi(line);
		else{
			int a, b,c;
			char delim = ' ';
			vector<string> s1 = split(line, delim);

			a = stoi(s1[0]);
			b = stoi(s1[1]);
			c = stoi(s1[2]) ;
			//cout<<a<<' '<<b<<' '<<c<<endl;
			graph[a].push_back(make_pair(b,c));
			graph[b].push_back(make_pair(a,c));

		}

	}

	vector<int> dist = dijkstra(1,n,graph);
	printf("Vertex   Distance from Source\n"); 
	cout<<n<<endl;
    for (int i = 1; i < n+1; ++i) 
        printf("%d \t\t %d\n", i, dist[i]); 
}