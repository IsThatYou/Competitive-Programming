#include <bits/stdc++.h>
using namespace std;
//Lowst common ancester reduce to Range Minimum query, with a slight twist.

vector<int> E;
vector<int> A;
vector<int> H(100005,0);
unordered_map<int,vector<int>> graph;
void SegmentTreeConstruction(int L,int R,int i,int* st, vector<int> & A)
{
	if (L==R) 
		st[i] = L;
	else
	{
		int mid = (L+R)/2;
		SegmentTreeConstruction(L, mid, 2*i,st,A);
		SegmentTreeConstruction(mid+1,R,2*i+1,st,A);
		// for a single element
		if (A[st[2*i]] <=A[st[2*i+1]])
			st[i] = st[2*i];
		else
			st[i] = st[2*i+1];
	}
}

int RMQ(int p, int L, int R, int i, int j, int* st,vector<int> & A)
{
	if (i>R||j<L) return -1;
	if (L>=i && R<=j)
		return st[p];
	int mid = (L+R)/2;
	int P1 = RMQ(2*p,L, mid,i,j,st,A);
	int P2 = RMQ(2*p+1,mid+1,R,i,j,st,A);
	//change this
	if (P1==-1) return P2;
	if (P2==-1) return P1;
	if (A[P1]<=A[P2])
		return P1;
	else
		return P2;
}
void SegmentTreeConstruction1(int L,int R,int i,pair<int,int>* st, vector<int> & A)
{
	if (L==R) 
		st[i] = make_pair(A[L],200005);
	else
	{
		int mid = (L+R)/2;
		SegmentTreeConstruction1(L, mid, 2*i,st,A);
		SegmentTreeConstruction1(mid+1,R,2*i+1,st,A);
		pair<int,int> a = st[2*i];
		pair<int,int> b = st[2*i+1];
		//vector<int> cmp;

		int temp = min(a.first,a.second);
		int temp2 = min(b.first,b.second);
		if (temp <= temp2)
		{
			if (max(a.first,a.second)<=temp2)
				st[i] = make_pair(a.first,a.second);
			else
				st[i] = make_pair(temp,temp2);
		}
		else{
			if (max(b.first,b.second)<=temp)
				st[i] = make_pair(b.first,b.second);
			else
				st[i] = make_pair(temp,temp2);
		}
		// for a single element
		// if (A[st[2*i]] <=A[st[2*i+1]])
		// 	st[i] = st[2*i];
		// else
		// 	st[i] = st[2*i+1];
	}
}

pair<int,int> RMQ1(int p, int L, int R, int i, int j, pair<int,int>* st,vector<int> & A)
{
	if (i>R||j<L) return make_pair(-1,-1);
	if (L>=i && R<=j)
		return st[p];
	int mid = (L+R)/2;
	pair<int,int> P1 = RMQ1(2*p,L, mid,i,j,st,A);
	pair<int,int> P2 = RMQ1(2*p+1,mid+1,R,i,j,st,A);
	//change this
	if (P1.first==-1) return P2;
	if (P2.first==-1) return P1;

	pair<int,int> a = P1;
	pair<int,int> b = P2;
	int temp = min(a.first,a.second);
	int temp2 = min(b.first,b.second);
	if (temp <= temp2)
	{
		if (max(a.first,a.second)<=temp2)
			return make_pair(a.first,a.second);
		else
			return make_pair(temp,temp2);
	}
	else{
		if (max(b.first,b.second)<=temp)
			return make_pair(b.first,b.second);
		else
			return make_pair(temp,temp2);
	}
	// if (A[P1]<=A[P2])
	// 	return P1;
	// else
	// 	return P2;
}
// SegmentTree and RMQ that returns not the min
// but max
void SegmentTreeConstruction2(int L,int R,int i,pair<int,int>* st, vector<int> & A)
{
	if (L==R) 
		st[i] = make_pair(A[L],-1);
	else
	{
		int mid = (L+R)/2;
		SegmentTreeConstruction2(L, mid, 2*i,st,A);
		SegmentTreeConstruction2(mid+1,R,2*i+1,st,A);
		pair<int,int> a = st[2*i];
		pair<int,int> b = st[2*i+1];
		int temp = max(a.first,a.second);
		int temp2 = max(b.first,b.second);
		if (temp <= temp2)
		{
			if (min(b.first,b.second)>=temp)
				st[i] = make_pair(b.first,b.second);
			else
				st[i] = make_pair(temp,temp2);
		}
		else{
			if (min(a.first,a.second)>=temp2)
				st[i] = make_pair(a.first,a.second);
			else
				st[i] = make_pair(temp,temp2);
		}
		// if (A[st[2*i]] >= A[st[2*i+1]])
		// 	st[i] = st[2*i];
		// else
		// 	st[i] = st[2*i+1];
	}
}
pair<int,int> RMQ2(int p, int L, int R, int i, int j, pair<int,int>* st,vector<int> & A)
{
	if (i>R||j<L) return make_pair(-1,-1);
	if (L>=i && R<=j)
		return st[p];
	int mid = (L+R)/2;
	pair<int,int> P1 = RMQ2(2*p,L, mid,i,j,st,A);
	pair<int,int> P2 = RMQ2(2*p+1,mid+1,R,i,j,st,A);
	if (P1.first==-1) return P2;
	if (P2.first==-1) return P1;
	pair<int,int> a = P1;
	pair<int,int> b = P2;
	int temp = max(a.first,a.second);
	int temp2 = max(b.first,b.second);
	if (temp <= temp2)
	{
		if (min(b.first,b.second)>=temp)
			return make_pair(b.first,b.second);
		else
			return make_pair(temp,temp2);
	}
	else{
		if (min(a.first,a.second)>=temp2)
			return make_pair(a.first,a.second);
		else
			return make_pair(temp,temp2);
	}
	// if (A[P1]>=A[P2])
	// 	return P1;
	// else
	// 	return P2;
}

int coun=0;
set<int> visited;
void dfs(int cur,int lv, int n)
{
	E.push_back(cur);
	A.push_back(lv);
	if (H[cur] == 0)
		H[cur] = coun;
	coun++;
	visited.insert(cur);
	for (int i = 0;i<graph[cur].size();++i)
	{
		dfs(graph[cur][i],lv+1,n);
		if (visited.size() <n)
		{
			E.push_back(cur);
			A.push_back(lv);
			coun++;
		}
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
	dfs(1,0,n);
	// cout<<"E"<<endl;
	// for (auto x: E)
	// {
	// 	cout<<x<<' ';
	// }
	// cout<<endl;
	// cout<<"A"<<endl;
	// for(auto x: A)
	// 	cout<<x<<' ';
	// cout<<endl;
	// cout<<"H"<<endl;
	// for (int x=0;x<n+1; ++x)
	// 	cout<<H[x]<<' ';
	int st[10*100005];
	SegmentTreeConstruction(0,A.size(),1, st,A);
	// realized I need another segment tree to find the max/min inTime.
	//min tree
	pair<int,int> st2[10*100005];
	SegmentTreeConstruction1(0,E.size(),1,st2,H);
	//max tree
	pair<int,int> st3[10*100005];
	SegmentTreeConstruction2(0,E.size(),1,st3,H);
	for (int i = 0;i<q;++i)
	{
		int l,r;
		cin>>l>>r;
		//cout<<"Hvals: "<<H[l]<<' '<<H[r]<<endl;
		// min in time
		pair<int,int> h1 = RMQ1(1,0,E.size(),l,r,st2,H);
		//cout<<"h1:"<<h1.first<<","<<h1.second<<endl;
		// max in time
		pair<int,int> h2 = RMQ2(1,0,E.size(),l,r,st3,H);
		//cout<<"h2:"<<h2.first<<","<<h2.second<<endl;

		int ans1;
		int h1a = max(h1.first,h1.second);
		int h1i = min(h1.first,h1.second);
		int h2a = max(h2.first, h2.second);
		int h2i = min(h2.first,h2.second);
		if (h1a != 200005)
		{
			ans1 = RMQ(1,0,A.size(),h1a,h2a,st,A);
		}
		else
		{
			ans1 = RMQ(1,0,A.size(),h1i,h2a,st,A);
		}
		int ans2;
		if (h2i != -1)
		{
			ans2 = RMQ(1,0,A.size(),h1i,h2i,st,A);
		}
		else
		{
			ans2 = RMQ(1,0,A.size(),h1i,h2a,st,A);
		}

		//cout<<ans<<endl;
		//cout<<"sol1:"<<E[ans1]<<", sol2:"<<E[ans2]<<endl;
		//cout<<"lvl1:"<<A[ans1]<<", lvl2:"<<A[ans2]<<endl;
		if (A[ans1] >=A[ans2])
		{
			cout<<E[h1i]<<' '<<A[ans1]<<endl;
		}
		else
			cout<<E[h2a]<<' '<<A[ans2]<<endl;

	}
}





