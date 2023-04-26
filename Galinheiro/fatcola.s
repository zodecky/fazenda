	.file	"roubo.c"
	.text
	.globl	fat
	.type	fat, @function
fat:
.LFB0:
	pushq	%rbp
	movq	%rsp, %rbp

	subq	$16, %rsp

	movl	%edi, -4(%rbp)
	cmpl	$0, -4(%rbp)
	jne	recursion
	movl	$1, %eax
	jmp	return
recursion:
	movl	-4(%rbp), %eax
	subl	$1, %eax
	movl	%eax, %edi
	call	fat
	imull	-4(%rbp), %eax
return:
	leave
	ret

.LFE0:
	.size	fat, .-fat
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
