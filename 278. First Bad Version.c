/*
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
*/
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n){
    // bad = move left, else right
    unsigned int l = 1;
    unsigned int r = n;
    while(l < r){
        unsigned int m = l + ((r-l)>>1);// >>1 equivalent of //2, bitwise shift right
        if(isBadVersion(m)){
            r = m;    
        }else{
            l = m+1;
        }
    }
    return isBadVersion(r)? l:-1;
}