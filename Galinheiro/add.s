.text
.globl add

add:
    pushq   %rbp
    
    movl %edi, %eax
    addl %esi, %eax
    addl %edx, %eax
    /*return eax (nao faz nada com ele)*/
    

    popq    %rbp
    ret
    