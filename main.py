import sys
import math

# Auto-generated code below aims at helping you parse the standard input according to the problem statement.

list = []
b = input()
for i in range(len(str(b))): 
    if b[i] == '0':
        list.append('1')
    elif b[i] == '1':
        list.append('0')
total = "".join(list)
print(total)