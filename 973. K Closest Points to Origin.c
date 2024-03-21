/*
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
*/
void swap(int** nums, int i, int j){
    int* temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
bool compare(int* a, int* b){
    return sqrt(a[0]*a[0] + a[1]*a[1]) < sqrt(b[0]*b[0] + b[1]*b[1]);
}
void siftDown(int** heap, int heapSize, int p){
    if(p >= heapSize){
        return;
    }
    int smallest = p;
    int nChildren = 2;// binary heap
    for(int c = p*2+1; c < heapSize && c < p*2+1+nChildren; c++){
        smallest = compare(heap[smallest], heap[c]) ? smallest : c;
    }
    if(smallest != p){
        swap(heap, p, smallest);
        siftDown(heap, heapSize, smallest);
    }
}
void heapify(int** nums, int numsSize){
    for(int p = numsSize/2 + numsSize%2 - 1; p > -1; p--){
        siftDown(nums, numsSize, p);
    }
}
int* pop(int** heap, int heapSize){
    swap(heap, 0, heapSize-1);
    siftDown(heap, heapSize-1, 0);
    return heap[heapSize-1];
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** kClosest(int** points, int pointsSize, int* pointsColSize, int k, int* returnSize, int** returnColumnSizes) {
    *returnSize = k;
    *returnColumnSizes = (int*)malloc(sizeof(int)*k);

    int** output = (int**)malloc(sizeof(int*)*returnSize[0]);
    heapify(points, pointsSize);
    for(int i = 0; i < k; i++){
        output[i] = (int*)malloc(sizeof(int)*2);
        returnColumnSizes[0][i] = 2;
        //printf("%d,%d\n", points[0][0], points[0][1]);
        output[i] = pop(points, pointsSize-i);
    }
    return output;
}