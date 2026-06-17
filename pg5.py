#include <stdio.h>
#include <stdbool.h>

bool haveOppositeSigns(int a, int b) {
    // True if the resulting sign bit is 1 (negative number)
    return (a ^ b) < 0; 
}

int main() {
    int x = 100, y = -200;
    if (haveOppositeSigns(x, y)) {
        printf("The integers have opposite signs.\n");
    } else {
        printf("The integers have the same sign.\n");
    }
    return 0;
}
