#include <stdio.h>


// 1.5.2(1)

int main()
/* count characters in input */
{
    long nc = 0;
    
    while (getchar() != '\n') { 
        nc++;                   
    }
    
    // 1.5.2(2)
    /*
     double nc;
     for (nc = 0; getchar() != EOF; ++nc)
        ;  // Empty body 
     
     printf ("%.0f\n", nc);
    */
    
    printf("%d\n", nc);
}

