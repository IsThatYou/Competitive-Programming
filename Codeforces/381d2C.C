#include <iostream>
#include <cstring>
using namespace std;
int main() {
	int n, m;
	cin>>n>>m;
	int min_mex = 1000000;
	for (int i=0; i<m; i++) {
		int l, r;
		cin>>l>>r;
		min_mex = min (min_mex, r - l + 1);
	}
	cout<<min_mex<<endl;
	for (int i=0; i<n; i++) {
		cout<< (i%min_mex)<<" ";
	}
	cout<<endl;
	return 0;
}