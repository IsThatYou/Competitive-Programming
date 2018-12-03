#include <bits/stdc++.h>
using namespace std;
int main()
{
	string line;
	while (getline(cin,line))
	{
		int n = stoi(line);
		vector<string> ans;
		for (int i =n+1;i<2*n+1;++i)
		{
			double result = (double)(i * n)/(i-n);
			double result2 = (int) result;
			if ((result - result2) ==0.0)
			{
				int result3 = (int) result;
				string temp = "1/" +to_string(n) +" = 1/"+to_string(result3)+" + 1/"+to_string(i);
				ans.push_back(temp);
			}
		}
		cout<<ans.size()<<endl;
		for (auto x:ans)
			cout<<x<<endl;
	}
}