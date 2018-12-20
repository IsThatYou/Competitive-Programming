#include <cstdio>
using namespace std;
int n,t;
double calc(int A[], int B[], double c)
{
	double sums = 0.;
	for (int i =0;i<n;++i)
	{
		double a = A[i];
		double b = B[i];
		if ((b+c)<=0) return -1;
		double rua= a/(b+c);

		sums+=a/(b+c);
	}
	return sums;
}
int main()
{
	scanf("%d%d",&n,&t);
	int h[n]={-1};
	int r[n]={-1};
	int a,b;
	for (int i = 0;i< n;++i)
	{
		scanf("%d%d",&h[i],&r[i]);
	}
	// for (auto x: h)
	// {
	// 	printf("%d",x);
	// }
	double start = -1e9;
	double end = 1e9;
	double mid = start;
	for (int i = 0;i<1000;++i)
	{
		mid = (start+end)/2;
		//printf("%f\n", mid);
		double ans = calc(h,r,mid);
		//printf("%f\n",ans);
		if (ans == t) break;
		else if (ans<0)
		{
			start = mid;
		}
		else if (ans < t)
			end = mid;
		else
			start = mid;
	}
	printf("%6.8f", mid);


}