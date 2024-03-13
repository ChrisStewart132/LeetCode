/*
Given a positive integer n, find the pivot integer x such that:

    The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
*/
class Solution {
public:
    int sum(int n){
        return n*(n+1)/2;
    }
    int search(int n){
        int l = 1;
        int r = n;
        int total = sum(n);
        while(l <= r){
            int m = (l+r)/2;
            int leftTotal = sum(m-1);
            int rightTotal = total - sum(m);
            if(leftTotal == rightTotal){
                return m;
            } else if(leftTotal < rightTotal){
                l = m+1;
            }else{
                r = m-1;
            }
        }
        return -1;
    }
    int pivotInteger(int n) {
        return search(n);
    }
};