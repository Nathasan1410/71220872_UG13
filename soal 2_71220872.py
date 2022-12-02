

def cetakHuruf(a,b):
    if (b % 2) == 0:
        a = (str(a)[0:3])+(str(a)[b-3:b+1])
    else:
        a = (str(a)[((b-1)//2)-1:((b-1)//2)+2])
    return a 
a = input("Masukkan kata : ")
b = len(a)
c = cetakHuruf(a,b)
print(c)