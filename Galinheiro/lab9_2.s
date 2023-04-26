.text
.globl fat
fat:
    pushq   %rbp
    movq    %rsp, %rbp
    subq    $16, %rsp
    movl    %edi, -4(%rbp)

    cmpl    $0, %edi
    jne     recursion
    movl    $1, %eax
    jmp     return

recursion:
    subl    $1, %edi
    call    fat
    imull   -4(%rbp), %eax # n * return fat

return:
    leave
    ret

    