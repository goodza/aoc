
import os

with open('2.txt', "r+") as file:
    s = file.read()           # reads a string from a file

opp = list(map(int, s.split(',')))

opp[1]=12
opp[2]=2

# print(len(opp),os.linesep)

noun = 0
verb = 0
op = opp.copy()
O = 0


while noun < 100 and op[0] != 19690720:

    verb = 0
    while verb < 100 and op[0] != 19690720:
        op = opp.copy()
        op [1] = noun
        op [2] = verb
        i=0
        while op[i] != 99 and i+4 <= len(op):
            if op[0] == 19690720:
                print(noun)
            if op[i] == 1 or op[i] == 2:
                if op[i+1] < len(op) and op[i+2] < len(op) and op[i+3] < len(op):
                    if op[i] == 1:
                        op[op[i+3]] = op[op[i+1]] + op[op[i+2]]
                    if op[i] == 2:
                        op[op[i+3]] = op[op[i+1]] * op[op[i+2]]
                i+=4
            else:
                i+=1
        # print(op[0])
        verb+=1
    noun+=1


print(verb)
print(noun)
# print(i)
print(op[0])
print(op)