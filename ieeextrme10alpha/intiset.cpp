#include <iostream>
#include <map>
using namespace std;

//Calculate greatest common divisor (extended Euclidean algorithm)
long gcdr(long a, long b) {
  if(a == 0) return b;
  return gcdr(b % a, a);
}

int main() {
	int numTestCases = 0;
	long n = 0, a = 0, b = 0;
	long sum = 0;
	bool flag = false;

	cin >> numTestCases;
	for(int testCase = 0; testCase < numTestCases; testCase++) {
		cin >> n;
		cin >> a;
		cin >> b;
		sum = 0;
		flag = false;
		map<long,bool> divisors;

		for(long i = a, j = 0; i <= b; i++) {
			for(pair<long,bool> val : divisors) {
				if(i % val.first == 0) {
					flag = true;
					break;
				}
			}
			if(flag) {flag = false; continue;}

			long result = gcdr(n, i);
			if(result == 1) {
				sum = (sum + i) % 1000000007;
			} else if(divisors.find(result) == divisors.end()) {
				divisors.insert(make_pair(result, false));
			}
		}
		cout << sum << endl;
	}

	return 0;
}
