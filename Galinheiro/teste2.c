#include <stdio.h>
extern void foo(int a[], int n);

int main(void)
{
int a[5] = {3, 3, 0, 4, 0};
foo(a, 5);
for (int i = 0; i < 5; i++)
{
printf("%d\n", a[i]);
}
return 0;
}