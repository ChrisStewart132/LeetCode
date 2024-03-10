/*
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
*/
int* countingBuffer(int* nums, int numsSize, int min, int max, int* returnSize){
    // create a buffer of max-min+1 length
    *returnSize = max-min+1;
    int* buffer = (int*)calloc((returnSize[0]), sizeof(int));
    // key=n-min and buffer[key] = count of n in nums
    for(int i = 0;i < numsSize; i++){
        buffer[nums[i]-min] += 1;
    }
    return buffer;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int buffer1Size = 0;
    int* buffer1 = countingBuffer(nums1, nums1Size, 0, 1000, &buffer1Size);

    int buffer2Size = 0;
    int* buffer2 = countingBuffer(nums2, nums2Size, 0, 1000, &buffer2Size);

    *returnSize = 0;
    for(int i = 0; i < 1000; i++){
        if(buffer1[i] && buffer2[i]){
            (*returnSize)++;
        }
    }

    int* output = (int*)malloc(sizeof(int)*returnSize[0]);
    int j = 0;
    for(int i = 0; i < 1000; i++){
        if(buffer1[i] && buffer2[i]){
            output[j++] = i;
        }
    }
    free(buffer1);
    free(buffer2);
    return output;
}