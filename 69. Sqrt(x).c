/*
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
*/
int mySqrt(int x) {
    if(x == 0){
        return 0;
    }
    if(x < 4){
        return 1;
    }
    int l = 0;
    int r = x;
    int m;
    while(l <= r){
        m = (l+r)/2;
        int target = x/m;
        //printf("l:%d r:%d m:%d sqr:%d\n",l,r, m, sqr);
        if(m == target){
            return m;
        }else if(m > target){
            r = m-1;
        }else{
            l = m+1;
        }
    }
    return r;
}