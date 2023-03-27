#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int num = 1;

struct lista
{
    int numero;
    char *prioridade;
    struct lista *prox;
};

typedef struct lista Lista;

// Cria uma lista vazia
Lista *lst_cria(void)
{
    return NULL;
}

// Retorna o número associado a uma prioridade, para ordenar a lista mais facilmente
int numero_associado(char *prioridade)
{
    if (strcmp(prioridade, "Vermelha") == 0)
        return 1;
    if (strcmp(prioridade, "Amarela") == 0)
        return 2;
    if (strcmp(prioridade, "Verde") == 0)
        return 3;
    return 0;
}

// ordem de prioridade: Vermelha, Amarela, Verde
// insere um elemento na lista de forma ordenada
Lista *lst_insere(Lista *lst, char *prioridade)
{
    // cria um novo nó
    Lista *novo = (Lista *)malloc(sizeof(Lista));
    int numero_da_prioridade = numero_associado(prioridade);
    if (numero_da_prioridade == 0)
    {
        printf("Prioridade inválida!");
        return lst;
    }
    // atribui o valor ao nó
    novo->numero = num;
    num = num + 1;                                             // incrementa o número do próximo nó (chamada futura)
    novo->prioridade = (char *)malloc(strlen(prioridade) + 1); // +1 para o \0
    strcpy(novo->prioridade, prioridade);
    // verifica se a lista está vazia
    if (lst == NULL)
    {
        // se sim, o novo nó é o primeiro e único elemento da lista
        novo->prox = NULL;
        return novo;
    }
    // se não, procura a posição correta para o novo nó
    Lista *ant = NULL; // ponteiro para o elemento anterior
    Lista *p = lst;    // ponteiro para o elemento atual

    // percorre a lista até encontrar um elemento com prioridade maior ou até o final da lista
    while (p != NULL && numero_associado(p->prioridade) <= numero_da_prioridade)
    {
        ant = p; // atualiza os ponteiros
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

// imprime a lista
void lst_imprime(Lista *lst)
{
    int verde = 0, amarela = 0, vermelha = 0;
    Lista *p = lst; // ponteiro para o elemento atual
    printf("\nImprimindo: \n");
    do
    {
        if (strcmp(p->prioridade, "Verde") == 0)
            verde = verde + 1;
        if (strcmp(p->prioridade, "Amarela") == 0)
            amarela = amarela + 1;
        if (strcmp(p->prioridade, "Vermelha") == 0)
            vermelha = vermelha + 1;
        printf("%d - %s\n", p->numero, p->prioridade); // imprime o elemento atual
        p = p->prox;                                   // atualiza o ponteiro para o próximo elemento
    } while (p != NULL);                               // repete até o final da lista
    printf("Verdes: %d | Amarelas: %d | Vermelhas: %d \n", verde, amarela, vermelha);
    return;
}

/* FUNÇÃO DE DEBUG: Busca um elemento na lista
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
*/

// remove um elemento da lista
Lista *lst_remove(Lista *lst, int val)
{
    Lista *p = lst;    // ponteiro para o elemento atual
    Lista *ant = NULL; // ponteiro para o elemento anterior
    do
    {
        if (p->numero == val) // vamos remover aqui
        {
            // caso 1: elem é o primeiro
            if (ant == NULL)
            {
                ant = lst->prox; // usa ant como buffer
                free(p->prioridade);
                free(lst);
                return ant;
            }
            // caso 2: elem é o último ou está no meio
            ant->prox = p->prox;
            free(p->prioridade);
            free(p);
            return lst;
        }
        // caminha na lista
        ant = p;
        p = p->prox;
    } while (p != NULL);
    return lst;
}

int main(void)
{
    Lista *lst = lst_cria();
    lst = lst_insere(lst, "Verde");
    lst = lst_insere(lst, "Vermelha");
    lst = lst_insere(lst, "Verde");
    lst = lst_insere(lst, "Amarela");
    lst = lst_insere(lst, "Vermelha");
    lst = lst_insere(lst, "Vermelha");
    lst = lst_insere(lst, "Verde");
    lst = lst_insere(lst, "Vermelha");
    lst_imprime(lst);
    lst = lst_remove(lst, 5);
    lst_imprime(lst);
    lst = lst_remove(lst, 4);
    lst_imprime(lst);

    lst = lst_insere(lst, "Verde");
    lst = lst_insere(lst, "Amarela");
    lst = lst_insere(lst, "Vermelha");
    lst = lst_insere(lst, "Amarela");
    lst_imprime(lst);
    lst = lst_remove(lst, 2);
    lst = lst_remove(lst, 6);
    lst_imprime(lst);
    lst = lst_remove(lst, 3);
    lst_imprime(lst);
    return 0;
}