//Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
double myPow(double x, int n) {
    /*
     2**4 = 2*2*2*2 == (2*2)**2 == 4**2 = 4*4 = 8
    */
    //printf("%f^%d\n",x,n);
    if(n == 0){
        return 1;
    }else if(n < 0){
        return 1 / (x * myPow(x, -(n + 1)));// -128<-0->127 fix negative limit overflow
    }else if(n&1){
        return myPow(x, n-1)*x;
    }else{
        double r = myPow(x, n/2);
        return r*r;
    }
}