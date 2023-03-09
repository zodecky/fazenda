section .data
    message: db "Hello, World!", 0

section .text
    global main
    extern printf

main:
    push message
    call printf
    add rsp, 8

    xor eax, eax
    ret