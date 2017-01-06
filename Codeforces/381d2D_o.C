#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;
const int maxn = 2e5 + 10;
int a[maxn],id[maxn],mark[maxn],ans[maxn];
long long path[maxn];
vector<pair<int,long long> > g[maxn];
long long dfs(int root,int dep,long long dist)
{
    long long ret = 0;
    path[dep] = dist;   id[dep] = root;
    for(int i=0;i<g[root].size();i++)
        ret += dfs(g[root][i].first,dep+1,dist+g[root][i].second);
    int pos = lower_bound(path,path+dep,dist - a[root]) - path;
    mark[root]++,    mark[id[pos]]--;
    ans[root] = ret;
    return ret + mark[root];
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for(int i=2,p,w;i<=n;i++)
        scanf("%d %d",&p,&w),   g[p].push_back(make_pair(i,w));
    dfs(1,0,0);
    for(int i=1;i<=n;i++)
        printf("%d ",ans[i]);
}