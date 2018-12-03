#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
	double n,h;
	cin>>n>>h;
	double cur_base = 1;
	double new_base;
	double cur_height;
	double total =0.5 * h; 
	double each = total/n;
	double sum_height = 0;
	for (int i =1;i<n;++i)
	{
		double height= sqrt(i/n);
		cout<<setprecision(8)<<height*h<<" ";
	}
}
