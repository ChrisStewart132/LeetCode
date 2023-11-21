/*
Given an integer x, return true if x is a
palindrome
, and false otherwise.
 
*/

int numDigits(int n){
    int nDigits = 0;
    while(n > 0) {
        nDigits += 1;
        n /= 10;
    }
    return nDigits;
}

bool isPalindrome(int x){
    if(x < 0) {
        return false;
    }
    int nDigits = numDigits(x);// calculate the number of digits to allocate the stack dynamically
    //printf("nDigits: %d\n", nDigits);
    // alternatively a static stack and index could be used/re-used per problem
    size_t stack_size = sizeof(int) * nDigits;
    int* stack = (int*)malloc(stack_size);
    memset(stack, 0, stack_size);

    for(int i = 0; i < nDigits; i++) {//fill the stack with all the digits of x
        stack[i] = x % 10;// add last digit to stack
        //printf("%d, %d\n", x, stack[i]);
        x /= 10;// integer divide x removing the last digit and shifting left 1 decimal
    }

    int i = 0;
    int j = nDigits-1;
    while(i < j){
        if(stack[i++] != stack[j--]) {
            free(stack);// free the dynamically allocated stack
            return false;
        }
    }

    free(stack);// free the dynamically allocated stack
    return true;
}