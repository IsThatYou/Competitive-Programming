#include <vector>
#include <iostream>
using namespace std;
int main()
{
	vector<int> A;
	A.push_back(1);
	A[11]=12;
	cout<<A[11];

}