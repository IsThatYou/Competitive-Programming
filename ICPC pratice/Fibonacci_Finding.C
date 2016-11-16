#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long* fastpow(unsigned long x1,unsigned long y1,unsigned long x2,unsigned long y2,int n, int m){


    long* result = new long[4];
    unsigned long sx1 = x1;
    unsigned long sy1 = y1;
    unsigned long sx2 = x2;
    unsigned long sy2 = y2;
    x1 = 1;
    y1 = 0;
    x2 = 0;
    y2 = 1;
    while (n > 0){
        if (n % 2){
            unsigned long t_x1 = (sx1 * x1 + sx2 * y1)%m;
            unsigned long t_y1 = (sy1 * x1 + sy2 * y1)%m;
            unsigned long t_x2 = (sx1 * x2 + sx2 * y2)%m;
            unsigned long t_y2 = (sy1 * x2 + sy2 * y2)%m;
            x1 = t_x1;
            y1 = t_y1;
            x2 = t_x2;
            y2 = t_y2;
        }
        unsigned long t_sx1 = (sx1 * sx1 + sx2 * sy1)%m;
        unsigned long t_sy1 = (sy1 * sx1 + sy2 * sy1)%m;
        unsigned long t_sx2 = (sx1 * sx2 + sx2 * sy2)%m;
        unsigned long t_sy2 = (sy1 * sx2 + sy2 * sy2)%m;
        /*
        cout<<t_sx1<<' '<<t_sy1<<' '<<t_sx2<<' '<<t_sy2<<endl;*/
        sx1 = t_sx1;
        sy1 = t_sy1;
        sx2 = t_sx2;
        sy2 = t_sy2;
        n /= 2;
    }
    /*
    cout<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;*/
    result[0] = x1;
    result[1] = y1;
    result[2] = x2;
    result[3] = y2;
    return result;

}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int input;
    cin>>input;
    for (int i=0; i < input; i ++){
        int a,b,n;
        cin>>a>>b>>n;

        long* result = fastpow(1,1,1,0,n-1,1000000007);
        unsigned long b1 = b * result[0] + a * result[1];
        long a1 = b * result[2] + a * result[3];
        cout<<b1%1000000007<<endl;
        delete[] result;
    }


    return 0;
}