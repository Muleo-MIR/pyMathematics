
#Euclidian algorithm

inputA,inputB = map(int,input('Input A,B: ').split())
A = inputA
B = inputB

while B != 0:
    if A > B:
        A -= B
    else:
        B -= A 

print(f'GCF({inputA},{inputB} = {A}')            