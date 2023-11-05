valores = [0,1,2,3,4,5,6,7,8,9]
def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
dobrar(valores)
print(valores)