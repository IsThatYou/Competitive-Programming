#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
bool cmp(pair<int,int>a,pair<int,int>b)
{
	return a.second<b.second;
}
int main()
{
	int n;
	scanf("%d",&n);
	vector<pair<int,int>> A;
	for (int i  = 0;i<n;++i)
	{
		int m;
		scanf("%d",&m);
		A.push_back(make_pair(i,m));

	}
	sort(A.begin(),A.end(),cmp);
	int sum=0;
	for (int i=0;i<n-1;i++)
	{
		sum += A[i].second;
	}
	int last = A[n-1].second;
	if (last>sum)
	{
		printf("impossible");
	}
	else{
		for (int j = n-1;j>=0;j--)
		{
			printf("%d ", A[j].first+1);
		}
	}

}