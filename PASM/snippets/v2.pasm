!Felipe GM - MOD7 Computer Architecture Concordia Continuing Education
!Final assignment for the Winter Class 2023

#data
A 0
B 1
C 2
D 3
E 4
S 0
T 50
#code
LDA T2 0
loopHere:
LDA T0 S
ADD T0 A
ADD T0 B
ADD T0 C
ADD T0 D
ADD T0 E
STR S T0
LDA T1 T 
INC T2
BSM T0 T1 loopHere
HLT

