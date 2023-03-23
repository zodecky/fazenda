#include <stdio.h>

void dump(void *p, int n)
{
  unsigned char *p1 = p;
  while (n--)
  {
    printf("%p - %02x\n", p1, *p1);
    p1++;
  }
}

int main(void)
{
  char c = 150; // 10010110
  short s = -3; // 1111111111111101
  int i = -151; // 11111111111111111111111110010101
  printf("dump de c: \n");
  dump(&c, sizeof(c));
  printf("dump de s: \n");
  dump(&s, sizeof(s));
  printf("dump de i: \n");
  dump(&i, sizeof(i));
  return 0;
}