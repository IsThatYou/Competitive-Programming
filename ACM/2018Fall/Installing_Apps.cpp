//https://open.kattis.com/problems/installingapps
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<utility> //pair
using namespace std;
int n,c,d,s;
int main(){
    scanf("%d%d",&n,&c);
    vector<pair<int,int>> lookup(n);
    vector<vector<pair<int,int>>> dp(n+1,vector<pair<int,int>>(n+1));
    int counter = 0;
    while (n--)
    {
        scanf("%d%d",&d,&s);
        lookup[counter] = make_pair(d,s);
        counter ++;
    }
    sort(lookup.begin(),lookup.end(),[](auto &left, auto &right){return (left.first-left.second)<(right.first-right.second);});
    
    // for (auto x : lookup)
    // {
    //     cout<<x.first<<x.second<<endl;
    // }
    for (int i =0;i< n;++i) dp[i][0] = make_pair(c,0);
    dp[0][0] = make_pair(c,0);
    d = lookup[0].first;
    s = lookup[0].second;
    if (max(d,s) <= c) dp[0][1] = make_pair(c-lookup[0].second,0);
    else dp[0][1] = make_pair(0,0);
    for (int i =1;i<n;++n)
    {
        d = lookup[i].first;
        s = lookup[i].second;
        int mx = max(d,s);
        for (int j =1;j<i+2;++j)
        {
            int rem = max(dp[i-1][j-1].first, dp[i][j-1].first);
            if (d-s)
        }
    }
}