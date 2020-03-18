#include <stdio.h>
#include <stdlib.h>
/**
 * Simple RNG to tests seeds fed from python
 *
 * Prints 95 entries to screen for python to parse
 */

// MUST BE COMPILED ON LINUX LIKE SO:
// gcc rng.c -o rng -Wl,--rpath=/root/to/folder/with/lib -Wl,--dynamic-linker=/root/to/folder/ld-linux-x86-64.so.2
int main(int argc, char *argv[]) {
    int seed = atoi(argv[1]);
    srand(seed);
    for (int c = 0; c <= 95; c++) {
        printf("%d ", rand());
    }
    return 0;
}
