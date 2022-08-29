print("Pilih Opsi Operasi: ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    pilihan = str(input("Masukkan pilihan: "))
    bil1 = eval(input("Masukkan bilangan pertama: "))
    bil2 = eval(input("Masukkan bilangan kedua: "))

    if pilihan == "1":
        jumlah = bil1 + bil2
        print(bil1, "+", bil2, "=", jumlah)

    elif pilihan == "2":
        kurang = bil1 - bil2
        print(bil1, "-", bil2, "=", kurang)

    elif pilihan == "3":
        kali = bil1 * bil2
        print(bil1, "x",bil2, "=", kali)

    elif pilihan == "4":
        bagi = bil1 / bil2
        print(bil1, "/", bil2, "=", bagi)
    
    a = input("Apakah anda ingin keluar? jika ya Ketik Q jika tidak ketik apa saja:")
    if a == "Q" :
        break





    

