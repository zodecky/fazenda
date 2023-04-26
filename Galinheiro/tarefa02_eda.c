// 2210912 gabriel zagury de magalhães
// 22111171 thiago henriques

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define RANGE_MIN 1
#define RANGE_MAX 20
struct nodo
{
    int info;
    int altura;
    struct nodo *esq;
    struct nodo *dir;
};
typedef struct nodo Nodo;

struct lista
{
    Nodo *p_no;
    struct lista *corr;
    struct lista *prox;
};
typedef struct lista Fila;

struct lista_encadeada
{
    int info;
    struct lista_encadeada *prox;
};

Nodo *insere_binario(Nodo *p, int val)
{ // recebe uma arvoreG e um valor a ser inserido
    Nodo *aux;
    // se a arvoreG eh vazia, cria um no, coloca o valor nele e retorna
    if (p == NULL)
    {
        aux = (Nodo *)malloc(sizeof(Nodo));
        aux->esq = NULL;
        aux->dir = NULL;
        aux->info = val;
        return aux;
    }
    else
    {
        if (p->info > val)
        {                                         // se o valor for menor que a raiz, ele vai entrar a esquerda
            p->esq = insere_binario(p->esq, val); // entrando recursivamente na subarvoreG esquerda
        }
        else if (p->info < val)
        {                                         // se o valor for maior/igual a raiz, ele vai entrar a direita
            p->dir = insere_binario(p->dir, val); // entrando recursivamente na subarvoreG direita
        }
    }
    return p; // retorna a arvoreG com o valor inserido
}

void exibe_preordem(Nodo *p)
{
    if (p == NULL)
        printf("arvore nao foi criada\n");
    printf("chave = %d ", p->info);
    if (p->esq)
        printf(" esq = %d", p->esq->info);
    else
        printf(" esq = NULL");
    if (p->dir)
        printf(" dir = %d\n", p->dir->info);
    else
        printf(" dir = NULL\n");

    if (p->esq != NULL)
        exibe_preordem(p->esq);
    if (p->dir != NULL)
        exibe_preordem(p->dir);
}

void calcula_altura(Nodo *no)
{
    static int h;
    if (no == NULL)
        return;
    h++;
    calcula_altura(no->esq);
    calcula_altura(no->dir);
    h--;
    no->altura = h;
}

bool isBSTUtil(struct nodo *node, int min, int max)
{
    if (node == NULL)
    {
        return true;
    }
    if (node->info < min || node->info > max)
    {
        return false;
    }
    return (isBSTUtil(node->esq, min, node->info - 1) &&
            isBSTUtil(node->dir, node->info + 1, max));
}

bool verifica_ABB(struct nodo *root)
{
    return isBSTUtil(root, RANGE_MIN, RANGE_MAX);
}

Nodo *insere_por_nivel(struct nodo *root, int val)
{
    // create a new node with the given value
    struct nodo *novo_node = (struct nodo *)malloc(sizeof(struct nodo));
    novo_node->info = val;
    novo_node->esq = NULL;
    novo_node->dir = NULL;

    // if the root is NULL, the new node becomes the root
    if (root == NULL)
    {
        root = novo_node;
        return root;
    }

    // create a queue to perform the level order traversal
    struct nodo **queue = (struct nodo **)malloc(sizeof(struct nodo *) * 100);
    int front = -1;
    int tras = -1;

    // enqueue the root node
    queue[++tras] = root;

    // perform the level order traversal
    while (front != tras)
    {
        // dequeue a node from the queue
        struct nodo *current_node = queue[++front];

        // if the esq child of the current node is NULL, insert the new node as its esq child and return
        if (current_node->esq == NULL)
        {
            current_node->esq = novo_node;
            break;
        }

        // if the dir child of the current node is NULL, insert the new node as its dir child and return
        if (current_node->dir == NULL)
        {
            current_node->dir = novo_node;
            break;
        }

        // if both children of the current node exist, enqueue them into the queue
        queue[++tras] = current_node->esq;
        queue[++tras] = current_node->dir;
    }

    // free the queue memory
    free(queue);

    return root;
}

void exibe_posordem(Nodo *no)
{
    if (!no)
        return;
    exibe_posordem(no->esq);
    exibe_posordem(no->dir);
    printf("no = %p; chave = %d; altura = %d; esq = %p; dir = %p\n", no, no->info, no->altura, no->esq, no->dir);
}

int *gerar_vetor_aleatorio(void)
{
    int *vetor = (int *)malloc(10 * sizeof(int));
    int j, num_aleatorio;

    // Inicializa o gerador de números aleatórios
    srand(time(NULL));

    // Gera um número aleatório e verifica se já está no vetor
    for (int i = 0; i < 10; i++)
    {
        do
        {
            num_aleatorio = rand() % 20 + 1;
            // Verifica se o número já está no vetor
            for (j = 0; j < i; j++)
            {
                if (vetor[j] == num_aleatorio)
                {
                    break;
                }
            }
        } while (j < i); // Repete o loop até gerar um número novo

        vetor[i] = num_aleatorio;
    }

    return vetor;
}

int altura(Nodo *no)
{
    static int h = 0;
    if (no == NULL)
        return 0;
    int a = altura(no->esq);
    int b = altura(no->dir);
    if (a > b)
        return 1 + a;
    return 1 + b;
}

void troca_sub(Nodo *root)
{
    if (!root)
    {
        return;
    }
    Nodo *aux = root->esq;
    root->esq = root->dir;
    root->dir = aux;
    troca_sub(root->esq);
    troca_sub(root->dir);
    return;
}

int main()
{
    // a) Vetor de numeros aleatorios:
    int *vetor = gerar_vetor_aleatorio(); // vetor de números aleatorios entre 1 e 20

    printf("a) Vetor de numeros aleatorios:\n");
    for (size_t i = 0; i < 10; i++)
    {
        printf("%d ", vetor[i]);
    }
    printf("\n\n");
    // ***************************

    // b) Inserindo por nivel:
    Nodo *arvoreG = NULL;
    printf("b) Inserindo por nivel (arvoreBinariaGenerica):\n");

    int i;
    for (i = 0; i < 10; i++)
        arvoreG = insere_por_nivel(arvoreG, vetor[i]);
    exibe_preordem(arvoreG);
    //*********************************

    // c) Inserindo ABB:
    printf("\nc) Inserindo ABB (arvoreABB):\n");
    Nodo *arvoreABB = NULL;
    for (i = 0; i < 10; i++)
        arvoreABB = insere_binario(arvoreABB, vetor[i]);
    exibe_preordem(arvoreABB);
    //*********************************

    // d) Exibindo em pre-ordem:
    printf("\nd) Ja exibido em pre-ordem nos itens b & c\n");
    //*********************************

    // e) Verifica se é ABB:
    printf("\ne) Verifica se eh ABB:\n");
    printf("arvoreBinariaGenerica: ");
    if (verifica_ABB(arvoreG))
        printf("Eh ABB\n");
    else
        printf("Nao eh ABB\n");

    printf("arvoreABB: ");
    if (verifica_ABB(arvoreABB))
        printf("Eh ABB\n");
    else
        printf("Nao eh ABB\n");

    /*
    f) Imprime alturas das árvores
    */
    printf("\nf) A altura da arvore do item b) eh: %d\n", altura(arvoreG));
    printf("f) A altura da arvore do item c) eh: %d\n", altura(arvoreABB));

    // g) Troca de b) e c):
    printf("\ng) Troca de b):\n");
    troca_sub(arvoreG);
    exibe_preordem(arvoreG);
    printf("\ng) Troca de c):\n");
    troca_sub(arvoreABB);
    exibe_preordem(arvoreABB);
    return 0;
}