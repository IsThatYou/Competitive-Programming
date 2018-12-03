//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=642&page=show_problem&problem=382
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<utility> //pair
#include<fstream> //ifstream
#include <bits/stdc++.h> 
#include <string>  //string
#include <sstream> //stringstream
using namespace std;
int A[13];
int n;
int main()
{
	ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
	string line;
	bool first = true;
	while (getline(cin,line))
	{
		stringstream stream(line);
		stream>>n;
		if (n==0) break;
		
		if (first==false)
			printf("\n");
		else first = false;
		
		int d;
		int counter =0;
		while(stream>>d)
		{
			A[counter] = d;
			counter++;
		}
		for (int i1 = 0;i1<n-5;++i1)
		{
			for (int i2 = i1+1;i2<n-4;++i2)
			{
				for (int i3 = i2+1;i3<n-3;++i3)
				{
					for(int i4 = i3+1;i4<n-2;++i4)
					{
						for (int i5 = i4+1;i5<n-1;++i5)
						{
							for (int i6 = i5+1;i6<n;++i6)
							{
								printf("%d %d %d %d %d %d\n",A[i1],A[i2],A[i3],A[i4],A[i5],A[i6]);
							}
						}
					}
				}
			}
		}


	}
}
