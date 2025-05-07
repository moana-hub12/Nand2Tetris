// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

@R1
D=M
@n
M=D  // setting value of R1 to n

@i
M=1

@R0
D=M
@NR0 // to preserve the initial value of RO
M=D

(LOOP)
@i
D=M
@n
D=D-M
@STOP
D;JEQ  // if i>n goto stop

@R0
D=M
@NR0
D=D+M
@NR0
M=D
@i
M=M+1

@LOOP
0;JMP

(STOP)
@NR0
D=M
@R2
M=D

(END)
@END
0;JMP