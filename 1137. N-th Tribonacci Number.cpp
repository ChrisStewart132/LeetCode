/*
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
*/
class Solution {
public:
    int tribonacci(int n) {
        std::vector<unsigned int>cache = {0,1,1,2};
        for(int i = 3; i <= n; i++){
            cache[3] = cache[0] + cache[1] + cache[2];
            cache[0] = cache[1];
            cache[1] = cache[2];
            cache[2] = cache[3];
        }
        return cache[min(n,2)];
    }
};