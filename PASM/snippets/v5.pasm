!Felipe GM - MOD7 Computer Architecture Concordia Continuing Education
!Final assignment for the Winter Class 2023

#data
ValueA 15
ValueB 15
RES 0
#code
start:
LDA T0 ValueA
LDA T1 ValueB
BEQ T0 T1 equal
ADD T0 T1
JMP done
equal:
PUSH T0
ADD T0 ValueB
POP T2
DIV T2 T0
STR ValueA T2
STR ValueB T0
JMP start
done:
INC T0
DEC T1
MOD T1 T0
STR RES T1
HLT