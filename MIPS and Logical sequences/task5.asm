	
.data
	
a:	.asciiz "Enter the year: "
year:   .word 1581
c:	.word 4
d:	.word 100
e:	.word 400


str1:	.asciiz "Enter number greater than 1581"
str2:	.asciiz "Is a leap year"
str3:	.asciiz "Is not a leap year"	
	.text
	
		
	la $a0,a
	addi $v0,$0,4
	syscall
	
	addi $v0,$0,5
	syscall
	move $t0, $v0
	
	lw $t1, year

Loop:	
	blt $t0,$t1,printstr1  # if year lt 1581
	                      # check 
	lw   $t3, c
	div $t0,$t3
	mfhi $t6
	beq $t6,$0,Loop3
	j Loop4
Loop3:
	
	
	lw   $t5, d
	
	div $t0,$t5
	mfhi $a1
	
	bne $a1,$0,printstr2
	
		
Loop4:
	
	lw   $t7,e
	
	div  $t0,$t7
	mfhi $a2
	
	beq $a2,$0,printstr2
	j printstr3
	
	

	
printstr1:
	addi $v0,$0,4
	la   $a0,str1
	syscall
	j EndLoop
	
printstr2:
	addi $v0,$0,4
	la   $a0,str2
	syscall
	j EndLoop

printstr3:
	addi $v0,$0,4
	la   $a0,str3
	syscall
	j EndLoop
 
	
	
	
EndLoop:
	addi	$v0, $0, 10	# exit
	syscall
	
	

main:
 # 1* 4 = 4 bytes local
 addi $fp, $sp, 0
 addi $sp, $sp, -4
# Initialize locals
 sw $0, 0($fp)
 
 addi $v0, $0, 5
 syscall
 sw $v0, -4($fp) # base
 addi $v0, $0, 5
 syscall
 sw $v0, 0($fp) 
	
	
# push 1* 4 = 4 bytes
# of arguments
addi $sp, $sp, 0
# arg = base
lw $t0, -8($fp) # base
sw $t0, 0($sp) # arg 1
jr $ra


	
			
jal function

function: 
	addi $sp, $sp,-8
 	sw $ra, 0($sp)
 	sw $fp, 4($sp)
 	
 	addi $fp, $sp, 0
 	
 	# Allocate local variables
	# 1 * 4 = 4 bytes.
	addi $sp, $sp, -4
	# Initialize locals.
	addi $t0, $0, 1
	sw $t0, -4($fp) # result

	
