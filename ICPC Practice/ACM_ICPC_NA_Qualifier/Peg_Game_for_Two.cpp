#include<iostream>
#include<vector>
using namespace std;

// 7 turns

struct point {
	int x;
	int y;
	point(int x_val, int y_val) {
		x = x_val;
		y = y_val;
	}
};

bool in_bound(int x, int y) {
	return (0 <= x) && (x < 5) && (0 <= y) && (y <= x);
}

void step(vector<vector<int>>& board, vector<point>& zeros, int& score) {
	int max_score = 0;
	int max_x = -1;
	int max_y = -1;
	int max_i = -1;
	int temp_x, temp_y;
	for (int i = 0; i < zeros.size(); ++i) {

		temp_x = zeros[i].x - 2;
		temp_y = zeros[i].y - 2;
		cout<<i<<endl;
		cout<<temp_x << " " << temp_y<<endl;
		if (in_bound(temp_x, temp_y) && board[temp_x][temp_y] != 0) {
			if (max_score < board[temp_x][temp_y] * board[temp_x + 1][temp_y + 1]) {
				max_score = board[temp_x][temp_y] * board[temp_x + 1][temp_y + 1];
				max_i = i;
				max_x = temp_x;
				max_y = temp_y;
			}
		}
		
		temp_x = zeros[i].x - 2;
		temp_y = zeros[i].y;
		cout<<temp_x << " " << temp_y<<endl;
		if (in_bound(temp_x, temp_y) && board[temp_x][temp_y] != 0) {
			cout<<1<<endl;
			if (max_score < board[temp_x][temp_y] * board[temp_x + 1][temp_y]) {
				max_score = board[temp_x][temp_y] * board[temp_x + 1][temp_y];
				max_i = i;
				max_x = temp_x;
				max_y = temp_y;
			}
		}
		
		temp_x = zeros[i].x;
		temp_y = zeros[i].y - 2;
		cout<<temp_x << " " << temp_y<<endl;
		if (in_bound(temp_x, temp_y) && board[temp_x][temp_y] != 0) {
			if (max_score < board[temp_x][temp_y] * board[temp_x][temp_y + 1]) {
				max_score = board[temp_x][temp_y] * board[temp_x][temp_y + 1];
				max_i = i;
				max_x = temp_x;
				max_y = temp_y;
			}
		}

		temp_x = zeros[i].x;
		temp_y = zeros[i].y + 2;
		cout<<temp_x << " " << temp_y<<endl;
		if (in_bound(temp_x, temp_y) && board[temp_x][temp_y] != 0) {
			if (max_score < board[temp_x][temp_y] * board[temp_x][temp_y - 1]) {
				max_score = board[temp_x][temp_y] * board[temp_x][temp_y - 1];
				max_i = i;
				max_x = temp_x;
				max_y = temp_y;
			}
		}

		temp_x = zeros[i].x + 2;
		temp_y = zeros[i].y;
		cout<<temp_x << " " << temp_y<<endl;
		// int ah = in_bound(temp_x, temp_y);
		// cout<<ah<<endl;
		// int ha = board[temp_x][temp_y];
		// cout<<ha<<endl;
		// cout<<"out"<<endl;
		if (in_bound(temp_x, temp_y) && board[temp_x][temp_y] != 0) {
			cout<<"rua"<<endl;
			if (max_score < board[temp_x][temp_y] * board[temp_x - 1][temp_y]) {
				max_score = board[temp_x][temp_y] * board[temp_x - 1][temp_y];
				max_i = i;
				max_x = temp_x;
				max_y = temp_y;
			}
		}
		cout<<"post?"<<endl;
		temp_x = zeros[i].x + 2;
		temp_y = zeros[i].y + 2;
		cout<<temp_x << " " << temp_y<<endl;
		if (in_bound(temp_x, temp_y) && board[temp_x][temp_y] != 0) {
			if (max_score < board[temp_x][temp_y] * board[temp_x - 1][temp_y - 1]) {
				max_score = board[temp_x][temp_y] * board[temp_x - 1][temp_y - 1];
				max_i = i;
				max_x = temp_x;
				max_y = temp_y;
			}
		}
		cout<<123<<endl;
	}

	score += max_score;
	cout << 111 << endl;
	point p1(max_x, max_y);
	point p2((zeros[max_i].x + max_x) / 2, (zeros[max_i].y + max_y) / 2);
	cout << 222 << endl;
	board[p1.x][p1.y] = 0;
	board[p2.x][p2.y] = 0;
	cout << 333 << endl;
	zeros.push_back(p1);
	zeros.push_back(p2);
	cout << 444 << endl;
	zeros.erase(zeros.begin() + max_i);
	cout << 555 << endl;
}

int main() {
	vector<vector<int>> board;
	vector<point> zeros;
	for (int i = 0; i < 5; ++i) {
		vector<int> tl;
		for (int j = 0; j <= i; ++j) {
			int temp;
			cin >> temp;
			if (temp == 0) {
				point start(i, j);
				zeros.push_back(start);
			}
			tl.push_back(temp);
		}
		board.push_back(tl);
	}

	int j_score = 0;
	int a_score = 0;

	for (int i = 0; i < 7; ++i) {
		// turns
		step(board, zeros, j_score);
		step(board, zeros, a_score);
	}

	int ans = j_score - a_score;
	cout << ans << endl;
	return 0;
}