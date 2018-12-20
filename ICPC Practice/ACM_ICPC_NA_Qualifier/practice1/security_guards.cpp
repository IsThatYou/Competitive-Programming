//http://codeforces.com/gym/101954/problem/B
#include <iostream>
#include <cstdlib>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstring>
#include <queue>
#include <tuple>
using namespace std;
int M[5001][5001] ={0};

void dfs(int x1,int y1)
{
	vector<pair<int,int>> pool;
	pool.push_back(make_pair(x1,y1));
	pair<int,int> v;
	vector<vector<bool>> visited(5001, vector<bool>(5001,0));
	int x,y;
	int mmax = max(x1,y1);

	while (!pool.empty())
	{
		//cout<<pool.size()<<endl;
		v = pool.back();
		pool.pop_back();
		x = v.first;
		y = v.second;
		//cout<<x<<' '<<y<<endl;
		if (!visited[x][y])
		{
			visited[x][y] = 1;
			mmax = max(abs(x1-x),abs(y1-y));
			if (M[x][y]==-1)
			{
				M[x][y]= mmax;
			}
			else{
				M[x][y] = min(M[x][y],mmax);
			}
			for (int i =-1;i<2;++i)
			{
				for (int j = -1;j<2;++j)
				{
					if (i==j && i==0) continue;
					if ((x+i)>=0 && (x+i)<=5000 && (y+j)>=0&& (y+j)<=5000)
					{
						if (!visited[x+i][y+j]) pool.push_back(make_pair(x+i,y+j));
					}
				}
			}
		}

	}
}
void bfs( queue<tuple<int,int,int>> pool)
{
	//queue<pair<int,int>> pool;
	//pool.push(make_pair(x1,y1));
	//vector<vector<bool>> visited(5001, vector<bool>(5001,0));
	//visited[x1][y1] = 1;
	int x,y,dist;
	while (!pool.empty())
	{
		tuple<int,int,int> v = pool.front();
		pool.pop();
		x = get<0>(v);
		y = get<1>(v);
		dist = get<2>(v);
		for (int i =-1;i<2;++i)
		{
			for (int j = -1;j<2;++j)
			{
				if (i==j && i==0) continue;
				if ((x+i)>=0 && (x+i)<=5000 && (y+j)>=0&& (y+j)<=5000)
				{
					if (M[x+i][y+j]==-1)
					{
						pool.push(make_tuple(x+i,y+j,dist+1));
						M[x+i][y+j] = dist+1;
					}
				}
			}
		}
	}

}
int main()
{
	int N,Q;
	scanf("%d%d",&N,&Q);
	memset(M,-1,5001*5001*sizeof(M[0][0]));
	
	int x,y;
	queue<tuple<int,int,int>> pool;
	for (int i = 0;i<N;++i)
	{
		scanf("%d%d", &x,&y);
		M[x][y] = 0;
		pool.push(make_tuple(x,y,0));
	}
	bfs(pool);

	for (int i = 0;i<Q;++i)
	{
		scanf("%d%d",&x,&y);
		cout<<M[x][y]<<endl;
	}
	return 0 ;
}