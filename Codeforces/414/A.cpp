#include <iostream>
using namespace std;
int main(){
	int a,b,c;
	cin>>a>>b>>c;
	int n;
	cin>>n;
	int d;
	int result=0;
	//if 
	for (int i = 0;i<n;++i)
	{
		cin>>d;
		if ((d<c) & (d>b)){
			result ++;		
		}	
	}
	cout<<result;
}
