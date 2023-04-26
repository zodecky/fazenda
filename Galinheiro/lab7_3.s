.data
Sf:  .string "%d\n"    /* string de formato para printf */

.text
.globl  main
main:

/********************************************************/
/* mantenha este trecho aqui e nao mexa - prologo !!!   */
  pushq   %rbp
  movq    %rsp, %rbp
  subq    $16, %rsp
  movq    %rbx, -8(%rbp)  /* guarda rbx */
  movq    %r12, -16(%rbp)  /* guarda r12 */
/********************************************************/

movl $1, %r12d

LOOP:
cmpl $10, %r12d
jg SKIP_LOOP

movl %r12d, %r13d
imull %r13d, %r13d

/*************************************************************/
/* este trecho imprime o \n (estraga %eax)                  */
  movq    $Sf, %rdi    /* primeiro parametro (ponteiro)*/
  movl    %r13d, %esi   /* segundo parametro  (inteiro) */
  movl  $0, %eax  
  call  printf       /* chama a funcao da biblioteca */
/*************************************************************/

addl $1, %r12d

jmp LOOP
SKIP_LOOP:
/***************************************************************/
/* mantenha este trecho aqui e nao mexa - finalizacao!!!!      */
  movq  $0, %rax  /* rax = 0  (valor de retorno) */
  movq    -16(%rbp), %r12 /* recupera r12 */
  movq    -8(%rbp), %rbx  /* recupera rbx */
  leave
  ret      
/***************************************************************/