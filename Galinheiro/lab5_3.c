#include <stdio.h>

struct X1
{
    char c1;
    int i;
    char c2;
};
struct X2
{
    long l;
    char c;
};

struct X3
{
    int i;
    char c1;
    char c2;
};
struct X4
{
    struct X2 x;
    char c;
};
struct X5
{
    char c1;
    char c2;
    char c3;
};

struct X6
{
    short s1;
    int i;
    char c[3];
    short s2;
};

union U1
{
    int i;
    char c[5];
};

union U2
{
    short s;
    char c[5];
};
void dump(void *ptr, size_t size)
{
    unsigned char *p = ptr;
    printf("size = %ld\n", size);
    while (size--)
        printf("%p - %02x\n", p++, *p);
}

int main()
{
    struct X1 x1;
    struct X2 x2;
    struct X3 x3;
    struct X4 x4;
    struct X5 x5;
    struct X6 x6;
    union U1 u1;
    union U2 u2;

    printf("dumping struct X1\n");
    dump(&x1, sizeof(x1));
    printf("dumping struct X2\n");
    dump(&x2, sizeof(x2));
    printf("dumping struct X3\n");
    dump(&x3, sizeof(x3));
    printf("dumping struct X4\n");
    dump(&x4, sizeof(x4));
    printf("dumping struct X5\n");
    dump(&x5, sizeof(x5));
    printf("dumping struct X6\n");
    dump(&x6, sizeof(x6));
    printf("dumping union U1\n");
    dump(&u1, sizeof(u1));
    printf("dumping union U2\n");
    dump(&u2, sizeof(u2));
    return 0;
}