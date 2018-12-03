#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
int greedy_helper(vector<int> coins, int m)
{
	int num = 0;
	for (auto const&coin:coins)
	{
		if (coin<=m)
		{
			num+=m/coin;
			m = m%coin;
		}

	}
	return num;
}

int main()
{
	int n;
	vector<int> coins;
	cin>>n;
	for (int i = 0; i<n;++i)
	{
		int temp;
		cin>>temp;
		coins.push_back(temp);
	}	
	vector<int> flipped_coins;

	flipped_coins = coins;
	reverse(flipped_coins.begin(),flipped_coins.end());
	vector<int> m;
	int range = coins.back() * 2;
	for (int i =0 ;i<range;++i)
	{
		m.push_back(0);
	}
	for (int i =1;i<range;++i)
	{
		set<int> possible_ways;
		for (auto const & coin:coins)
		{
			if (i-coin>=0) possible_ways.insert(m[i-coin]);
			else break;	
		}		
		m[i] =  *possible_ways.begin() + 1;
		if (m[i]!= greedy_helper(flipped_coins,i)){
		       	cout<<"non-canonical"<<endl;
			goto mlabel;
			;}
	}
	
	
	cout<<"canonical"<<endl;
	
mlabel:
	int i = 0;
}
