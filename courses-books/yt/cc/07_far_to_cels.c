#include <stdio.h>

/* print Fahrenheit-Celsius table
for f = 0, 20, ..., 300 */

int main()
{
    int lower, upper, step;
    float fahr, celsius;
    lower = 0; /* lower limit of temperature table */
    upper = 300; /* upper limit */
    step = 20; /* step size */
    fahr = lower;

    //printf("Fahr Cels\n");
    printf("Cels Fahr\n");

    // while (fahr <= upper) {
    //     celsius = (5.0/9.0) * (fahr-32.0);
    //     printf("%4.0f %6.1f\n", fahr, celsius);
    //     fahr = fahr + step;
    // }

    for (celsius = upper; celsius >= lower; celsius = celsius - step) {
        printf("%4.0f %6.1f\n", celsius, celsius * 1.8 + 32);
    }
}