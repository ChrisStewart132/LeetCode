/*
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
*/

class Solution {
public:
    // returns the 2d vector representing the pascals triangle
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> arr;
        _generate(arr, numRows-1);
        return arr;
    }
    
    // recursively add rows to the triangle
    void _generate(vector<vector<int>>& arr, int numRows) {
        vector<int> v;
        if(numRows == 0) {
            v.push_back(1);
            arr.push_back(v);
            return;
        } 

        // DFS recursion from the bottom of the triangle to the top base case of 1
        _generate(arr, numRows-1);   

        // reference the row above
        v.push_back(1);
        vector<int> parent = arr[numRows-1];
        for(int i = 1; i < parent.size(); i++){
            v.push_back(parent[i-1] + parent[i]);
        }
        v.push_back(1);

        arr.push_back(v);   
    }
};