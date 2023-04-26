 .data
  nums: .int 3, -5, 7, 8, -2
  s1:   .string "%d\n"
  /*gcc lab8_2.s lab8_2_filtro.c -o main -no-pie -Wall*/

  .text
  .globl main
  main:
  /* prologo */
  /*necessario checar se´é calle saved
  se é eu salvo no inicio do programa
  se nao é eu guardo no RA antes da chamada da função

  nesse caso seria neces´ário recalcular a área, ja que nao usei
  o rbx  
  */
     pushq %rbp
     movq  %rsp, %rbp
     subq  $32, %rsp
     movq  %rbx, -8(%rbp) /*nao precisa pois usei r11*/
     movq  %r12, -16(%rbp)

    movl $0, %r12d
    movq $nums, %r11 /* *p */

loop1:
    cmpl $5, %r12d
    jge fim

    movl (%r11), %edi
    movl $1, %esi
    movq %r11, -24(%rbp)
    call filtro

    movq $s1, %rdi
    movl %eax, %esi
    movl $0, %eax
    call printf

    movq -24(%rbp), %r11

    incq %r11
    incl %r12d
    jmp loop1

fim:

  /* finalizacao */
     movq -8(%rbp), %rbx /*nao precisa pois usei r11*/
     movq -16(%rbp), %r12
     leave
     ret
