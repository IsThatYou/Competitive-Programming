#include <iostream>
#include <vector>
using namespace std;
vector<pair<int,int>> mem(3000+1,make_pair(-1,0));
int main()
{
	vector<int> arr(3000,-1);
	int n;
	bool c=true;
	cin >> n;
	for(int i=0; i<n; i++){
		for (int j =0;j<25;j++)
		{
			int t;
			scanf("%d",&t);

			if(arr[t-1]==-1 && c){
				arr[t-1] = i;
			}else if(c){
				cout << arr[t-1]+1 << " " << i+1 << endl;
				c=false;
			}

		}
	}

	if(c){
		cout << "no ties" << endl;
	}
	return 0;
}