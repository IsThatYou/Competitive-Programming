#include <bits/stdc++.h>
using namespace std;
//Lowst common ancester reduce to Range Minimum query, with a slight twist.
int st[4 * 100005];
vector<int> E;
vector<int> A;
int H[100005]={0};
unordered_map<int,vector<int>> graph;
void SegmentTreeConstruction(int L,int R,int i)
{
	if (L==R) 
		st[i] = L;
	else
	{
		int temp = (L+R)/2;
		SegmentTreeConstruction(L, temp, 2*i);
		SegmentTreeConstruction(temp+1,R,2*i+1);
		if (A[st[2*i]] <=A[st[2*i+1]])
			st[i] = st[2*i];
		else
			st[i] = st[2*i+1];
	}
}

int RMQ(int p, int L, int R, int i, int j)
{
	if (i>R||j<L) return -1;
	if (L>=i && R<=j)
		return st[p];
	int mid = (L+R)/2;
	int P1 = RMQ(2*p,L, mid,i,j);
	int P2 = RMQ(2*p,mid+1,R,i,j);
	if (P1==-1) return P2;
	if (P2==-1) return P1;
	if (A[P1]<=A[P2])
		return P1;
	else
		return P2;
}

int coun;
void dfs(int cur,int lv)
{
	E.push_back(cur);
	A.push_back(lv);
	if (H[cur] == 0)
		H[cur] = coun;
	coun++;
	for (int i = 0;i<graph[cur].size();++i)
	{
		dfs(graph[cur][i],lv+1);
		E.push_back(cur);
		A.push_back(lv);
	}
	
	
}

int main()
{
	int n,q;
	cin>>n>>q;
	int t;
	for (int i = 0;i<n-1;++i)
	{
		cin>>t;
		graph[t].push_back(i+2);
	}
	coun = 0;
	dfs(1,0);
	cout<<"E"<<endl;
	for (auto x: E)
	{
		cout<<x<<' ';
	}
	cout<<endl;
	cout<<"A"<<endl;
	for(auto x: A)
		cout<<x<<' ';
	cout<<endl;
	cout<<"H"<<endl;
	for (auto x: E)
		cout<<x<<' ';
	SegmentTreeConstruction(0,A.size(),1);
	for (int i = 0;i<q;++i)
	{
		int l,r;
		cin>>l>>r;
		int ans = RMQ(1,0,A.size(),l,r);
		cout<<ans<<endl;
	}
}





