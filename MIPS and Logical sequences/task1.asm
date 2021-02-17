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
	
		
	la $a0,a  # loading the address from a
	addi $v0,$0,4 #it means printing string
	syscall
	
	addi $v0,$0,5 #inputing integer
	syscall
	move $t0, $v0 #moving the value of v0 into t0
	
	lw $t1, year #load value of year into t1

Loop:	
	blt $t0,$t1,printstr1  # if year less than 1581
	                      # check 
	lw   $t3, c #c=t3
	div $t0,$t3 # $t0/$t3
	mfhi $t6  #t6=$t0/$t3
	beq $t6,$0,Loop3 # if $t6=0 then goto Loop3 or else to Loop4
	j Loop4
Loop3:
	
	
	lw   $t5, d #d=$t5
	
	div $t0,$t5 #$t0/$t5
	mfhi $a1    # $a1=$t0/$t5	
	
	bne $a1,$0,printstr2  # if $a1=0 then goto printstr2 or else continue
	
		
Loop4:
	
	lw   $t7,e  #e=$t7
	
	div  $t0,$t7 #$t0/$t7
	mfhi $a2     #$a2=$t0/$t7
	
	beq $a2,$0,printstr2 #if $a2=0 goto printstr2 or else goto printstr3
	j printstr3
	
	

	
printstr1:
	addi $v0,$0,4 
	la   $a0,str1 # $a0=str1
	syscall
	j EndLoop # goto EndLoop
	
printstr2:
	addi $v0,$0,4
	la   $a0,str2
	syscall
	j EndLoop # goto EndLoop

printstr3:
	addi $v0,$0,4
	la   $a0,str3
	syscall
	j EndLoop #goto EndLoop
 
	
	
	
EndLoop:
	addi	$v0, $0, 10	# exit
	syscall
	
	
