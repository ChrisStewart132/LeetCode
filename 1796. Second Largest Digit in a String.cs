/*
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.
*/
public class Solution {
    public int SecondHighest(string s) {
        int a = -1;
        int b = -1;
        foreach (char c in s){
            int i = (int)c - 48;// -48 to convert from ASCII to digit
            if(char.IsDigit(c) && i > a){
                b = a;
                a = i;
            }else if(char.IsDigit(c) && i > b && i != a){
                b = i;
            }
        }
        return b;
    }
}