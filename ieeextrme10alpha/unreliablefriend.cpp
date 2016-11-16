#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

enum balloon_t {RGB = 0, R, G, B, RG, RB, GB};

int main() {
	int numTestCases = 0;
	int numQuestions = 0, numLies = 0;
	string questionType;
	string answer;
	balloon_t balloons[10];

	cin >> numTestCases;
	for(int testcase = 0; testcase < numTestCases; testcase++) {
		//For each testcase...
		cin >> numQuestions;
		cin >> numLies;
		for(int i = 0; i < 10; i++) {
			balloons[i] = RGB;
		}

		for(int question = 0; question < numQuestions; question++) {
			//For each question...
			cin >> questionType;
			//TODO: Important bit
			//TODO: Important bit
			//TODO: Important bit
			cin >> answer;
		}

		for(int i = 0; i < 10; i++) {
			switch(balloons[i]) {
				case RGB:
					cout << "rgb ";
					break;
				case R:
					cout << "r ";
					break;
				case G:
					cout << "g ";
					break;
				case B:
					cout << "b ";
					break;
				case RG:
					cout << "rg ";
					break;
				case RB:
					cout << "rb ";
					break;
				case GB:
					cout << "gb ";
					break;
			}
		}
		cout << endl;
	}
	return 0;
}
