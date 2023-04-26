#include <stdio.h>
#include <stdlib.h>

int *inverte_vetor(int *vetor, int tamanho)
{
    int *vetor_invertido = (int *)malloc(tamanho * sizeof(int));
    for (int i = 0; i < tamanho; i++)
    {
        vetor_invertido[i] = vetor[tamanho - i - 1];
    }
    return vetor_invertido;
}

int main(void)
{
    printf("teste\n\n");

    int vetor_original[5] = {1, 2, 3, 4, 5};
    int tamanho = sizeof(vetor_original) / sizeof(int);

    printf("Vetor original: ");
    for (int i = 0; i < tamanho; i++)
    {
        printf("%d ", vetor_original[i]);
    }
    printf("\n");

    int *vetor_invertido = inverte_vetor(vetor_original, tamanho);
    for (int i = 0; i < tamanho; i++)
    {
        printf("%d ", vetor_invertido[i]);
    }
    printf("\n");

    return 0;
}