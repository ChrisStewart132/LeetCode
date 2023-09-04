/*
Given an m x n matrix, return all elements of the matrix in spiral order.
*/
class Solution {
public:
    void _spiralOrder(vector<vector<int>>& matrix, vector<int>& output, int m=0, int n=0, int dir=0, int depth=0) {
        if(depth > (int)(matrix.size()/2) || depth > (int)(matrix[0].size()/2)) {
            return;
        }
        
        if(dir==0) {// right  
            if(n < matrix[0].size() - depth){
                output.push_back(matrix[m][n]);
                _spiralOrder(matrix, output, m, n+1, 0, depth);
            }else if(m+1 < matrix.size() - depth){
                _spiralOrder(matrix, output, m+1, n-1, 1, depth);
            }            
        }
                
        if(dir==1 && m < matrix.size() - depth) {// down
            output.push_back(matrix[m][n]);
            _spiralOrder(matrix, output, m+1, n, 1, depth);
        }else if (dir==1 && n-1 >= 0 + depth){
            _spiralOrder(matrix, output, m-1, n-1, 2, depth);
        }
        
        
        if(dir==2 && n >= 0 + depth) {// left
            output.push_back(matrix[m][n]);
            _spiralOrder(matrix, output, m, n-1, 2, depth);
        }else if(dir==2 && m-1 > 0 + depth){
            _spiralOrder(matrix, output, m-1, n+1, 3, depth);
        }
        

        if(dir==3 && m > 0 + depth) {// up
            output.push_back(matrix[m][n]);
            _spiralOrder(matrix, output, m-1, n, 3, depth);
        }else if(dir==3 && n+2 < matrix[0].size() - depth){
            _spiralOrder(matrix, output, m+1, n+1, 0, depth+1);
        }
        
    }
    
    vector<int> spiralOrder(vector<vector<int>>& matrix){
        vector<int> output;
        _spiralOrder(matrix, output);
        return output;
    }
};