#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    long int result = -1000000000;
    for (int i =0;i < n; ++i)
    {
        cin>>arr[i];
    }
    for (int i = 0; i< n; ++i)
    {
        long int sums = 0;
        for (int j = 0; j < n; ++j)
        {
            sums += (j+1) * arr[(i+j)%n];
        }
        if (sums > result) result = sums;
    }
    cout<<result;
    return 0;
}