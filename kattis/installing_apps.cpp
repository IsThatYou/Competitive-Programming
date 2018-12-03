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
    for (int i =1;i<n;++n)
    {
        for (int j =1;j<i+2;++j)
        {
            
        }
    }
}
