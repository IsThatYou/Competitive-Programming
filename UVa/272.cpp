//Author: Junlin Wang
//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=208
#include <bits/stdc++.h>
using namespace std;
int main()
{
    char ch;
    bool left = true;
    
        //bool left = true;
        while (scanf("%c",&ch)!=EOF)
        {
            if (ch =='"')
            {
                if (left)
                {
                    printf("``");
                    left = !left;
                }
                else
                {
                    printf("''");
                    left = !left;
                }
            }
            else{
                printf("%c",ch);
            }
        }
        return 0;

       
}
