#include <stdio.h>
#include <limits.h>

int main(void)
{
    int number;
    int current_sum = 0;
    int max_subsum = INT_MIN;

    while (scanf("%d", &number) == 1 && number != 0) {
        current_sum += number;

        if (current_sum > max_subsum)
            max_subsum = current_sum;

        if (current_sum < 0)
            current_sum = 0;
    }

    printf("%d\n", max_subsum);

    return 0;
}

