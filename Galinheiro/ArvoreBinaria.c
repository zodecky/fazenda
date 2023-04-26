#include <stdio.h>
#include <stdlib.h>

typedef struct noodle
{
    int info;
    struct noodle *left;
    struct noodle *right;
} Noodle;

Noodle *create_noodle(int info)
{
    Noodle *noodle = (Noodle *)malloc(sizeof(Noodle));
    noodle->info = info;
    noodle->left = NULL;
    noodle->right = NULL;
    return noodle;
}

void insert_noodle(Noodle **root, int info)
{
    if (*root == NULL)
    {
        *root = create_noodle(info);
    }
    // else
    {
        if (info < (*root)->info)
        {
            insert_noodle(&(*root)->left, info);
        }
        else
        {
            insert_noodle(&(*root)->right, info);
        }
    }
}

void print_pre_order(Noodle *root)
{
    if (root != NULL)
    {
        printf("%d ", root->info);
        print_pre_order(root->left);
        print_pre_order(root->right);
    }
}


printf()
void print_in_order(Noodle *root)
{
    if (root != NULL)
    {
        print_in_order(root->left);
        printf("%d ", root->info);
        print_in_order(root->right);
    }
}

void print_post_order(Noodle *root)
{
    if (root != NULL)
    {
        print_post_order(root->left);
        print_post_order(root->right);
        printf("%d ", root->info);
    }
}

void print_beautiful(Noodle *root, int level)
{
    if (root != NULL)
    {
        print_beautiful(root->right, level + 1);
        for (int i = 0; i < level; i++)
        {
            printf("   ");
        }
        printf("%d \n", root->info);
        print_beautiful(root->left, level + 1);
    }
}

int main()
{
    Noodle *root = NULL;
    insert_noodle(&root, 5);
    insert_noodle(&root, 3);
    insert_noodle(&root, 7);
    insert_noodle(&root, 2);
    insert_noodle(&root, 4);
    insert_noodle(&root, 6);
    insert_noodle(&root, 8);
    print_pre_order(root);
    printf(" <- Pre Order (raiz, esquerda, direita) \n");
    print_in_order(root);
    printf(" <- In Order (esquerda, raiz, direita) \n");
    print_post_order(root);
    printf(" <- Post Order (esquerda, direita, raiz) \n");
    print_beautiful(root, 0);
    return 0;
}