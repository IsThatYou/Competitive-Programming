#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <set>
#include <tuple>
#include <utility>
#include <vector>
#include <limits>
using namespace std;
#define tp tuple<int,int,int>
#define INT_MAX 21474
int M[2501][2501] = {0};
bool fncmp(tuple<int,int,int> a, tuple<int,int,int> b)
{
	return get<2>(a) > get<2>(b);
}
int minKey(int key[], bool mstSet[], int n) 
{ 
// Initialize min value 
	int min = INT_MAX, min_index; 
	  
	for (int v = 0; v < n; v++) 
	    if (mstSet[v] == false && key[v] < min) 
	        min = key[v], min_index = v; 
	  
	return min_index; 
} 
int main()
{
	int n;
	cin>>n;
	for (int i =0 ;i<n;i++)
	{
		for (int j = 0;j<n;++j)
		{
			scanf("%d",&M[i][j]);
		}
	}
	int parent[n] = {0};
	bool mstSet[n] ={false};
	int key[n];
	for (int i =0;i<n;++i)
	{
		key[i] = INT_MAX;
	}
	key[0] = 0;
	parent[0] = -1;
	for (int i = 0;i<n;++i)
	{
		int u = minKey(key,mstSet,n);
		mstSet[u] = true;
		for (int j = 0;j<n;++j)
			if (M[u][j] <key[j] && mstSet[j]==false) //M[u][j] exist if the graph not complete
				parent[j]=u, key[j] = M[u][j];
	}

	for (int i = 1;i<n;++i)
	{
		cout<<i+1<<' '<<parent[i]+1<<endl;
	}
	return 0;
}