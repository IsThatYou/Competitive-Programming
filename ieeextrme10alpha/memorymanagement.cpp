#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;


class LRUCache {
private:
	// key access history, most recent at back
	list<int> lruList;
	// key to value and key history iterator
	unordered_map<int, list<int>::iterator> cache;
	size_t capacity;

public:
	LRUCache(size_t aCapacity) : capacity(aCapacity) {}

	//get value for key val
	bool operator()(int val) {
		auto it = cache.find(val);
		if(it == cache.end()) {	//cache-miss: did not find the key
			return insert(val);
		}

		// cache-hit
		// Update access record by moving accessed key to back of the list
		lruList.splice(lruList.end(), lruList, it->second);
		return true;
	}

private:
	// insert a new key-value pair in the cache
	bool insert(int val) {
		//method should be called only when cache-miss happens
		//assert(cache.find(val) == cache.end());

		// make space if necessary
		bool hasSpace = lruList.size() < capacity;
		if(!hasSpace) {evict();}

		// record k as most-recently-used key
		auto it = lruList.insert(lruList.end(), val);

		// create key-value entry, linked to the usage record
		cache.insert(make_pair(val, it));

		return hasSpace;
	}

	//Purge the least-recently used element in the cache
	void evict() {
		if(lruList.empty()) {return;}

		// identify least-recently-used key
		auto it = cache.find(lruList.front());

		//erase both elements to completely purge record
		cache.erase(it);
		lruList.pop_front();
	}
};




int main() {
	int numTestCases = 0;
	int p = 0, s = 0, n = 0;
	int num = 0;
	int page = 0;
	bool found = false;
	int qReplacements = 0;
	int lruReplacements = 0;

	cin >> numTestCases;
	for(int testCase = 0; testCase < numTestCases; testCase++) {
		cin >> p;
		cin >> s;
		cin >> n;

		list<int> q;
		LRUCache c(p);
		qReplacements = 0;
		lruReplacements = 0;

		for(int i = 0; i < n; i++) {
			//Find accessed page
			cin >> num;
			page = num/s;

			//Check queue
			for(int loadedPage : q) {
				if(loadedPage == page) {
					found = true;
					break;
				}
			}
			if(!found) {
				if(q.size() == p) {
					qReplacements++;
					q.pop_front();
				}
				q.push_back(page);
			}
			found = false;

			//Check LRU
			if(!c(page)) {
				lruReplacements++;
			}
		}
		cout << (lruReplacements < qReplacements ? "yes " : "no ");
		cout << qReplacements << " ";
		cout << lruReplacements << endl;
	}

	return 0;
}
