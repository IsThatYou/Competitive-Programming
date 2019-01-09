//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1051

#include <bits/stdc++.h>
using namespace std;
int main()
{
    string line;
    while (getline(cin, line))
    {
        if (line == "0")
                break;
                
        /* long n = stol(line); */
        /* int result = 0; */
        /* for (int i = 1; i<= ceil(sqrt(n));i++) */
        /* { */
        /*     if (n%i==0) */
        /*         result ++; */
        /* } */
        //result += 1;
        //A better solution:
        //if the number is a perfect square, then it is a yes
        //else it is a no
        long n = stol(line);
        long sq = (long) sqrt(n);
        if (sq*sq == n)
            cout<<"yes"<<endl;
        else
            cout<<"no"<<endl;
    }

}




