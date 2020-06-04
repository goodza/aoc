

# NN = 101741582076661
# NN = 10000
# N = 119315717514047
# N = 119500000
# N = 11930
N = 2193
NROW = 2


#GENERATE
i = 0
c = []


c = list(range(0,N))
print(c[2020])


def incr(a,C):
    CC = []
    for i in range(0,N):
        p = i
        while p % a != 0:
            p += N
        CC.append(C[p//a])
    return CC[:]

    # i = 0
    # j = 0
    # while i<N+1:
    #     while j<N+1:
    #         cc[j] = C[i]
    #         i+=1
    #         j+=I
    #     j = j - N - 1

def cut(a,C,f):
    if f:
        C = C[a:len(C)]+C[0:a]
    else:
        C = C[N-a:len(C)]+C[0:N-a]
    return C


cont = []
with open("22.txt") as F:
    cont = F.readlines()



k = 1

while k<=NROW:

    for j in range(0,len(cont)):
        # print(cont[j])
        if 'deal with increment' in cont[j]:
            print('inc:'+cont[j][20:len(cont[j])])
            c = incr(int(cont[j][20:len(cont[j])]),c)
            # print(c)

        if 'deal into new stack' in cont[j]:
            print('new')
            c.reverse()
            # print(c)

        if 'cut -' in cont[j]:
            print('cut-:'+cont[j][5:len(cont[j])])
            c = cut(int(cont[j][5:len(cont[j])]),c,False)
            # print(c)

        elif 'cut' in cont[j]:
            print('cut+:'+cont[j][4:len(cont[j])])
            c = cut(int(cont[j][4:len(cont[j])]),c,True)
            # print(c)
        print(j)
    # # if c[3] == 4117:
    #     if c[1020] in out:
    #         print('BINGO:'+c[1020])
    #         k = NN
    #     else:
    #         out.append(c[1020])
    k+=1

print(c[2])