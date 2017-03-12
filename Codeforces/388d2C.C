#include <bits/stdc++.h>
using namespace std;
char s[200005];
int main() {
  queue<int> d, r;
  int n;
  scanf("%d %s", &n, s);
  for (int i = 0; i < n; i++) {
    if (s[i] == 'D') {
      d.push(i);
    } else {
      r.push(i);
    }
  }
  int t = n;
  while (!d.empty() && !r.empty()) {
    if (d.front() < r.front()) {
      d.push(t++);
      d.pop();
      r.pop();
    } else {
      r.push(t++);
      r.pop();
      d.pop();
    }
  }
  if (!d.empty()) {
    printf("D\n");
  } else {
    printf("R\n");
  }
  return 0;
}