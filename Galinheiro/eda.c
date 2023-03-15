#include <stdio.h>
#include <stdlib.h>

struct lista
{
    int numero;
    struct lista *prox;
};

typedef struct lista Lista;

Lista *lst_cria(void)
{
    return NULL;
}

Lista *lst_insere(Lista *lst, int num)
{
    Lista *novo = (Lista *)malloc(sizeof(Lista));
    novo->numero = num;
    novo->prox = lst;
    return novo;
}

void lst_imprime(Lista *lst)
{
    Lista *p = lst;
    printf("\nImprimindo: \n");
    do
    {
        printf("Numero: %d, prox: %p\n", p->numero, p->prox);
        p = p->prox;
    } while (p != NULL);
    return;
}

Lista *lst_busca(Lista *lst, int val)
{
    Lista *p = lst;
    do
    {
        if (p->numero == val)
            return p;
        p = p->prox;
    } while (p != NULL);
    return NULL;
}

Lista *lst_remove(Lista *lst, int val)
{
    Lista *p = lst;
    Lista *ant = NULL;
    do
    {
        if (p->numero == val) // vamos remover aqui
        {
            // caso 1: elem é o primeiro
            if (ant == NULL)
            {
                ant = lst->prox; // usa ant como buffer
                free(lst);
                return ant;
            }
            ant->prox = p->prox;
            free(p);
            return lst;
        }
        ant = p;
        p = p->prox;
    } while (p != NULL);
    return lst;
}

int main(void)
{
    Lista *lst;
    lst = lst_cria();

    lst = lst_insere(lst, 20);
    lst = lst_insere(lst, 30);
    lst = lst_insere(lst, 10);
    lst = lst_insere(lst, 12);
    lst = lst_insere(lst, 4);
    lst = lst_insere(lst, 5);
    lst = lst_insere(lst, 7);

    lst_imprime(lst);

    printf("\nBuscando: 20, encontrou: %p", lst_busca(lst, 20));
    printf("\nBuscando: 30, encontrou: %p", lst_busca(lst, 30));
    printf("\nBuscando: 3, encontrou: %p", lst_busca(lst, 3));

    lst = lst_remove(lst, 30);
    lst_imprime(lst);

    lst = lst_remove(lst, 20);
    lst_imprime(lst);

    lst = lst_remove(lst, 7);
    lst_imprime(lst);

    return 0;
}
