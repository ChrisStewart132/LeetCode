/*
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
*/
#include <unordered_set>
#include <utility> // for std::pair
// Custom hash functor for std::pair<int, int>
struct PairHash {
    std::size_t operator()(const std::pair<int, int>& p) const {
        return std::hash<int>{}(p.first) ^ std::hash<int>{}(p.second);
    }
};
class Solution {
public:
    bool wordExistsFromTile(vector<vector<char>>& board, string& word, int i, int j, int depth, std::unordered_set<std::pair<int, int>, PairHash>& visited){
        bool inBounds = i >= 0 && i < board.size() && j >= 0 && j < board[i].size();
        std::pair<int, int> pos(i, j);
        if(!inBounds || visited.find(pos) != visited.end()){
            return depth == word.size();
        }
        //printf("   depth:%d: dfs %d,%d,%c:%c\n", depth,i,j,board[i][j],word[depth]);
        if(depth == word.size()){
            //printf("        end %d,%d\n", i,j);
            return true;
        }
        if(board[i][j] != word[depth]){
            return false;
        }
        visited.insert(pos);
        bool u = wordExistsFromTile(board, word, i-1, j, depth+1, visited);
        bool d = wordExistsFromTile(board,word, i+1, j, depth+1, visited);
        bool l = wordExistsFromTile(board, word, i, j-1, depth+1, visited);
        bool r = wordExistsFromTile(board, word, i, j+1, depth+1, visited);
        visited.erase(pos);
        return u || d || l || r;
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                std::unordered_set<std::pair<int, int>, PairHash> visited;
                if(wordExistsFromTile(board, word, i, j, 0, visited)){
                    //printf("start %d,%d\n", i,j);
                    return true;
                }
            }
        }
        return false;
    }
};
/*
"ABCESEEEFS"
["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]]
   depth:0: dfs 0,0,A:A
   depth:1: dfs 1,0,S:B
   depth:1: dfs 0,1,B:B
   depth:2: dfs 1,1,F:C
   depth:2: dfs 0,2,C:C
   depth:3: dfs 1,2,E:E
   depth:4: dfs 2,2,E:S
   depth:4: dfs 1,1,F:S
   depth:4: dfs 1,3,S:S
   depth:5: dfs 0,3,E:E
   depth:5: dfs 2,3,E:E
   depth:6: dfs 2,2,E:E
   depth:7: dfs 2,1,D:E
   depth:0: dfs 0,1,B:A
   depth:0: dfs 0,2,C:A
   depth:0: dfs 0,3,E:A
   depth:0: dfs 1,0,S:A
   depth:0: dfs 1,1,F:A
   depth:0: dfs 1,2,E:A
   depth:0: dfs 1,3,S:A
   depth:0: dfs 2,0,A:A
   depth:1: dfs 1,0,S:B
   depth:1: dfs 2,1,D:B
   depth:0: dfs 2,1,D:A
   depth:0: dfs 2,2,E:A
   depth:0: dfs 2,3,E:A
*/