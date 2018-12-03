#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	string a,b;
	cin>>a;
	cin>>b;
	vector<char> a1(a.begin(),a.end());
	vector<char> b1(b.begin(),b.end());
	sort(a1.begin(),a1.end());
	sort(b1.begin(),b1.end());
	int n = a1.size();
	vector<char> result(n);
	for (int i = 0; i<n;++i)
	{
		result[i] = 'a';		
	}
	//for (auto &x:result)
	//{
//		cout<<x<<endl;
	//}
	
}
