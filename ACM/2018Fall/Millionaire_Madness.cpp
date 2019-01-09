//https://open.kattis.com/problems/millionairemadness
// binary search + dfs, not dp
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
int m,n;

int main()
{
	scanf("%d%d",&m,&n);
	int matrix[m][n]= {0};
	int matrix2[m][n] = {0};
	//printf("%d",matrix[1][1]);
	for (int i = 0;i<m;++i)
	{
		for (int j = 0;j<n;++j)
		{
			scanf("%d",&matrix[i][j]);
		}
	}
	matrix2[0][0] = 0;
	for (int i = 0;i<m;++i)
	{
		for (int j = 0;j<n;++j)
		{
			if (i == 0 && j ==0)
			{
				continue;
			}
			int top = 2147483646;
			int left = 2147483646;
			int ans = top;
			if (i-1>=0){
				top = matrix2[i-1][j];
				int diff =matrix[i][j] - matrix[i-1][j];
				if (top > diff)
				{
					
					if (ans >top) ans = top;
				}else
				{
					if (ans>diff) ans = diff;
				}

			}

			if (j-1>=0){
				left = matrix2[i][j-1];
				int diff2 = matrix[i][j] - matrix[i][j-1];
				int rua = max(left,diff2);
				if (rua<ans) ans = rua;
			}
			if (top == left && top == 2147483646)continue;
			matrix2[i][j] = ans;

		}
		for (int j = n-1;j>=0;--j)
		{
			if (i == 0 && j ==0)
			{
				continue;
			}
			int top = 2147483646;
			int right = 2147483646;
			int ans = top;
			if (i-1>=0){
				top = matrix2[i-1][j];
				int diff =matrix[i][j] - matrix[i-1][j];
				if (top > diff)
				{
					
					if (ans >top) ans = top;
				}else
				{
					if (ans>diff) ans = diff;
				}

			}
			if (j<n-1){
				right = matrix2[i][j+1];
				int diff2 = matrix[i][j] - matrix[i][j+1];
				int rua = max(right,diff2);
				if (rua<ans) ans = rua;
			}
			if (top == right && top == 2147483646)continue;
			if (ans < matrix2[i][j])
			matrix2[i][j] = ans;
		}
	}
	cout<<matrix2[m-1][n-1]<<endl;
	// for (auto r:matrix2)
	// {
	// 	for (int i = 0;i<n;++i)
	// 	{
	// 		cout<<r[i]<<' ';
	// 	}
	// 	cout<<endl;
	// }
}