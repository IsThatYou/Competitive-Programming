#include <iostream>
#include <cstdlib>
#include <unordered_set>
using namespace std;
#define IN(n) int n;scanf("%d",&n);
#define FOR(i, m, n) for (int i(m); i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)
#define FT(m, n) FOR(k, m, n)
int dp[2001] = {0};
int main()
{
	int n;
	scanf("%d",&n);
	int m[n] ;
	for (int i = 0;i<n;++i)
	{
		scanf("%d", &m[i]);
	}
	dp[0] =0;
	dp[1] = 0;
	for (int i = 2;i<2001;++i)
	{
		unordered_set<int> s;
		for (int j = i-1;j>0;--j)
		{
			int p = i/j;
			int q = i-(p * j);
			int ans = 0;
			for (int z = 0;z<p;z++)
			{
				ans = dp[j]^ans;
			}
			ans = ans^dp[q];
			s.insert(ans);
		}
		int Mex = 0;
		while (s.find(Mex)!=s.end())
			Mex++;
		dp[i] = Mex;
	}
	int sol = 0;
	for (int i = 0;i<n;++i)
	{
		//cout<<dp[m[i]]<<endl;
		sol = sol ^ dp[m[i]];
	}
	if (sol ==0)
	{
		cout<<"Second"<<endl;
	}
	else cout<<"First"<<endl;
}