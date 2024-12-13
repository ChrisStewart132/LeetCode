//Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
bool hasAlternatingBits(int n) {
    int prev_bit = n&1 == 1? 0 : 1;
    while(n > 0){
        int last_bit = n&1;
        if(last_bit == prev_bit){
            return false;
        }
        prev_bit = last_bit;
        n >>= 1;
    }
    return true;
}