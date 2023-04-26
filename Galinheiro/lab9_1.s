.data
    sf: .string "%d\n"

.text
.globl main

main:
    pushq   %rbp

    movl $1, %edi
    movl $2, %esi
    movl $3, %edx
    call    add

    movq    $sf,  %rdi
    movl    %eax, %esi
    xorl    %eax, %eax /*zera eax printf*/
    call    printf

    popq    %rbp
    ret
    