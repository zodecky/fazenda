.text
.globl fat
fat:
    pushq   %rbp
    movq    %rsp, %rbp

    cmpl    $0, %edi
    jne     recursion
    movl    $1, %eax
    jmp     return

recursion:
    movl    %edi, %edx
    decl    %edi
    call    fat
    imull   %edx, %eax # n * return fat

return:
    leave
    ret

    