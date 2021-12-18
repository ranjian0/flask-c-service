#include <stdio.h>

double sum(double *nums, unsigned int size) {
    double result = 0;
    for (unsigned int i = 0; i < size; i++) {
        result += nums[i];
    }
    return result;
}