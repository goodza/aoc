"""
 A   B   C
src aux dest
"""

def move(h,src,aux,dest):
    if h >= 1:
        #from src to aux using dest
        move(h-1,src,dest,aux)
        
        #move last h disk from src to dest
        print(f'move from {src} to {dest}')
        
        #from aux to dest using src
        move(h-1,aux,src,dest)


move(1,'A','B','C')
