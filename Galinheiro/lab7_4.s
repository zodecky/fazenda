
.data
Sf: .string "soma = %d\n"
nums: .int 65, -105, 111, 34

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

    movl    $0, %r12d  /* r12 = 0; zera para iniciar o loop*/
    movl    $0, %r13d  /* r13 = 0; zera para guardar da soma*/
    movq    $nums, %r10

LOOP_1:
    cmpl    $4, %r12d  /* r12 == 4 ? */
    jge      PRINT     /* se sim, pula para FIM_1 */
    movl    %r12d, %r11d
    imull   $4, %r11d
    addq    %r10, %r11
    addq    (%r11), %r13
    addl    $1, %r12d  /* r12 += 1 */
    
    jmp     LOOP_1

PRINT:

    /*************************************************************/
    /* este trecho imprime o \n (estraga %eax)                  */
    movq    $Sf, %rdi    /* primeiro parametro (ponteiro)*/
    movl    %r13d, %esi   /* segundo parametro  (inteiro) */
    movl    $0, %eax       
    call    printf       /* chama a funcao da biblioteca */
    /*************************************************************/

    /***************************************************************/
    /* mantenha este trecho aqui e nao mexa - finalizacao!!!!      */
    movq  $0, %rax  /* rax = 0  (valor de retorno) */
    movq    -16(%rbp), %r12 /* recupera r12 */
    movq    -8(%rbp), %rbx  /* recupera rbx */
    leave
    ret
    /***************************************************************/
