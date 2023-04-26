#include <stdio.h>

struct X
{
    int a;
    short b;
    int c;
} x = {0xa1a2a3a4, 0xb1b2, 0xc1c2c3c4};

void dump(void *ptr, size_t size)
{
    unsigned char *p = ptr;
    while (size--)
    {
        printf("%p - %02x\n", p, *p);
        p++;
    }
}

int main(void)
{
    dump(&x, sizeof(x));
    printf("Tamanho da estrutura: %ld\n", sizeof(x));
    return 0;
}