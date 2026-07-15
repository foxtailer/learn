#include <stdio.h>


// 1.2(1)

int main()
/* print Fahrenheit-Celsius table for f = 0, 20, ..., 300 */
{
    int lower, upper, step;
    float fahr, celsius;

    lower = 0; /* lower limit of temperature table */
    upper = 300; /* upper limit */
    step = 20; /* step size */

    fahr = lower;

    printf("Cels Fahr\n");

    // 1.3(1)
    for (celsius = upper; celsius >= lower; celsius = celsius - step) {
        printf("%4.0f %10.2f\n", celsius, celsius * 1.8 + 32);
    }
    
    /*
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%4.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
    */
}

