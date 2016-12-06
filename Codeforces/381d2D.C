
// C++ program to print DFS traversal from a given vertex in a  given graph
#include <iostream>
#include <list>
#include <string>
#include <map>
#include <sstream>
 
using namespace std;
 
// Graph class represents a directed graph using adjacency list representation
/*
std::string to_string(int i)
{
    std::stringstream ss;
    ss << i;
    return ss.str();
}*/

class Graph
{
    int V;    // No. of vertices
    list<int> *adj;    // Pointer to an array containing adjacency lists
    void DFSUtil(int v, bool visited[], int track[], map<int, int> ances, int last);  // A function used by DFS
    int *values;
    map<string,int> dicc;
public:
    Graph(int V, int w[]);   // Constructor
    void addEdge(int v, int w);   // function to add an edge to graph
    void DFS(int v, int track[]);    // DFS traversal of the vertices reachable from v
    void setMap(map<string, int> dic);
};
 
Graph::Graph(int V, int li[])
{
    this->V = V;
    adj = new list<int>[V];
    values = li;
}
void Graph::setMap(map<string, int> dic)
{
	dicc = dic;
	/*
	std::map<std::string, int>::iterator it = dic.begin();
    while(it != dic.end())
    {
        std::cout<<it->first<<" :: "<<it->second<<std::endl;
       	it++;
    }
    */

}
void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w); // Add w to v’s list.
}
 
void Graph::DFSUtil(int v, bool visited[], int track[], map<int, int> ances, int last)
{
    // Mark the current node as visited and print it
    visited[v] = true;
    // get the edge value
    // forgive me for doing this this way
    string sp = to_string(last);
	string sj = to_string(v);
	string key = sp+sj;
 	int ev = dicc.find(key) -> second;
 	// add the edge value to all of the ancester.
 	std::map<int, int>::iterator it = ances.begin();
    while(it != ances.end())
    {
        it -> second = it -> second + ev;

        if (it -> second <= values[v]){
        	track[it -> first] += 1;
        }
       	it++;
    }
 	ances[v] = 0;

    // Recur for all the vertices adjacent to this vertex
    list<int>::iterator i;
    if (v < V){
    	
	    for (i = adj[v].begin(); i != adj[v].end(); ++i){
	        if (!visited[*i]){
	            DFSUtil(*i, visited, track, ances, v);
	        }
	    }
	}

}
 
// DFS traversal of the vertices reachable from v. 
// It uses recursive DFSUtil()
void Graph::DFS(int v, int track[])
{
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    map<int, int> ances;
    for (int i = 0; i < V; i++){
        visited[i] = false;
    }
 
    // Call the recursive helper function to print DFS traversal
    visited[v] = true;
    ances[v] = 0;
    // Recur for all the vertices adjacent to this vertex
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            DFSUtil(*i, visited, track, ances, v);
    //return track;
}

int main() {
	/*
	int a = 1000000000;
	string b = to_string(a);
	int c;
	std::stringstream ss(b);
    ss >> c;
	cout<<c<<endl;
	*/
	int n;
	cin>>n;

	int values [n];
	for (int i = 0; i < n; i++){
		int value;
		cin>>value;
		values[i] = value;
	}
	//cout<<values[4]<<endl;
	map<string, int> dic;
	Graph g(n, values);
	for (int j = 1; j < n; j++){
		int p;
		int v;
		cin>>p>>v;
		string sp = to_string(p-1);
		string sj = to_string(j);
		string key = sp+sj;
		//cout<<key<<endl;
		dic.insert(make_pair(key, v));
		g.addEdge(p-1, j);
	}
	int track[n] = {0}; 
	g.setMap(dic);
	
	g.DFS(0, track);
	for (int z =0; z<n;z++){
		cout<<track[z]<<' ';
	}
	
	//cout<<results[0]<<endl;
	/*
	std::map<std::string, int>::iterator it = dic.begin();
    while(it != dic.end())
    {
        std::cout<<it->first<<" :: "<<it->second<<std::endl;
       	it++;
    }
	*/
	return 0;
}