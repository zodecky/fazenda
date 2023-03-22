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
    // cria um novo nó
    Lista *novo = (Lista *)malloc(sizeof(Lista));
    // atribui o valor ao nó
    novo->numero = num;
    // verifica se a lista está vazia
    if (lst == NULL)
    {
        // se sim, o novo nó é o primeiro e único elemento da lista
        novo->prox = NULL;
        return novo;
    }
    // se não, procura a posição correta para o novo nó
    Lista *ant = NULL;
    Lista *p = lst;
    while (p != NULL && p->numero < num)
    {
        ant = p;
        p = p->prox;
    }
    // se a lista está vazia ou o novo elemento for menor que o primeiro, insere no início
    if (ant == NULL)
    {
        novo->prox = lst;
        return novo;
    }
    // se não, insere no meio ou no fim
    ant->prox = novo;
    novo->prox = p;
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