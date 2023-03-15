#include <stdio.h>
#include <stdlib.h>
struct lista
{
    int numero;
    struct lista *prox;
};

typedef struct lista Lista;

Lista *lst_ord_cria(void)
{
    return NULL;
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

Lista *lst_ord_insere(Lista *lst, int num)
{
    Lista *novo = (Lista *)malloc(sizeof(lst));
    novo->numero = num;
    novo->prox = lst;
    if (lst == NULL) // se a lista esta vazia ou o numero for o menor
    {
        return novo;
    }

    // caso nao insira no inicio
    Lista *p = lst;
    Lista *ant = NULL;
    do
    {
        if (p->numero < num)
        {
            ant = p;
            p = p->prox;
        }
        else
        {
            novo->prox = p;
            ant->prox = novo;
        }
    } while (p != NULL);
    return lst;
}

int main(void)
{
    Lista *lst = lst_ord_cria();
    lst = lst_ord_insere(lst, 10);
    lst = lst_ord_insere(lst, 20);
    lst = lst_ord_insere(lst, 30);
    lst = lst_ord_insere(lst, 40);
    lst = lst_ord_insere(lst, 50);
    lst_imprime(lst);

    lst = lst_ord_insere(lst, 25);
    lst_imprime(lst);

    lst = lst_ord_insere(lst, 5);
    lst_imprime(lst);

    lst = lst_ord_insere(lst, 55);
    lst_imprime(lst);
    return 0;
};