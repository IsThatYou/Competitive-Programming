#include <bits/stdc++.h>
using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
int main(){
	long long q,l,r;
	cin>>q>>l>>r;
	//printf("%lld\n", l);
	vector<int> lis;
	long long n = q;
	if (n<2){
		int count =0;
		if (n==1){
			count = 1;
		}
		else{
			count = 0;
		}
		printf("%d\n", count);
	}
	else{
	while (n>1){
		if (n%2){
			lis.push_back(1);
		}
		else{
			lis.push_back(0);
		}
		n = n/2;
	}
	reverse(lis.begin(), lis.end());
	
	//for (vector<int>::const_iterator i = lis.begin(); i != lis.end(); ++i){
    	//std::cout << *i << ' ';
	//}
	int llis = lis.size();
	int count = 0;
	long long constraint = pow(2, llis+1) -1;
	//printf("%lld\n", constraint);
	for (long long i = l;i<r+1;++i){

		if (i % 2 && i<=constraint){
			count += 1;
		}
		else{
			for (int j = 0; j<llis;j++){
				int another = (int) pow(2,j+1);
				if (i - another <0){
					
					break;
				}

				int another1 = (int) pow(2,j+2);
				if ((i-another)%(another1) == 0){

					count += lis[j];
				}
			}
		}
	}
	printf("%d\n", count);
}
};