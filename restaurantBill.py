data = "y"
while data == "y":
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
    pesan = str(input("Masukkan Kode Menu ="))
    jumlahpesan = int(input("Jumlah Pesanan ="))
    if pesan == "A1":
        listnama = "Ayam Saus Tiram"
        harga = (30000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = (0)
            totalharga = int(harga + ppn)
    elif pesan == "B1":
        listnama = "Ayam Goreng Mentega"
        harga = (28000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = (0)
            totalharga = int(harga + ppn)
    elif pesan == "C1":
        listnama = "Ayam Goreng Crispy"
        harga = int(27000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    elif pesan == "D1":
        listnama = "Ayam Lada Hitam"
        harga = int(30000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    elif pesan == "E1":
        listnama = "Nasi Uduk"
        harga = int(10000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    elif pesan == "A2":
        listnama = "Teh/Es"
        harga = (3000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 10:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = (0)
            totalharga = int(harga + ppn)
    elif pesan == "B2":
        listnama = "Jeruk/Es"
        harga = int(4000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    elif pesan == "C2":
        listnama = "Lemon Tea/Es"
        harga = int(6000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    elif pesan == "D2":
        listnama = "Susu/Es"
        harga = int(8000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    elif pesan == "E2":
        listnama = "Kopi"
        harga = int(10000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan = input("Menu tidak tersedia, silahkan masukkan kode menu yang tersedia. Silahkan ulangi kembali (y/n) =")

    print("--------------------------")
    print("Restaurant Bill")
    print("--------------------------")
    print("Menu :", listnama)
    print("Jumlah :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Total :", totalharga)
    print("--------------------------")
    
    def pilihan():
        pilihan = input("Apakah anda ingin memesan lagi? (y/n) = ")
        if pilihan == 'y':
            menu()
        else:
            exit()
            
    print("\nTotal harus Dibayar: ", totalharga)
    metode_pembayaran = str(input("Melakukan pembayaran melalui (Debit/Kredit/Ovo/Go-Pay) = "))
    print("""
        Silahkan melakukan pembayaran melalui
            Rekening = 98023813 BCA
        Ovo / Go - Pay = 0875142378927
        """)
    bayar = int(input("Pelanggan membayar sebesar :"))
    kembalian = int(bayar-totalharga)
    print("Kembalian :", kembalian)

    print("\n==============================================")
    print("===================== BILL ====================")
    print("===============================================")
    print(" Nama                :", pelanggan)
    print(" Meja                :", nomormeja)
    print(" Pesanan             :", listnama, "-", jumlahpesan, "porsi" , "-", totalharga)
    print(" Total               : Rp.", totalharga)
    print(" Metode Pembayaran   :", metode_pembayaran)
    print(" Nominal Bayar       : Rp.", bayar)
    print(" Kembalian           : Rp.", kembalian)
    print("===============================================")
