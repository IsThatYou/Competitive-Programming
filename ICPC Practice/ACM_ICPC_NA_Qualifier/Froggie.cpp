#include <iostream>
#include <vector>

using namespace std;

int main(){

	int l,w,px,py=-1;
	string s;

	cin >> l >> w;

	int arr[l][3];

	for(int i=0; i<l; i++){
		cin >> arr[i][0] >> arr[i][1] >> arr[i][2] ;

	}

	cin >> px >> s;

	for(int i=0; i<s.length(); i++){
		if(s[i]=='U'){
			py+=1
			if(py==l){
				cout << 'safe' << endl;
				return 0;
			}
			if(i*)
		}
	}


	return 0;
}
