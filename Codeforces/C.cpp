#include <bits/stdc++.h>
using namespace std;
int m = (int)1e9+7;
int mult(int a, int b) {
	return (long long) a * b % m;
}
void add(int& a, int b) {
	a += b;
	if (a >= m) {
		a -= m;
	}
}
int mpow(int a, int b) {
	int ret = 1;
	while (b) {
		if (b & 1) {
			ret = mult(ret, a);
		}
		a = mult(a, a);
		b >>= 1;
	}
	return ret;
}
int main(){
	int n,q;
	cin>>n>>q;
	string s;
	cin >>s;
	vector<int> arr;
	vector<int> ones ={0};
	for (int i = 0;i<n;++i)
	{
		arr.push_back(s[i] - '0');
		ones.push_back(ones.back() + arr.back());
	}
	for (int i = 0;i<q;++i)
	{
		int l,r;
		cin>>l>>r;
	
		int length = r-l+1;
		int sums = ones[r] - ones[l-1];

		int a = mpow(2,sums);
		//cout<<sums<<' '<<a<<endl;
		int ans = 0;
		ans = (ans+a-1)%m;
		int mul = a-1;
		int b = mpow(2,length-sums);
		//cout<<b<<endl;
		int c = 0;
		if (b<=1)
	        c = 0;
	    else{
	        c = (mult((b-1) , mul))%m;
	    }
	    add(ans,c);
	    ans = ans%m;
	    cout<<ans<<endl;
}

}