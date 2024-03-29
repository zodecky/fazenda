/*void foo (int a[], int n) {
int i;
int s = 0;
for (i=0; i < n; i++)
s += a[i];
if (a[i] == 0) {
a[i] = s;
s = 0;
}
}
}*/

.text
.globl foo

foo:
/* a = %rdi
; n = %esi
; aux = %r10
; a + i * sizeof(int) */
pushq %rbp
movq %rsp, %rbp
xorl %r10d, %r10d /* aux = 0*/
xorl %ecx, %ecx /* int i = 0 */
xorl %edx, %edx /* int s = 0 */

forloop:
cmpl %esi, %ecx /* if i < n */
jge return

movl %ecx, %r10d /* ecx i para prox iteração, r10 atual */
imulq $4, %r10 /* i * sizeof(int) */
addq %rdi, %r10 /* a + i*sizeof(int) */

addl (%r10), %edx /* s += a[i] */

cmpl $0, (%r10) /*cmp 0 a[i] if a[i] == 0*/
jne endloop /*if equals segue*/
movl %edx, (%r10)
xorl %edx, %edx
endloop:
incl %ecx
jmp forloop
return:
leave
ret
