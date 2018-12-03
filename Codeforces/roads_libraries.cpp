#include <bits/stdc++.h>

using namespace std;
vector<string> split_string(string);
//int adj[100001][100001] = {0};
// Complete the roadsAndLibraries function below.
long long bfs(unordered_map<int,vector<int>> &adj,vector<long long>  &visited, long long start,int clib,int croad, int n)
{
    long long result = clib;
    queue<pair<long long, long long >> pool;
    pool.push(make_pair(start,0));
    visited[start] =1;
    //cout<<start<<endl;
    while (pool.size())
    {
        pair<long long, long long>  cur = pool.front();
        pool.pop();
        long long cur_node = cur.first;
        long long cost = cur.second;
        int length = adj[cur_node].size();
        //cout<<cur_node<<' '<<length<<endl;
        
        for (int i = 0;i <length;++i)
        {
            long long temp = adj[cur_node][i];

            if (!visited[temp])
            {
                pool.push(make_pair(temp,cost+croad));
                visited[temp] = 1;
                result += croad;
            }
            
        }
    }
    return result;
}
long long roadsAndLibraries(int n, int c_lib, int c_road, vector<vector<int>> cities) {
    n = n;
    long long result = 0;
    long long nn = n;

    if (c_lib<c_road)
    {
        return nn* (long long)c_lib;
    }
    //cout<<n<<endl;
    //vector<vector<long long >> adj(n+1,vector<long long> (n+1));
    // long long adj[n+1][n+1] = {0};
    // cout<<"rua"<<endl;
    //memset(adj,0,sizeof(adj[0][0]*(2*n+2)));
    unordered_map<int,vector<int>> adj;
    vector<long long>  visited(n+1,0);

    for (int i =0;i<cities.size();++i)
    {
        long long v1 = cities[i][0];
        long long v2 = cities[i][1];
        //adj[v1][v2] = 1;
        adj[v1].push_back(v2);
        //adj[v2][v1] = 1;
        adj[v2].push_back(v1);
    }

    for (int i = 1;i<n+1;++i)
    {

        long long returned = 0;
        if (!visited[i])
        {
          
            returned = bfs(adj, visited,i,c_lib,c_road,n);
        }
        //cout<<returned<<endl;
        result += returned;
    }
 
    return result;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string nmC_libC_road_temp;
        getline(cin, nmC_libC_road_temp);

        vector<string> nmC_libC_road = split_string(nmC_libC_road_temp);

        int n = stoi(nmC_libC_road[0]);

        int m = stoi(nmC_libC_road[1]);

        int c_lib = stoi(nmC_libC_road[2]);

        int c_road = stoi(nmC_libC_road[3]);

        vector<vector<int>> cities(m);
        for (int i = 0; i < m; i++) {
            cities[i].resize(2);

            for (int j = 0; j < 2; j++) {
                cin >> cities[i][j];
            }

            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        //cout<<"1"<<endl;
        long long result = roadsAndLibraries(n, c_lib, c_road, cities);
        printf("%lld\n",result);
        fout << result << "\n";
    }

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
