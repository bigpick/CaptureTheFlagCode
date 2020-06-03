#include <stdio.h>
#include <stdlib.h>  // rand(), srand()
#include <time.h>    // time()

int main(){

    // Epoch timestamp: 1590782400
    //                  1590849879
    // Timestamp in milliseconds: 1590782400000
    // Date and time (GMT): Friday, May 29, 2020 20:00:00
    // Date and time (your time zone): Friday, May 29, 2020 16:00:00 GMT-04:00

    time_t then = 1590782400;
    srand(then);
    printf("%d\n", rand());
    printf("%d\n", rand());
    printf("%d\n", rand());
    printf("%d\n", rand());
    printf("%d\n", rand());
    printf("%d\n", rand());

    // Watering Pattern: 150 2 103 102 192 216 52 128 9 144 10 201 209 226 22 10 80 5 102 195 23 71 77 63 111 116 219 22 113 89 187 232 198 53 146 112 119 209 64 79 236 179


    return 0;
}
