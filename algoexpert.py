def isValidSubsequence(array, sequence):
    c=[]
    cont=0
    if sequence == array:
        return True
    for i in array:
        if c==sequence:
            return True
        elif i==sequence[cont]:
            c.append(i)
            cont+=1
    if c==sequence:
        return True
    else:
        return False
array=[5, 1, 22, 25, 6, -1, 8, 10]
sequence=[1, 6, -1, 10]
print(isValidSubsequence(array,sequence))