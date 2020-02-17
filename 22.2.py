from os import system


def deinc(a,p,n):
    # m = -1
    while (p % a) != 0:
        # m = p % a
        p = p + n
    return int(p / a)

def deminuscut(a,p,n):
    return (p - a + n) % n

def depluscut(a,p,n):
    return (p + a) % n

def denew(p,n):
    return n - p - 1


def reverse_deal(p):
    return N-1-p
    
def reverse_cut(p, a):
    return (i+a+N) % N



def reverse_increment(p, a):
    return pow(a,-1,N) * p % N


#REVERSE LIST
cont = []
with open("22.0.txt") as F:
    cont = F.readlines()

cont.reverse()
#REVERSE LIST

N = 10
NROW = 1
p = 0 #LAST POS

j=1
k=0

OUTROW = []

while j<=NROW:
    for i in range(0,len(cont)):
        # print(p)
        if 'deal with increment' in cont[i]:
            # p = deinc(int(cont[i][20:len(cont[i])]),p,N)
            p = reverse_increment(p,int(cont[i][20:len(cont[i])]))

        if 'deal into new stack' in cont[i]:
            # print('new')
            # p = denew(p,N)
            p = reverse_deal(p)
        if 'cut' in cont[i]:
            p = reverse_cut(p,int(cont[i][4:len(cont[i])]))
        # if 'cut -' in cont[i]:
        #     # print('cut-:'+cont[i][5:len(cont[i])])
        #     p = deminuscut(int(cont[i][5:len(cont[i])]),p,N)

        # elif 'cut' in cont[i]:
        #     # print('cut+:'+cont[i][4:len(cont[i])])
        #     p = depluscut(int(cont[i][4:len(cont[i])]),p,N)

    # if p==3471206487120:
    #     print('Bingo!'+str(j))
    j+=1

# p = 2020
# Z = 924832060185
# Y = 3471206487120
# B = (Z - pow(Y,2) / p)/(1-Y/p)
# print(B)
# p = 3471206487120
# while p % 924832060185 !=0:
#     p += N
#     print(p)
#     system('clear')

print(str(p)) 
