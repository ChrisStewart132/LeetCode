/*
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
*/
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int l = 0;
        for(int i = 1; i < arr[arr.size()-1]; i++){
            if(arr[l] > i){
                k--;
            }else{
                l++;
            }
            if(k == 0){
                return i;
            }
        }
        return arr[arr.size()-1]+k;
    }
};