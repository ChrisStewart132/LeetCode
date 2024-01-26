/*
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int* output = calloc(sizeof(digits[0]),(digitsSize+1));
    *returnSize = digitsSize;
    output[0] = 0;
    output[digitsSize] = 1;
    for(int i = digitsSize-1; i > -1; i--){
        output[i+1] += digits[i];
        if(output[i+1] == 10){
            output[i+1] = 0;
            output[i] += 1;
        }
    }
    if(output[0] == 1){
        *returnSize = digitsSize+1;
        return output;
    }
    return &output[1];
}