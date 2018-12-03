#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int p;
	cin>>p;
	for (int i =0;i<p;++i)
	{
	int k,n;
	cin>>k>>n;
	//cout<<n/10<<endl;
	vector<int> a;
	for (int i =0;i<n;++i)
	{
		int b;
		cin>>b;
		a.push_back(b);			
	}
	vector<int>c;
	c = a;
	sort(c.begin(),c.end());
	int counter = 0;
	for (int j =0;j<n;++j)
	{
		if (a[j] == c[counter])counter+=1;
	}
	//for (auto &x:a)cout<<x;
	cout<<k<<" "<<n-counter<<endl;
	}	
	return 0;
}
