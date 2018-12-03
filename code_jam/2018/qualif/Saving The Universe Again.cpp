#include <iostream>
#include <string>
#include<vector>
using namespace std;


int check(string mystr)
{
	vector<char> temp(mystr.begin(), mystr.end());
	int add = 1;
	int damage = 0;
	for (auto x : temp)
	{
		if (x == 'C')
		{
			add *= 2;
		}
		else
		{
			damage += add;
		}
	}
	return damage;
}

int main()
{
	int T;
	cin >> T;
	int D;
	string mystr;
	for (int i = 0; i < T; i++)
	{
		cin>>D;
		cin >> mystr;

		int total = check(mystr);
		if (total <= D)
		{
			printf("Case #%d: %d\n", i + 1, 0);
		}
		else {
			int made = 0;
			while (total > D)
			{
				//move a S forward
				char last = 'C';
				int change = 0;

				for (int j = mystr.size() - 1; j >= 0; j--)
				{
					if (mystr[j] == 'S')
					{
						if (last == 'C') change++;
						last = 'S';
					}
					else
					{
						if (last == 'S')
						{
							change++;
							mystr.replace(j, 1, "S");
							mystr.replace(j + 1, 1, "C");
							made++;
							break;
						}
						last = 'C';
					}
				}
				total = check(mystr);
				if (change <= 1) break;
			}
			if (total > D) printf("Case #%d: IMPOSSIBLE\n", i + 1);
			else printf("Case #%d: %d\n", i + 1, made);
		}
	}

	
	return 0;
}
