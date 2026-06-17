#include <stdio.h>
#include <stdbool.h>

bool isPowerOfTwo(int x) {
    // x must be greater than 0, and x & (x - 1) must equal 0
    return (x > 0) && ((x & (x - 1)) == 0);
}

int main() {
    int num = 16;
    if (isPowerOfTwo(num)) {
        printf("%d is a power of 2.\n", num);
    } else {
        printf("%d is NOT a power of 2.\n", num);
    }
    return 0;
}
