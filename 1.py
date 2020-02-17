m = 0

def getFuel(f):
    fu = f // 3 - 2
    if fu > 0:
        return fu + getFuel(fu)
    else:
        return 0

with open("1.txt") as F:
    for line in F:
        m = m + getFuel(int(line))
        
print(m)
