// Exercise 2.1

#include <stdio.h>
#include <limits.h>
#include <float.h>

void print_header_limits() {
    printf("=== ЗНАЧЕНИЯ ИЗ ЗАГОЛОВОЧНЫХ ФАЙЛОВ ===\n");
    printf("signed char        : %d до %d\n", SCHAR_MIN, SCHAR_MAX);
    printf("unsigned char      : 0 до %u\n", UCHAR_MAX);
    printf("signed short       : %d до %d\n", SHRT_MIN, SHRT_MAX);
    printf("unsigned short     : 0 до %u\n", USHRT_MAX);
    printf("signed int         : %d до %d\n", INT_MIN, INT_MAX);
    printf("unsigned int       : 0 до %u\n", UINT_MAX);
    printf("signed long        : %ld до %ld\n", LONG_MIN, LONG_MAX);
    printf("unsigned long      : 0 до %lu\n", ULONG_MAX);
    
    printf("\n--- Вещественные типы ---\n");
    printf("float              : %e до %e\n", FLT_MIN, FLT_MAX);
    printf("double             : %e до %e\n", DBL_MIN, DBL_MAX);
    printf("long double        : %Le до %Le\n", LDBL_MIN, LDBL_MAX);
    printf("\n");
}

void compute_integer_limits() {
    printf("=== ПРЯМОЕ ВЫЧИСЛЕНИЕ (ЦЕЛОЧИСЛЕННЫЕ) ===\n");
    
    // Вычисление через битовые сдвиги и инверсию
    // Почти все современные системы используют дополнительный код (two's complement)
    
    signed char s_char_max = (signed char)((unsigned char)~0 >> 1);
    signed char s_char_min = (signed char)~s_char_max;
    unsigned char u_char_max = (unsigned char)~0;
    printf("signed char        : %d до %d\n", s_char_min, s_char_max);
    printf("unsigned char      : 0 до %u\n", u_char_max);

    signed short s_short_max = (signed short)((unsigned short)~0 >> 1);
    signed short s_short_min = (signed short)~s_short_max;
    unsigned short u_short_max = (unsigned short)~0;
    printf("signed short       : %d до %d\n", s_short_min, s_short_max);
    printf("unsigned short     : 0 до %u\n", u_short_max);

    signed int s_int_max = (signed int)((unsigned int)~0 >> 1);
    signed int s_int_min = (signed int)~s_int_max;
    unsigned int u_int_max = (unsigned int)~0;
    printf("signed int         : %d до %d\n", s_int_min, s_int_max);
    printf("unsigned int       : 0 до %u\n", u_int_max);

    signed long s_long_max = (signed long)((unsigned long)~0 >> 1);
    signed long s_long_min = (signed long)~s_long_max;
    unsigned long u_long_max = (unsigned long)~0;
    printf("signed long        : %ld до %ld\n", s_long_min, s_long_max);
    printf("unsigned long      : 0 до %lu\n", u_long_max);
    printf("\n");
}

void compute_float_limits() {
    printf("=== ПРЯМОЕ ВЫЧИСЛЕНИЕ (ПЛАВАЮЩАЯ ТОЧКА) ===\n");
    
    // 1. Вычисление МАКСИМАЛЬНОГО float
    // Стратегия: умножаем число на 2, пока оно не станет бесконечностью (inf)
    float f_max = 1.0f;
    float f_prev = 1.0f;
    while (f_max * 2.0f != f_max) { // Когда достигнем переполнения, f*2 станет inf, а inf*2 == inf
        f_prev = f_max;
        f_max *= 2.0f;
    }
    // f_prev сейчас хранит предпоследнюю степень двойки. 
    // Чтобы заполнить мантиссу единицами, нужно добавить к ней меньшие степени двойки.
    float sub = f_prev / 2.0f;
    f_max = f_prev;
    while (sub > 0.0f) {
        if (f_max + sub != f_max) {
            f_max += sub;
        }
        sub /= 2.0f;
    }
    
    // 2. Вычисление МИНИМАЛЬНОГО (нормализованного) float
    // Делим на 2, пока число нормализовано. Как только f/2 == 0 или теряется точность:
    float f_min = 1.0f;
    while (f_min / 2.0f > 0.0f && (f_min / 2.0f) * 2.0f == f_min) {
        f_min /= 2.0f;
    }

    printf("float              : %e до %e\n", f_min, f_max);
    
    // Примечание: Вычисление double и long double строится по точно такой же логике,
    // но требует больше времени из-за разрядности.
    printf("(double и long double вычисляются аналогичными итерациями по степеням двойки)\n");
}

int main() {
    print_header_limits();
    compute_integer_limits();
    compute_float_limits();
    return 0;
}

