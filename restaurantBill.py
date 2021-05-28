print("""
    ******************************
    Selamat Datang di Restaurant
        Selamat Menikmati
    ******************************
    >>>>>>>>>>>> MENU <<<<<<<<<<<<
    Makanan
    ==============================
    A1. Ayam Saus Tiram              : Rp 30.000
    B1. Ayam Goreng Mentega          : Rp 28.000
    C1. Ayam Goreng Crispy           : Rp 27.000
    D1. Ayam Lada Hitam              : Rp 30.000
    E1. Nasi Uduk                    : Rp 10.000 
    ==============================
    Minuman
    ==============================
    A2. Teh/Es       : Rp 3.000
    B2. Jeruk/Es     : Rp 4.000
    C2. Lemon Tea/Es : Rp 6.000
    D2. Susu/Es      : Rp 8.000
    E2. Kopi         : Rp 10.000
    ==============================
    """)

pelanggan = str(input("Nama Pelanggan ="))
nomormeja = int(input("Meja Nomor ="))

total1 = 0
menu1 = ""
jumlahpesan = 0
buah = 0
diskon = ""
ppn = 0

def makanan():
    global total1
    global jumlahpesan
    global menu1
    global diskon
    global ppn
    print("\nMakanan")
    pesan = str(input("Masukkan Kode Menu ="))
    jumlahpesan = int(input("Jumlah Pesanan ="))
    if pesan == "A1":
        menu1 = "Ayam Saus Tiram"
        harga = (30000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn)
        else:
            diskon = (0)
            total1 = int(harga + ppn)
    elif pesan == "B1":
        menu1 = "Ayam Goreng Mentega"
        harga = (28000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn)
        else:
            diskon = (0)
            total1 = int(harga + ppn)
    elif pesan == "C1":
        menu1 = "Ayam Goreng Crispy"
        harga = int(27000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        total1 = int(harga + ppn)
    elif pesan == "D1":
        menu1 = "Ayam Lada Hitam"
        harga = int(30000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        total1 = int(harga + ppn)
    elif pesan == "E1":
        menu1 = "Nasi Uduk"
        harga = int(10000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        total1 = int(harga + ppn)
    else:
        print("Menu tidak terdaftar, silahkan ulangi kembali")
        makanan()

makanan()

total2 = 0
menu2 = ""
jumlah = 0

def minuman():
    global total2
    global menu2
    global jumlah
    global diskon
    global ppn
    print("\nMinuman")
    pesan = str(input("Masukkan Kode Menu ="))
    jumlah = int(input("Jumlah Pesanan ="))

    if pesan == "A2":
        menu2 = "Teh/Es"
        harga = (3000 * jumlah)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 10:
            diskon = int(harga * 0.2)
            total2 = int(harga - diskon + ppn)
        else:
            diskon = (0)
            total2 = int(harga + ppn)
    elif pesan == "B2":
        menu2 = "Jeruk/Es"
        harga = int(4000 * jumlah)
        ppn = int(harga * 0.1)
        diskon = 0
        total2 = int(harga + ppn)
    elif pesan == "C2":
        menu2 = "Lemon Tea/Es"
        harga = int(6000 * jumlah)
        ppn = int(harga * 0.1)
        diskon = 0
        total2 = int(harga + ppn)
    elif pesan == "D2":
        menu2 = "Susu/Es"
        harga = int(8000 * jumlah)
        ppn = int(harga * 0.1)
        diskon = 0
        total2 = int(harga + ppn)
    elif pesan == "E2":
        menu2 = "Kopi"
        harga = int(10000 * jumlah)
        ppn = int(harga * 0.1)
        diskon = 0
        total2 = int(harga + ppn)
    else:
        print("Menu tidak terdaftar, silahkan ulangi kembali")
        minuman()
minuman()

totalharga = total1+total2

print("--------------------------")
print("Pesanan")
print("--------------------------")
print("Menu :", menu1, "||", menu2)
print("Jumlah :",jumlahpesan, "porsi", "||", jumlah, "buah")
print("Harga :", total1, "+", total2)
print("Diskon :", diskon)
print("PPN :", ppn)
print("--------------------------")
print("Total :", totalharga)
print("--------------------------")
print(input("Apakah"))
print(input("Apakah pesanan Anda sudah sesuai? Silahkan periksa kembali (y/n) ="))

print("\nTotal harus Dibayar: ", totalharga)
metode_pembayaran = str(input("Melakukan pembayaran melalui (Cash/Kredit/Ovo/Go-Pay) = "))
   if metode_pembayaran == 'Cash':
      print("masukan nominal uang")
   elif metode_pembayaran == 'Kredit':
      print("Silahlan melakukan pembayaran ke Rekening 98023813 BCA")
   elif metode_pembayaran == 'Ovo/Go-Pay':
      print("silahkan melakukan pembayaran ke no Ovo / Go - Pay = 0875142378927")
   else:
      print("maaf metode pembayaran tidak tersedia")
bayar = int(input("Pelanggan membayar sebesar :"))
kembalian = int(bayar - totalharga)
print("Kembalian :", kembalian)

print("\n=============================================================")
print("                           STRUK                             ")
print("=============================================================")
print(" Nama                :", pelanggan)
print(" Meja                :", nomormeja)
print(" Pesanan             :" ,jumlahpesan, menu1, "dan", jumlah, menu2, "-", totalharga)
print(" Total               : Rp.", totalharga)
print(" Metode Pembayaran   :", metode_pembayaran)
print(" Nominal Bayar       : Rp.", bayar)
print(" Kembalian           : Rp.", kembalian)
print("==============================================================")
print("                        TERIMA KASIH                          ")
print("==============================================================")
