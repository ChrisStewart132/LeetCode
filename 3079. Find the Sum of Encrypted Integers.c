/*
You are given an integer array nums containing positive integers. We define a function 
encrypt such that encrypt(x) replaces every digit in x with the largest digit in x.
 For example, encrypt(523) = 555 and encrypt(213) = 333.

Return the sum of encrypted elements.
*/
int encrypt(int num){
    int maxDigit = num % 10;
    int nDigits = 0;
    while(num > 0){
        int digit = num%10;
        maxDigit = digit > maxDigit ? digit : maxDigit;
        nDigits++;
        num /= 10;
    }
    int output = maxDigit;
    while(nDigits-- > 1){
        output *= 10;
        output += maxDigit;
    }
    printf("output:%d, nDigits:%d, maxDigit:%d\n", output, nDigits, maxDigit);
    return output;
}

int sumOfEncryptedInt(int* nums, int numsSize) {
    int sum = 0;
    for(int i = 0; i < numsSize; i++){
        sum += encrypt(nums[i]);
    }
    return sum;
}