#include <stdio.h>
// gcc teste.c lab9_2.s -o main -no-pie -Wall
int main(void)
{
    for (int i = 0; i < 8; i++)
        printf("Fatorial de %d = %d\n", i, fat(i));
    return 0;
}