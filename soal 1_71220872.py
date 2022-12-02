


def hk():
    kalimat = input("Masukkan sebuah kalimat/kata : ")
    kata = input("Masukkan kata yang ingin dihitung : ")
    b = kalimat.split()
    a = b.count(kata)
    print("Terdapat sebanyak "+str(a)+" kata "+str(kata)+" di dalam kalimat")
    return kalimat
def uk():
    kalimat = input("Masukkan sebuah kalimat/kata : ")
    kata = input("Masukkan kata yang ingin di ubah : ")
    pengganti = input("Masukkan kata pengganti : ")
    jawab = kalimat.replace(kata, pengganti)
    print("String berhasil diubah menjadi : "+str(jawab))
    return kalimat

print("""====== Program Manipulasi String ======
Pilihan Menu :
1. Hitung Kata
2. Ubah Kata""")
coblos = int(input("Pilihan anda : "))
if coblos == 1:
    hk()
elif coblos == 2:
    uk()
else:
    input("Masukkan sebuah kalimat/kata : ")
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")