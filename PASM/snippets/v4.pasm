!Felipe GM - MOD7 Computer Architecture Concordia Continuing Education
!Final assignment for the Winter Class 2023

#data
A 0
B 1
RES 0
#code
LDA T3 10
LDA T2 2
stackLoop:
MOD T3 T2
PUSH T3
BNE T3 0 stackLoop
POP T2
LDA T0 A
LDA T1 B
OR T0 T1
AND T0 T1
NOT T0
INC T0
DIV T0 T1
MUL T0 10
ADD T0 T1
SUB T0 2
STR RES T0
done:
HLT

