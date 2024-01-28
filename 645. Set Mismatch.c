/*
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int maxElement(int* arr, int size){
    int largest = arr[0];
    for(int i = 1; i < size; i++){
        if(largest < arr[i]){
            largest = arr[i];
        }
    }
    return largest;
}

int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    int largest = maxElement(nums, numsSize);
    int* cache = (int*)calloc(sizeof(int), largest+1);

    *returnSize = 2;
    int* output = (int*)malloc(sizeof(int)*returnSize[0]);
    output[1] = largest+1;// case where the largest element was replaced
    
    // fill cache and find the duplicate number
    for(int i = 0; i < numsSize; i++){
        cache[nums[i]]++;
        if(cache[nums[i]] == 2){
            output[0] = nums[i];
        }
    }

    // find the missing number
    for(int i = 1; i < largest+1; i++){
        if(cache[i] == 0){
            output[1] = i;
        }
    }

    free(cache);
    return output;
}