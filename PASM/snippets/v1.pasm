!Felipe GM - MOD7 Computer Architecture Concordia Continuing Education
!Final assignment for the Winter Class 2023

#data
A 1
B 5
C 17
D 15
RES 0
#code
LDA T0 A
ADD T0 B
ADD T1 D
SUB T1 C
BBG T0 T1 here
STR RES T1
JMP done
here:
STR RES T0
done:
HLT

