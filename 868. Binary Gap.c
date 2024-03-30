/*
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n.
 If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
 The distance between two 1's is the absolute difference between their bit positions.
  For example, the two 1's in "1001" have a distance of 3.
*/
int binaryGap(int n) {
    // find the first 1
    while(n>0 && (n&1) == 0){
        n>>=1;
    }
    // base case
    if(n < 3){
        return 0;
    }
    // find dist to next 1 bit
    n>>=1;
    int gap = 1;
    while(n > 0){
        int bit = n&1;
        if(bit == 1){
            break;
        }else{
            gap++;
            n>>=1;
        }
    }
    int gap2 = binaryGap(n);
    return gap > gap2 ? gap : gap2;
}