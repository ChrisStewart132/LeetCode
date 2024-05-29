/*
You are given an array nums, where each number in the array appears either once or twice.

Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.
*/

#define LEN(b) sizeof(buffer)/sizeof(buffer[0])

int duplicateNumbersXOR(int* nums, int numsSize) {
    int output = 0;
    char buffer[51] = {0};
    for(int i = 0; i < numsSize; i++){
        buffer[nums[i]]++;
    }

    for(int i = 0; i < LEN(buffer); i++){
        if(buffer[i] == 2){
            output = output == 0 ? i : output^i;
        }
    }

    return output;
}