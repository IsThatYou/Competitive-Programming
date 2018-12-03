//https://open.kattis.com/problems/permutationdescent
// 2d dp

#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
 
using namespace std;
const int mod =1001113;
int dp[1007][1007] = {};
int f,k,n,v;
void calc(){
    dp[2][0] = 1;
    dp[2][1] = 1;
    for (int i =3;i<1007;++i)
    {
        for (int j = 0;j<i;++j)
        {
            if (j==0) dp[i][j] = 1;
            else dp[i][j] = ((i-j)*dp[i-1][j-1] + (j+1)*dp[i-1][j])%mod;
        }
    }
}




int main(){
    calc();
scanf("%d",&f);
while (f--)
{
    scanf("%d%d%d",&k,&n,&v);
    printf("%d %d\n",k,dp[n][v]);

}
return 0;
}