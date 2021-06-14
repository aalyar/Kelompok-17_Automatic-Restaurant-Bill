from datetime import datetime

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
jumlahpesan = 0
buah = 0
diskon = 0
ppn1 = 0


def makanan():
    global total1
    global jumlahpesan
    global menu1
    global diskon
    global ppn1
    print("\nMakanan")
    pesan = str(input("Masukkan Kode Menu ="))
    jumlahpesan = int(input("Jumlah Pesanan ="))
    if pesan == "a1":
        menu1 = "Ayam Saus Tiram"
        harga = (30000 * jumlahpesan)
        ppn1 = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn1)
            if jumlahpesan > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return(makanan())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
        else:
            total1 = int(harga + ppn1)
    elif pesan == "b1":
        menu1 = "Ayam Goreng Mentega"
        harga = (28000 * jumlahpesan)
        ppn1 = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn1)
            if jumlahpesan > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (makanan())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
        else:
            total1 = int(harga + ppn1)
    elif pesan == "c1":
        menu1 = "Ayam Goreng Crispy"
        harga = int(27000 * jumlahpesan)
        ppn1 = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn1)
            if jumlahpesan > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (makanan())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
        else:
            total1 = int(harga + ppn1)
    elif pesan == "d1":
        menu1 = "Ayam Lada Hitam"
        harga = int(30000 * jumlahpesan)
        ppn1 = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn1)
            if jumlahpesan > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (makanan())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
        else:
            total1 = int(harga + ppn1)
    elif pesan == "e1":
        menu1 = "Nasi Uduk"
        harga = int(10000 * jumlahpesan)
        ppn1 = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            total1 = int(harga - diskon + ppn1)
            if jumlahpesan > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (makanan())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
        else:
            total1 = int(harga + ppn1)
    else:
        print("Menu tidak terdaftar, silahkan masukkan kembali pesanan Anda")
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
    global ppn2
    print("\nMinuman")
    pesan = str(input("Masukkan Kode Menu ="))
    jumlah = int(input("Jumlah Pesanan ="))

    if pesan == "a2":
        menu2 = "Teh/Es"
        harga = (3000 * jumlah)
        ppn2 = int(harga * 0.1)
        total2 = int(harga + ppn2)
        if jumlah > 10:
            print("Maaf stok menu yang tersedia hanya 10")
            return (minuman())
        else:
            print("Pesanan yang Anda pesan sebanyak = ", jumlah)
    elif pesan == "b2":
        menu2 = "Jeruk/Es"
        harga = int(4000 * jumlah)
        ppn2 = int(harga * 0.1)
        total2 = int(harga + ppn2)
        if jumlah > 10:
            print("Maaf stok menu yang tersedia hanya 10")
            return (minuman())
        else:
            print("Pesanan yang Anda pesan sebanyak = ", jumlah)
    elif pesan == "c2":
        menu2 = "Lemon Tea/Es"
        harga = int(6000 * jumlah)
        ppn2 = int(harga * 0.1)
        total2 = int(harga + ppn2)
        if jumlah > 10:
            print("Maaf stok menu yang tersedia hanya 10")
            return (minuman())
        else:
            print("Pesanan yang Anda pesan sebanyak = ", jumlah)
    elif pesan == "d2":
        menu2 = "Susu/Es"
        harga = int(8000 * jumlah)
        ppn2 = int(harga * 0.1)
        total2 = int(harga + ppn2)
        if jumlah > 10:
            print("Maaf stok menu yang tersedia hanya 10")
            return (minuman())
        else:
            print("Pesanan yang Anda pesan sebanyak = ", jumlah)
    elif pesan == "e2":
        menu2 = "Kopi"
        harga = int(10000 * jumlah)
        ppn2 = int(harga * 0.1)
        total2 = int(harga + ppn2)
        if jumlah > 10:
            print("Maaf stok menu yang tersedia hanya 10")
            return (minuman())
        else:
            print("Pesanan yang Anda pesan sebanyak = ", jumlah)
    else:
        print("Menu tidak terdaftar, silahkan masukkan kembali pesanan Anda")
        minuman()
minuman()

totalharga = total1+total2
ppntotal = ppn1+ppn2

print("--------------------------")
print("Pesanan")
print("--------------------------")
print("Menu :", menu1, "||", menu2)
print("Jumlah :",jumlahpesan, "porsi", "||", jumlah, "buah")
print("Harga :", total1, "+", total2)
print("Diskon :", diskon)
print("PPN :", ppntotal)
print("--------------------------")
print("Total :", totalharga)
print("--------------------------")
pastikan_pesanan = str(input("Apakah pesanan Anda sudah sesuai? Silahkan periksa kembali (y/n) ="))
if pastikan_pesanan == 'y':
    print("Silahkan lanjut ke metode pembayaran")
else:
    print("Masukkan kembali pesanan anda =  """"
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

    def makanan():
        global total1
        global jumlahpesan
        global menu1
        global diskon
        global ppn1
        print("\nMakanan")
        pesan = str(input("Masukkan Kode Menu ="))
        jumlahpesan = int(input("Jumlah Pesanan ="))
        if pesan == "a1":
            menu1 = "Ayam Saus Tiram"
            harga = (30000 * jumlahpesan)
            ppn1 = int(harga * 0.1)
            if jumlahpesan >= 5:
                diskon = int(harga * 0.2)
                total1 = int(harga - diskon + ppn1)
                if jumlahpesan > 10:
                    print("Maaf stok menu yang tersedia hanya 10")
                    return (makanan())
                else:
                    print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
            else:
                total1 = int(harga + ppn1)
        elif pesan == "b1":
            menu1 = "Ayam Goreng Mentega"
            harga = (28000 * jumlahpesan)
            ppn1 = int(harga * 0.1)
            if jumlahpesan >= 5:
                diskon = int(harga * 0.2)
                total1 = int(harga - diskon + ppn1)
                if jumlahpesan > 10:
                    print("Maaf stok menu yang tersedia hanya 10")
                    return (makanan())
                else:
                    print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
            else:
                total1 = int(harga + ppn1)
        elif pesan == "c1":
            menu1 = "Ayam Goreng Crispy"
            harga = int(27000 * jumlahpesan)
            ppn1 = int(harga * 0.1)
            if jumlahpesan >=5:
                diskon = int(harga * 0.2)
                total1 = int(harga - diskon + ppn1)
                if jumlahpesan > 10:
                    print("Maaf stok menu yang tersedia hanya 10")
                    return (makanan())
                else:
                    print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
            else:
                total1 = int(harga + ppn1)
        elif pesan == "d1":
            menu1 = "Ayam Lada Hitam"
            harga = int(30000 * jumlahpesan)
            ppn1 = int(harga * 0.1)
            if jumlahpesan >=5:
                diskon = int(harga * 0.2)
                total1 = int(harga - diskon + ppn1)
                if jumlahpesan > 10:
                    print("Maaf stok menu yang tersedia hanya 10")
                    return (makanan())
                else:
                    print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
            else:
                total1 = int(harga + ppn1)
        elif pesan == "e1":
            menu1 = "Nasi Uduk"
            harga = int(10000 * jumlahpesan)
            ppn1 = int(harga * 0.1)
            if jumlahpesan >=5:
                diskon = int(harga * 0.2)
                total1 = int(harga - diskon + ppn1)
                if jumlahpesan > 10:
                    print("Maaf stok menu yang tersedia hanya 10")
                    return (makanan())
                else:
                    print("Pesanan yang Anda pesan sebanyak = ", jumlahpesan)
            else:
                total1 = int(harga + ppn1)
        else:
            print("Menu tidak terdaftar, silahkan masukkan kembali pesanan Anda")
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
        global ppn2
        print("\nMinuman")
        pesan = str(input("Masukkan Kode Menu ="))
        jumlah = int(input("Jumlah Pesanan ="))

        if pesan == "a2":
            menu2 = "Teh/Es"
            harga = (3000 * jumlah)
            ppn2 = int(harga * 0.1)
            total2 = int(harga + ppn2)
            if jumlah > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (minuman())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlah)
        elif pesan == "b2":
            menu2 = "Jeruk/Es"
            harga = int(4000 * jumlah)
            ppn2 = int(harga * 0.1)
            total2 = int(harga + ppn2)
            if jumlah > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (minuman())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlah)
        elif pesan == "c2":
            menu2 = "Lemon Tea/Es"
            harga = int(6000 * jumlah)
            ppn2 = int(harga * 0.1)
            total2 = int(harga + ppn2)
            if jumlah > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (minuman())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlah)
        elif pesan == "d2":
            menu2 = "Susu/Es"
            harga = int(8000 * jumlah)
            ppn2 = int(harga * 0.1)
            total2 = int(harga + ppn2)
            if jumlah > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (minuman())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlah)
        elif pesan == "e2":
            menu2 = "Kopi"
            harga = int(10000 * jumlah)
            ppn2 = int(harga * 0.1)
            total2 = int(harga + ppn2)
            if jumlah > 10:
                print("Maaf stok menu yang tersedia hanya 10")
                return (minuman())
            else:
                print("Pesanan yang Anda pesan sebanyak = ", jumlah)
        else:
            print("Menu tidak terdaftar, silahkan masukkan kembali pesanan Anda")
            minuman()
    minuman()

    totalharga = total1 + total2
    ppntotal = ppn1 + ppn2

print("--------------------------")
print("Pesanan")
print("--------------------------")
print("Menu :", menu1, "||", menu2)
print("Jumlah :",jumlahpesan, "porsi", "||", jumlah, "buah")
print("Harga :", total1, "+", total2)
print("Diskon :", diskon)
print("PPN :", ppntotal)
print("--------------------------")
print("Total :", totalharga)
print("--------------------------")



print("\nTotal harus Dibayar: ", totalharga)
metode_pembayaran = str(input("Melakukan pembayaran melalui (Cash/Kredit/Ovo/Go-Pay) = "))
if metode_pembayaran == 'cash':
    print("Silahkan menuju kasir dan melakukan pembayaran")
elif metode_pembayaran == 'kredit':
    print("Silahkan melakukan pembayaran ke Rekening 98023813 BCA")
    pin_kredit = input("Silahkan masukkan PIN Anda (Masukkan PIN sebanyak 6 digit) = ")
    if len(pin_kredit) < 6 or len(pin_kredit) > 6:
       print("Maaf PIN yang Anda masukkan tidak terdaftar, silahkan masukkan ulang")
       pin_kredit = input("Silahkan masukkan PIN Anda (Masukkan PIN sebanyak 6 digit) = ")
    else:
       print("PIN yang Anda masukkan terdaftar")
elif metode_pembayaran == 'ovo':
    print("Silahkan melakukan pembayaran ke no Ovo = 0875142378927")
elif metode_pembayaran == 'go-pay':
    print("Silahkan melakukan pembayaran ke no Go-Pay = 0875142378927")
else:
    print("Maaf metode pembayaran tidak tersedia")
    exit()
pasti_bayar = str(input("Apakah sudah melakukan pembayaran? (y/n) = "))
if pasti_bayar == 'y':
    print("Silahkan lanjut")
else:
    print("Maaf pesanan Anda dibatalkan")
    exit()
bayar = int(input("Pelanggan membayar sebesar :"))
if bayar < totalharga:
    print("Maaf uang yang Anda masukkan kurang, Silahkan masukkan kembali")
    bayar = int(input("Pelanggan membayar sebesar :"))
kembalian = int(bayar - totalharga)

waktu = datetime.now()
#Open file txt
print("\n=============================================================")
print("                           STRUK                             ")
print("=============================================================")
print("                         ",waktu)
print(" Nama                :", pelanggan)
print(" Meja                :", nomormeja)
print(" Pesanan             :" ,jumlahpesan, menu1, "dan", jumlah, menu2)
print(" Total               : Rp.", totalharga)
print(" Metode Pembayaran   :", metode_pembayaran)
print(" Nominal Bayar       : Rp.", bayar)
print(" Kembalian           : Rp.", kembalian)
print("==============================================================")
print("                        TERIMA KASIH                          ")
print("==============================================================")

struk = "\n=============================================================" \
        "\n                           STRUK                             " \
        "\n=============================================================" \
        "\n                                   {}".format(waktu)
struk1 = "\nNama: {}\nMeja: {}\nJumlah Pesan Makanan: {}\nMenu Makanan: {}\nJumlah Pesan Minuman: {}\nMenu Minuman: {}\nTotal: {}\nMetode Pembayaran: {}\nNominal Bayar: {}\nKembalian: {}".format(pelanggan, nomormeja,jumlahpesan, menu1, jumlah, menu2, totalharga, metode_pembayaran, bayar, kembalian)
struk2 = "\n=============================================================" \
         "\n                        TERIMA KASIH                         " \
         "\n============================================================="

file_data = open("struk.txt", "a")
file_data.write(struk)
file_data.write(struk1)
file_data.write(struk2)
file_data.close()

file_data = open("struk fix.csv", "a+")
file_data.write(struk)
file_data.write(struk1)
file_data.write(struk2)
file_data.close()
