import os


def penjumlahan(A, B):
    return A+B


def pengurangan(A, B):
    return A-B


def perkalian(A, B):
    return A*B


def pembagian(A, B):
    return A/B


def menu():
    print("=== Aplikasi Kalkulator Sederhana ===")
    print("Pilih Jenis Operasi di bawah:")
    print("1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n0.Exit")

    inputan = int(input("input nomor operasi : "))
    os.system("cls")  # windows

    if inputan == 1:
        print("===Sub Program Penjumlahan===")
        bil1 = int(input("masukkan bilangan pertama : "))
        bil2 = int(input("masukkan bilangan kedua   : "))
        print(f"{bil1} + {bil2} = {penjumlahan(bil1, bil2)}")
    elif inputan == 2:
        print("===Sub Program Pengurangan===")
        bil1 = int(input("masukkan bilangan pertama : "))
        bil2 = int(input("masukkan bilangan kedua   : "))
        print(f"{bil1} - {bil2} = {pengurangan(bil1, bil2)}")
    elif inputan == 3:
        print("===Sub Program Perkalian===")
        bil1 = int(input("masukkan bilangan pertama : "))
        bil2 = int(input("masukkan bilangan kedua   : "))
        print(f"{bil1} - {bil2} = {perkalian(bil1, bil2)}")
    elif inputan == 4:
        print("===Sub Program Pembagian===")
        bil1 = int(input("masukkan bilangan pertama : "))
        bil2 = int(input("masukkan bilangan kedua   : "))
        print(f"{bil1} - {bil2} = {pembagian(bil1, bil2)}")
    elif inputan == 0:
        print("program kalkulator diakhiri")
        exit()
    else:
        print("inputan anda tidak tercalidasi")


# memanggil dan fungsi perulangan
if __name__ == '__main__':
    while True:
        menu()
