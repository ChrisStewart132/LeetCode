/*
You are given an array of positive integers nums.

You have to check if it is possible to select two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.

For example, the binary representation of 5, which is "101", does not have any trailing zeros, whereas the binary representation of 4, which is "100", has two trailing zeros.

Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise.
*/
bool hasTrailingZeros(int* nums, int numsSize) {
    int numsWithTrailingZeroCount = 0;
    for(int i = 0; i < numsSize && numsWithTrailingZeroCount < 2; i++){
        if((nums[i]&1) == 0){
            numsWithTrailingZeroCount++;
        }
    }
    return numsWithTrailingZeroCount == 2;
}