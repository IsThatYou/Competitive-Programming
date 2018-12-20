#include <iostream>
using namespace std;
#define N 100
void multiply(int mat1[][N],  
              int mat2[][N],  
              int res[][N]) 
{ 
    int i, j, k; 
    for (i = 0; i < N; i++) 
    { 
        for (j = 0; j < N; j++) 
        { 
            res[i][j] = 0; 
            for (k = 0; k < N; k++) 
                res[i][j] += mat1[i][k] *  
                             mat2[k][j]; 
        } 
    } 
} 
int main()
{
	int n;
	cin>>n;
	int total_node = n*(n+1)/2;
	int value[total_node];
	for (int i = 0;i< total_node;++i)
	{
		cin>>value[i];
	}
    double res[N][N]; // To store result 
    double mat1[N][N] = {0};
    int p0,p1,p2,p3,p4
    for (int i = 0;i<total_node;++i)
    {
    	
    	k = i + 1;
    	p
    }
  
    // multiply(mat1, mat2, res); 
  
    // for (i = 0; i < N; i++) 
    // { 
    //     for (j = 0; j < N; j++) 
    //     cout << res[i][j] << " "; 
    //     cout << "\n"; 
    // } 
  
    return 0;
}