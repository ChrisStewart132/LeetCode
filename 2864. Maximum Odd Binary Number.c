/*
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.
*/
char* maximumOddBinaryNumber(char* s){
    int count[2] = {0,0};
    char* temp = s;
    while(*temp != '\0'){
        if(*temp == '0'){
            count[0]++;
        }else{
            count[1]++;
        }
        temp++;
    }
    temp = s;
    while(*temp != '\0'){
        if(count[1]-- > 1){
            *temp = '1';
        }else if (count[0]-- > 0){
            *temp = '0';
        }else{
            *temp = '1';
        }
        temp++;
    }
    return s;
}