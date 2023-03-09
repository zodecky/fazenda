// Created on Spyware Ipad.

#include <stdio.h>
#include <stdlib.h>

#define MAX_LENGTH 20

int main()
{
  printf("Input your name:\n");
  char *nome = (char *)malloc(MAX_LENGTH);
  char banana[MAX_LENGTH] = "banana";
  int scanf_result = scanf("%s", nome);
  if (scanf_result == 0)
  {
    printf("Error: not a string.\n");
    return 1;
  }
  printf("Your name is %s\n", nome);
  printf("banana = %s", banana);
  free(nome);
  return 0;
}
