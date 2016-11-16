#include <iostream>
#include <vector>
using namespace std;

int main() {
	int numTestCases = 0;
	int numGames = 0, numPiles = 0, numStones = 0;
	int numSwitches = 0;

	cin >> numTestCases;
	for(int testCase = 0; testCase < numTestCases; testCase++) {
		numSwitches = 0;
		cin >> numGames;
		vector<int> piles;
		for(int game = 0; game < numGames; game++) {
			cin >> numPiles;
			for(int pile = 0; pile < numPiles; pile++) {
				cin >> numStones;
				piles.push_back(numStones);
			}
		}

		for(int pile : piles) {
			numSwitches += (pile - 1) / 2;
		}

		if(numSwitches % 2 == 0) {
			cout << "Bob" << endl;
		} else {
			cout << "Alice" << endl;
		}
	}

	return 0;
}
