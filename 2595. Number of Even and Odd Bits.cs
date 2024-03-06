/*
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].
*/
public class Solution {
    public int[] EvenOddBit(int n) {
        int[] pair = new int[2];
        for(int i = 0; n > 0; i++){
            //Console.WriteLine($"{n} {n&1}");
            if(i % 2 == 0){
                pair[0] += n&1;
            }else{
                pair[1] += n&1;
            }
            n>>=1;
        }
        return pair;
    }
}