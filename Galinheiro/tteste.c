#include <stdio.h>
#include <stdlib.h>

struct nodo
{
    struct nodo *esq;
    struct nodo *dir;
    unsigned int num;
    char op;
};

struct nodo2
{
    int num;
    struct nodo2 *esq;
    struct nodo2 *dir;
};

int main(void)
{
    // compare struct sizes
    printf("sizeof(struct nodo) = %lu bytes, sizeof(struct nodo2) = %lu bytes", sizeof(struct nodo), sizeof(struct nodo2));
    return 0;
}