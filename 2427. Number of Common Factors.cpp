/*
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.
*/
class Solution {
public:
    int commonFactors(int a, int b) {
        int output = 0;
        for(int i = std::max(a, b); i > 0; i--){
            output = a%i==0 && b%i==0 ? output+1 : output;
        }
        return output;
    }
};