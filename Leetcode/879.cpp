#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int profitableSchemes(int G, int P, vector<int>& group, vector<int>& profit) {
        unordered_map<pair<int,int>,int> smh;
        int M[G+1][P+1] = {0};
        for (int i = 0;i<group.size();++i)
        {
            pair<int,int> temp = make_pair(group[i],profit[i]);
            if (smh.find(temp) != end())
            {
                smh[temp]++;
            }
            else
                smh[temp] =1;
        }
        for (int i = 1;i<G+1;++i)
        {
            for (int j = 0;j<P+1;++j)
            {
                // search smh first;
                pair<int,int> temp = make_pair(i,j);
                if (smh.find(temp) != end())
                {
                    if (smh[temp] != 0){
                        M[i][j] ++;
                        smh[temp] --;
                    }
                }
                for (int z = 1;z<floor(i/2)+1;++z)
                {
                    int counter = i-z;
                    for (int c = 0;c<=j;++c)
                    {
                        int a = M[z][c];
                        int b = M[counter][j-c];
                        M[i][j] += a*b;
                    }
                }
                //then search previous combo using for loop
            }
        }
        int result = 0;
        for (int i = 1;i<G+1;i++)
        {
            for (int j = P;j<P+1;++j)
            {
                result += M[i][j];
            }
        }
        cout<<result<<endl;
        return result;
        
    }
};