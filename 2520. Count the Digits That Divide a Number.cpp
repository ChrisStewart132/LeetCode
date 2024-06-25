/*
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
*/
class Solution {
public:
    int countDigits(int num) {
        int output = 0;
        int temp = num;
        while(temp > 0){
            int digit = temp%10;
            if(num % digit == 0){
                output++;
            }
            temp -= digit;
            temp /= 10;
        }
        return output;
    }
};