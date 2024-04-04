/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
*/
int hammingDistance(int x, int y) {
    int xor = x^y;
    int d = 0;
    while(xor > 0){
        d += xor & 1;
        xor>>=1;
    }
    return d;
}