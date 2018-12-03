#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main(){
	int n;
	scanf("%d",&n);
	char A[n];
	scanf("%s",&A);
	A[n-1] = 'R';
	vector<int> B;
	int last_R = -1;
	for (int i =0;i<n;++i)
	{
		if (A[i]=='R')
		{
			int count = i+1;
			B.push_back(count);

			for (int j = i-1;j>last_R;--j)
			{
				B.push_back(--count);
			}
			last_R = i;
		}
	}
	for (auto x: B)
	{
		cout<<x<<endl;
	}
}