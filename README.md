# Automatic Restaurant Bill
Tugas Besar Praktikum Program Komputer 2021 Kelas C Kelompok  18

Program ini dibuat untuk membantu usaha di bidang makanan atau restauran dalam pelayanan khususnya dalam pembayaran di kasir. Dengan adanya pengembangan informasi yang digunakan dalam pemesanan menu dan harga dapat mendukung _customer_ dalam melakukan pemesanan secara efektif dan efisien dalam waktu.


# Repository

Berkas "18_Tubes_Diagram Alir Program"
    
        Merupakan lampiran berupa diagram alir yang 
        menjelaskan cara kerja program

Berkas "18_Tubes_Laporan Tugas Besar Tahap I"

        Merupakan lampiran berupa laporan tugas besar tahap 1 yang
        menjelaskan mengenai gagasan ide program, yaitu automatic restaurant bill 
        
Berkas "restaurantBill.py"
        
        Merupakan lampiran berupa program python yang
        berisi mengenai program automatic restaurant bill
        
Berkas “struk_pendukung program”

	    Merupakan lampiran yang berguna sebagai pendukung
	    jalannya program automatic restaurant bill
        
Berkas “18_Tubes_Referensi Program”

	    Merupakan lampiran berupa inspirasi program yang digunakan 
	    sebagai referensi dalam pengembangan program automatic restaurant bill
        
Berkas “README.md”

	    Merupakan penjelasan singkat isi dari repository
        
        
# System Requirement


Spesifikasi OS : Windows 7 atau lebih, macOS


Python Version : 3.7 atau lebih


# Penjelasan Singkat Program


1. Pelanggan restaurant diminta untuk memasukkan nama dan nomor meja pada _display_ kasir.
   
2. Setelah ter-_input_, pelanggan dapat memesan makanan dan minuman dengan menuliskan kode menu yang tertera pada layar.
   Apabila kode menu tidak sesuai, pelanggan akan diminta untuk mengisi ulang kode menu hingga sesuai.
   
3. Selanjutnya pelanggan diminta memasukkan jumlah tiap pesanan yang akan dipesan.
   Apabila jumlah pesanan melebihi stok yang telah disediakan, maka program akan secara otomatis meminta pelanggan untuk memasukkan kode menu kembali.

4. Jika jumlah pesanan yang dipesan oleh pelanggan sesuai dengan stok yang dimiliki, maka secara otomatis program akan memunculkan total harga dari pesanan yang telah ditambah PPN dan dikurangi diskon.
   Pelanggan akan mendapatkan diskon apabila memesan makanan atau minuman >5
        
	Total Harga = Harga makanan/minuman + PPN (10%) - diskon (20%)

5. Setelah itu, pelanggan diminta untuk memilih apakah ingin memesan kembali atau tidak.
   Apabila pelanggan memilih memesan kembali, maka program akan memunculkan _display_ menu dan pelanggan diminta untuk memasukkan kode menu seperti di atas.

6. Jika pelanggan memilih tidak memesan kembali, maka pelanggan diminta untuk memeriksa apakah pesanan yang dipesan sudah sesuai atau belum.
   Apabila pesanan belum sesuai maka program akan kembali menampilkan _display_ menu dan pelanggan diminta untuk memesan ulang.
   
7. Jika pesanan telah sesuai, maka pelanggan diminta untuk membayar pesanan dengan beberapa metode pembayaran yang telah disediakan, sperti _cash_, kredit, ovo, atau go-pay.
   
8. Lalu program akan menanyakan, apakah pelanggan sudah melakukan transaksi pembayaran atau belum. 
   Apabila pelanggan belum melakukan transaksi pembayaran, maka program akan secara otomatis membatalkan pesanan tersebut.
   
9. Jika pelanggan telah melakukan pembayaran, maka pelanggan akan diminta memasukkan jumlah nominal uang dibayarkan pada layar yang tertera. 
   Program akan secara otomatis memproses pembayaran pelaggan dan menghitung nominal uang kembalian.
   
10. Program juga akan meberikan output kepada pelanggan berupa nota/struk pembelian yang berisi nama pelanggan, nomor meja, rincian pesanan, total harga, metode pembayaran yang dipilih, nominal yang dibayarkan, dan juga jumlah uang kembalian pelanggan. 
