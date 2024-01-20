/*
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
*/
void swap(int* nums, int i, int j){
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
void maxHeapify(int* nums, int numsSize){
    for(int p = numsSize/2 + numsSize%2 - 1; p >= 0; p--){
        maxSiftDown(nums, numsSize, p);
    }
}
void maxSiftDown(int* heap, int heapSize, int p){
    while(p < heapSize){
        int c1 = p*2+1;
        int c2 = c1+1;
        if(c2 < heapSize){// 2 children
            int largestChild = heap[c1] > heap[c2]? c1 : c2;
            if(heap[p] < heap[largestChild]){
                swap(heap, p, largestChild);
                p = largestChild;
            }else{
                break;
            }
        }else if(c1 < heapSize && heap[p] < heap[c1]){// 1 child
            swap(heap, p, c1);
            p = c1;
        }else{// leaf node
            break;
        }
    }
}
void heapSort(int* nums, int numsSize){
    maxHeapify(nums, numsSize);
    int heapSize = numsSize;
    for(int i = 0; i < numsSize-1; i++){
        swap(nums, 0, heapSize-1);// swap max value to the tail
        heapSize--; // heapSize represents the unsorted partition
        maxSiftDown(nums, heapSize, 0);// sift down the swapped head
    }
}

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    if(sSize == 0){
        return 0;
    }
    heapSort(g, gSize);
    heapSort(s, sSize);
    //qsort(g, gSize, sizeof(int), compare);
    //qsort(s, sSize, sizeof(int), compare);
    
    int output = 0;
    int l = 0;
    int r = 0;
    while(l < gSize && r < sSize){
        if(g[l] > s[r]){
            while(r < sSize && s[r] < g[l]){
                r++;
            }
        }else{
            output++;
            l++;
            r++;
        }
    }
    return output;
}