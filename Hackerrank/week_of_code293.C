#include <bits/stdc++.h>

using namespace std;
#include <cmath>//for pow
#include <algorithm>//for min
int main(){
    int w;
    int h;
    cin >> w >> h;
    int circleX;
    int circleY;
    int r;
    cin >> circleX >> circleY >> r;
    int x1;
    int y1;
    int x3;
    int y3;
    cin >> x1 >> y1 >> x3 >> y3;
    int sdx = abs(x1-x3);
    int sdy = abs(y1-y3);
    /*
    if (sdx == 0|sdy==0){
        if (sdx >0){
            int x2 = min(x1,x3) + sdx/2;
            int y2 = y1 - sdx/2;
            int x4 = min(x1,x3) +sdx/2;
            int y4 = y1 + sdx/2;
        }
        else{
            int x2 = min(x1,x3) - sdx/2;
            int y2 = min(y1,y3) - sdx/2;
            int x4 = min(x1,x3) +sdx/2;
            int y4 = min(y1,y3) - sdx/2;
        }
    }
    else{
        if (sdx == sdy){
            int x2 = min(x1,x3) + sdx;
            int y2 = y1 if (x1 < x3) else y3;
            int x4 = max(x1,x3) - sdx;
            int y4 = y2 if (x1 < x3) else y1;
        }
        else{
            if (sdx>sdy){
                int ddy = sdx-sdy;
                int x2 = min(x1, x3)+max(ddy,sdy) if (y1 > y3) else min(x1, x3)+min(ddy,sdy);
                int y2 = y1 + min(ddy,sdy) if (y1<y3) else y1+max(ddy,sdy);
                int x4 = min(x1, x3)+min(ddy,sdy) if (y1 > y3) else min(x1, x3)+max(ddy,sdy);
                int y4 = y1 + max(ddy,sdy) if (y1<y3) else y1+min(ddy,sdy);
            }
        }
    }*/
    // MUCH Better way //lst
    int mx = (x1 + x3)/2;
    int my = (y1 + y3)/2;
    int tx = (y3-y1)/2;
    int ty = (x1-x3)/2;
    int x2 = mx + tx;
    int y2 = my + ty;
    int x4 = mx - tx;
    int y4 = my - ty;
    //printf("p2(%d,%d) p4(%d,%d) \n",x2,y2,x4,y4);
    for (int i =0; i<h; ++i){
        int dy = abs(circleY-i);
        for (int j = 0; j<w; ++j){
            //check if it is in a circle
            int dx = abs(circleX-j);
            float ed = sqrt(pow(dx,2) + pow(dy,2));
            //printf("%d %d %f\n",dx,dy,ed );
            if (ed<=r){
                printf("#");
            }
            else{
                float amx = j - x1;
                float amy = i - y1;
                float abx = x2-x1;
                float aby = y2-y1;
                float adx = x4-x1;
                float ady = y4-y1;
                float nmb = (amx * abx + amy * aby);
                float cnm = (abx * abx) + aby*aby;
                float nmb2= amx * adx + amy * ady;
                float cnm2 = adx * adx + ady * ady;

                if ((0<=nmb && nmb <= cnm)&&(0<=nmb2 && nmb2 <= cnm2)){
                    printf("#");
                }else{
                    printf(".");
                }

            }

        }
        printf("\n");
    }
    return 0;
}
