#include <stdio.h>

int add(int x, int y) {
    while (y != 0) {
        // Carry contains common set bits of x and y
        int carry = x & y; 
        
        // Sum of bits where at least one bit is not set
        x = x ^ y; 
        
        // Carry is shifted by one to add it to the next position
        y = carry << 1; 
    }
    return x;
}

int main() {
    printf("Sum: %d\n", add(15, 32)); // Output: 47
    return 0;
}
