#include <iostream>
#include <string>
#include <iterator>
#include <utility>
#include <sstream>
#include <vector>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for (int i =0;i<t; ++i)
	{
		int n;
		cin>>n;
		cin.ignore();
		string line;
		getline(cin, line);
		istringstream this_line(line);
		istream_iterator<int> b(this_line),e;
		vector<int> coals(b, e);

		//vector<int> coals(istream_iterator<int>(this_line),(istream_iterator<int>()));
		string line2;
		getline(cin, line2);
		istringstream this_line2(line2);
		istream_iterator<int> b2(this_line2),e2;
		vector<int> tax(b2,e2);
		//for (vector<int>::iterator j = tax.begin();j != tax.end(); ++j)
		//{
		//	cout<<*j;
		//}
		getline(cin, line);
		istringstream this_line3(line);
		istream_iterator<int> b3(this_line3),e3;
		vector<int> policy(b3,e3);

		


	}
	return 0;
}
