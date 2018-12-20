
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <utility>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000") 
#define eps 1e-10
#define inf 0x3f3f3f3f
#define PI pair<int, int> 
typedef long long LL;
const int maxn = 1000 + 5;
struct job{
	int b, j;
	bool operator < (const job& p) const {
		return j > p.j;
	}
}a[maxn];
int main() {
	int n, kase = 1;
	while(scanf("%d", &n) == 1 && n) {
		for(int i = 0; i < n; ++i) scanf("%d%d", &a[i].b, &a[i].j);
		sort(a, a + n);
		int t = 0, B = 0;
		for(int i = 0; i < n; ++i) {
			t = max(t, B + a[i].b+ a[i].j);
			B += a[i].b;
		}
		printf("Case %d: %d\n", kase++, t);
	}
	return 0;
}
