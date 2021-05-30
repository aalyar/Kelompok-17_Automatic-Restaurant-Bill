print("""
    ******************************
    Selamat Datang di Restaurant
        Selamat Menikmati
    ******************************
    >>>>>>>>>>>> MENU <<<<<<<<<<<<
    Makanan
    ==============================
    a1. Ayam Saus Tiram              : Rp 30.000
    b1. Ayam Goreng Mentega          : Rp 28.000
    c1. Ayam Goreng Crispy           : Rp 27.000
    d1. Ayam Lada Hitam              : Rp 30.000
    e1. Nasi Uduk                    : Rp 10.000 
    ==============================
    Minuman
    ==============================
    a2. Teh/Es       : Rp 3.000
    b2. Jeruk/Es     : Rp 4.000
    c2. Lemon Tea/Es : Rp 6.000
    d2. Susu/Es      : Rp 8.000
    e2. Kopi         : Rp 10.000
    ==============================
    """)

pelanggan = str(input("Nama Pelanggan ="))
nomormeja = int(input("Meja Nomor ="))

total1 = 0
menu1 = ""
jumlahpesan1 = 0
buah = 0
diskon = ""
ppn = 0


def makanan():
    global total1
    global jumlahpesan1
    global menu1
    global diskon
    global ppn
    print("\nMakanan")
    pesan = str(input("Masukkan Kode Menu ="))
    jumlahpesan1 = int(input("Jumlah Pesanan ="))
    if pesan == "a1":
        menu1 = "Ayam Saus Tiram"
        harga = (30000 * jumlahpesan1)
        ppn = int(harga * 0.1)
        if jumlahpesan1 >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn)
        else:
            total1 = int(harga + ppn)
    elif pesan == "b1":
        menu1 = "Ayam Goreng Mentega"
        harga = (28000 * jumlahpesan1)
        ppn = int(harga * 0.1)
        if jumlahpesan1 >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn)
        else:
            total1 = int(harga + ppn)
    elif pesan == "c1":
        menu1 = "Ayam Goreng Crispy"
        harga = int(27000 * jumlahpesan1)
        ppn = int(harga * 0.1)
        if jumlahpesan1 >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn)
        else:
            total1 = int(harga + ppn)
    elif pesan == "d1":
        menu1 = "Ayam Lada Hitam"
        harga = int(30000 * jumlahpesan1)
        ppn = int(harga * 0.1)
        if jumlahpesan1 >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn)
        else:
            total1 = int(harga + ppn)
    elif pesan == "e1":
        menu1 = "Nasi Uduk"
        harga = int(10000 * jumlahpesan1)
        ppn = int(harga * 0.1)
        if jumlahpesan1 >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn)
        else:
            total1 = int(harga + ppn)
    else:
        print("Menu tidak terdaftar, silahkan ulangi kembali")
        makanan()
makanan()

total2 = 0
menu2 = ""
jumlah1 = 0

def minuman():
    global total2
    global menu2
    global jumlah1
    global diskon
    global ppn
    print("\nMinuman")
    pesan = str(input("Masukkan Kode Menu ="))
    jumlah1 = int(input("Jumlah Pesanan ="))

    if pesan == "a2":
        menu2 = "Teh/Es"
        harga = (3000 * jumlah1)
        ppn = int(harga * 0.1)
        diskon = (0)
        total2 = int(harga + ppn)
    elif pesan == "b2":
        menu2 = "Jeruk/Es"
        harga = int(4000 * jumlah1)
        ppn = int(harga * 0.1)
        diskon = 0
        total2 = int(harga + ppn)
    elif pesan == "c2":
        menu2 = "Lemon Tea/Es"
        harga = int(6000 * jumlah1)
        ppn = int(harga * 0.1)
        diskon = 0
        total2 = int(harga + ppn)
    elif pesan == "d2":
        menu2 = "Susu/Es"
        harga = int(8000 * jumlah1)
        ppn = int(harga * 0.1)
        diskon = 0
        total2 = int(harga + ppn)
    elif pesan == "e2":
        menu2 = "Kopi"
        harga = int(10000 * jumlah1)
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
print("Jumlah :",jumlahpesan1, "porsi", "||", jumlah1, "buah")
print("Harga :", total1, "+", total2)
print("Diskon :", diskon)
print("PPN :", ppn)
print("--------------------------")
print("Total :", totalharga)
print("--------------------------")

pesanlagi = str(input("Apakah Anda ingin memesan lagi (y/n) = "))
if pesanlagi == "y":
    print("Masukkan kembali pesanan Anda =  """"
            >>>>>>>>>>>> MENU <<<<<<<<<<<<
            Makanan
            ==============================
            a1. Ayam Saus Tiram              : Rp 30.000
            b1. Ayam Goreng Mentega          : Rp 28.000
            c1. Ayam Goreng Crispy           : Rp 27.000
            d1. Ayam Lada Hitam              : Rp 30.000
            e1. Nasi Uduk                    : Rp 10.000 
            ==============================
            Minuman
            ==============================
            a2. Teh/Es       : Rp 3.000
            b2. Jeruk/Es     : Rp 4.000
            c2. Lemon Tea/Es : Rp 6.000
            d2. Susu/Es      : Rp 8.000
            e2. Kopi         : Rp 10.000
            ==============================
            """)

    total3 = 0
    menu3 = ""
    jumlahpesan2 = 0
    buah = 0
    diskon = ""
    ppn = 0

    def makanan():
        global total3
        global jumlahpesan2
        global menu3
        global diskon
        global ppn
        print("\nMakanan")
        pesan = str(input("Masukkan Kode Menu ="))
        jumlahpesan2 = int(input("Jumlah Pesanan ="))
        if pesan == "a1":
            menu3 = "Ayam Saus Tiram"
            harga = (30000 * jumlahpesan2)
            ppn = int(harga * 0.1)
            if jumlahpesan2 >= 5:
                diskon = int(harga * 0.2)
                total3 = int(harga - diskon + ppn)
            else:
                total3 = int(harga + ppn)
        elif pesan == "b1":
            menu3 = "Ayam Goreng Mentega"
            harga = (28000 * jumlahpesan2)
            ppn = int(harga * 0.1)
            if jumlahpesan2 >= 5:
                diskon = int(harga * 0.2)
                total3 = int(harga - diskon + ppn)
            else:
                total3 = int(harga + ppn)
        elif pesan == "c1":
            menu3 = "Ayam Goreng Crispy"
            harga = int(27000 * jumlahpesan2)
            ppn = int(harga * 0.1)
            if jumlahpesan2 >= 5:
                diskon = int(harga * 0.2)
                total3 = int(harga - diskon + ppn)
            else:
                total3 = int(harga + ppn)
        elif pesan == "d1":
            menu3 = "Ayam Lada Hitam"
            harga = int(30000 * jumlahpesan2)
            ppn = int(harga * 0.1)
            if jumlahpesan2 >= 5:
                diskon = int(harga * 0.2)
                total3 = int(harga - diskon + ppn)
            else:
                total3 = int(harga + ppn)
        elif pesan == "e1":
            menu3 = "Nasi Uduk"
            harga = int(10000 * jumlahpesan2)
            ppn = int(harga * 0.1)
            if jumlahpesan2 >= 5:
                diskon = int(harga * 0.2)
                total3 = int(harga - diskon + ppn)
            else:
                total3 = int(harga + ppn)
        else:
            print("Menu tidak terdaftar, silahkan ulangi kembali")
            makanan()
    makanan()

    total4 = 0
    menu4 = ""
    jumlah2 = 0


    def minuman():
        global total4
        global menu4
        global jumlah2
        global diskon
        global ppn
        print("\nMinuman")
        pesan = str(input("Masukkan Kode Menu ="))
        jumlah2 = int(input("Jumlah Pesanan ="))

        if pesan == "a2":
            menu4 = "Teh/Es"
            harga = (3000 * jumlah2)
            ppn = int(harga * 0.1)
            diskon = 0
            total4 = int(harga + ppn)
        elif pesan == "b2":
            menu4 = "Jeruk/Es"
            harga = int(4000 * jumlah2)
            ppn = int(harga * 0.1)
            diskon = 0
            total4 = int(harga + ppn)
        elif pesan == "c2":
            menu4 = "Lemon Tea/Es"
            harga = int(6000 * jumlah2)
            ppn = int(harga * 0.1)
            diskon = 0
            total4 = int(harga + ppn)
        elif pesan == "d2":
            menu4 = "Susu/Es"
            harga = int(8000 * jumlah2)
            ppn = int(harga * 0.1)
            diskon = 0
            total4 = int(harga + ppn)
        elif pesan == "e2":
            menu4 = "Kopi"
            harga = int(10000 * jumlah2)
            ppn = int(harga * 0.1)
            diskon = 0
            total4 = int(harga + ppn)
        else:
            print("Menu tidak terdaftar, silahkan ulangi kembali")
            minuman()
    minuman()

    totalharga = total1 + total2 + total3 + total4
    print("--------------------------")
    print("Pesanan")
    print("--------------------------")
    print("Menu :", menu1, "||", menu2, "||", menu3, "||", menu4)
    print("Jumlah :", jumlahpesan1, "porsi", "||", jumlah1, "buah", "||", jumlahpesan2, "porsi", "||", jumlah2, "buah")
    print("Harga :", total1, "+", total2, "+", total3, "+", total4)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Total :", totalharga)
    print("--------------------------")

pastikan_pesanan = str(input("Apakah pesanan Anda sudah sesuai? Silahkan periksa kembali (y/n) ="))
if pastikan_pesanan == 'y':
    print("Silahkan lanjut ke pembayaran")
else:
    print("Masukkan kembali pesanan Anda =  """"
        >>>>>>>>>>>> MENU <<<<<<<<<<<<
        Makanan
        ==============================
        a1. Ayam Saus Tiram              : Rp 30.000
        b1. Ayam Goreng Mentega          : Rp 28.000
        c1. Ayam Goreng Crispy           : Rp 27.000
        d1. Ayam Lada Hitam              : Rp 30.000
        e1. Nasi Uduk                    : Rp 10.000 
        ==============================
        Minuman
        ==============================
        a2. Teh/Es       : Rp 3.000
        b2. Jeruk/Es     : Rp 4.000
        c2. Lemon Tea/Es : Rp 6.000
        d2. Susu/Es      : Rp 8.000
        e2. Kopi         : Rp 10.000
        ==============================
        """)
    print(makanan())
    print(minuman())

    totalharga = total1 + total2

    print("--------------------------")
    print("Pesanan")
    print("--------------------------")
    print("Menu :", menu1, "||", menu2)
    print("Jumlah :",jumlahpesan1, "porsi", "||", jumlah1, "buah")
    print("Harga :", total1, "+", total2)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Total :", totalharga)
    print("--------------------------")

print("\nTotal harus Dibayar: ", totalharga)
metode_pembayaran = str(input("Melakukan pembayaran melalui (Cash/Kredit/Ovo/Go-Pay) = "))
if metode_pembayaran == 'cash':
    print("Silahkan menuju kasir dan melakukan pembayaran")
elif metode_pembayaran == 'kredit':
    print("Silahlan melakukan pembayaran ke Rekening 98023813 BCA")
elif metode_pembayaran == 'ovo/go-pay':
    print("Silahkan melakukan pembayaran ke Ovo/Go-Pay = 0875142378927")
else:
    print("Maaf metode pembayaran tidak tersedia")
pasti_bayar = str(input("Apakah sudah melakukan pembayaran? (y/n) = "))
if pasti_bayar == 'y':
    print("Silahkan lanjut")
else:
    print("Maaf pesanan anda dibatalkan")
    exit()
bayar = int(input("Pelanggan membayar sebesar :"))
kembalian = int(bayar - totalharga)
print("Kembalian :", kembalian)

if pesanlagi == "y":
    print("\n=============================================================")
    print("                           STRUK                             ")
    print("=============================================================")
    print(" Nama                :", pelanggan)
    print(" Meja                :", nomormeja)
    print(" Pesanan             :", jumlahpesan1, " ", menu1, "  ", total1)
    print("                     :", jumlah1, "  ", menu2, "   ",  total2)
    print("                     :", jumlahpesan2, " ", menu3, "   ", total3)
    print("                     :", jumlah2, "  ", menu4, "   ", total4)
    print("                     : ---------------------------------------")
    print(" Total               :                           Rp.", totalharga)
    print(" Metode Pembayaran   :", metode_pembayaran)
    print(" Nominal Bayar       : Rp.", bayar)
    print(" Kembalian           : Rp.", kembalian)
    print("==============================================================")
    print("                        TERIMA KASIH                          ")
    print("==============================================================")
else:
    print("\n=============================================================")
    print("                           STRUK                             ")
    print("=============================================================")
    print(" Nama                :", pelanggan)
    print(" Meja                :", nomormeja)
    print(" Pesanan             :", jumlahpesan1, " ", menu1, "  ", total1)
    print("                     :", jumlah1, "  ", menu2, "   ",  total2)
    print("                     : ---------------------------------------")
    print(" Total               :                           Rp.", totalharga)
    print(" Metode Pembayaran   :", metode_pembayaran)
    print(" Nominal Bayar       : Rp.", bayar)
    print(" Kembalian           : Rp.", kembalian)
    print("==============================================================")
    print("                        TERIMA KASIH                          ")
    print("==============================================================")
