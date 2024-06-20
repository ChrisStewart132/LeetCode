//Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.
class Solution {
public:
    string removeTrailingZeros(string num) {
        int i = num.size()-1;
        for(; i>-1 && num[i] == '0';i--){
        }
        return num.substr(0, i+1);
    }
};s