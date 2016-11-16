#include <map>
#include <set>
#include <memory>
#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
#include <istream>
#include <stack>

void open_room(std::map<std::pair<int,int>,std::set<std::pair<int,int>>> & graph, int x_coord, int y_coord, int N) {
    if (graph.count(std::pair<int,int>(x_coord,y_coord))) {
        graph[std::pair<int,int>(x_coord,y_coord)] = std::set<std::pair<int,int>>();
    }
    if (y_coord != N-1) {
        graph[std::pair<int,int>(x_coord,y_coord)].insert(std::pair<int,int>(x_coord,y_coord+1));
    } 
    if (y_coord != 0) {
        graph[std::pair<int,int>(x_coord,y_coord)].insert(std::pair<int,int>(x_coord,y_coord-1));
    } 
    if (x_coord != N-1) {
        graph[std::pair<int,int>(x_coord,y_coord)].insert(std::pair<int,int>(x_coord+1,y_coord));
    } 
    if (x_coord != 0) {
        graph[std::pair<int,int>(x_coord,y_coord)].insert(std::pair<int,int>(x_coord-1,y_coord));
    } 
}
void dfs(std::map<std::pair<int,int>,std::set<std::pair<int,int>>> & graph, std::pair<int,int> start, std::set<std::pair<int,int>> & visited) {
    std::stack<std::pair<int,int>> stack;
    stack.push(start);
    
    while ( ! stack.empty() ){
        std::pair<int,int> vertex = stack.top();
        stack.pop();
        if (visited.count(vertex) == 0) {
            visited.insert(vertex);
            std::set<std::pair<int,int>> set_difference;
            std::set_difference(graph[vertex].begin(), graph[vertex].end(), visited.begin(), visited.end(), std::inserter(set_difference, set_difference.end()));
            for (auto item : set_difference) {
                stack.push(item);
            }
        }
    }
}
int main(){
    int N, num_open_rooms = 0, x_coord, y_coord;
    bool is_maze_open = false;
    std::cin >> N;
    //std::cout << N << std::endl;
    std::map<std::pair<int,int>,std::set<std::pair<int,int>>> graph;
    
    std::cin >> x_coord;
    
    while (x_coord != -1 && !is_maze_open) {
        std::cin >> y_coord;
        --x_coord;
        --y_coord;
        open_room(graph,x_coord,y_coord,N);
        ++num_open_rooms;
        if (num_open_rooms >= N) {
            std::set<std::pair<int,int>> visited;
            for (int i = 0; i < N; ++i){
                dfs(graph, std::pair<int,int>(0,i), visited);
            }
            for (int i = 0; i < N; ++i){
                if (visited.count(std::pair<int,int>(N-1,i)) != 0) {
                    is_maze_open = true;
                    std::cout << num_open_rooms << std::endl;
                    break;
                }
            }
        }
        std::cin >> x_coord;
    }
    if (! is_maze_open) {
        std::cout << -1 << std::endl;
    }
    
    return 0;
}
