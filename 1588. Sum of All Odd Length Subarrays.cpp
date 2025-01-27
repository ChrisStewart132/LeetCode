/*
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
*/
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int output = 0;
        for(int i = 1; i <= arr.size(); i+=2){// sub arr len
            for(int j = 0; j <= arr.size() - i; j++){// each sub arr of length i
                for(int k = j; k < j+i; k++){// add the elements of the sub arr to output
                    output += arr[k];
                }
            }
        }
        return output;
    }
};