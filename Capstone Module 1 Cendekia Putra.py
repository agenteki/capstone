from tabulate import tabulate
import os

#Capstone Cendekia Putra Perdana
#JCDS 2602
#BSD CAMPUS
#=================================

#Membuat tampilan bersih
def clear_terminal():
    os.system('clear')

#Dictlist gudang sabun
gudang_sabun = {
    "Facewash" : 
    {"Acne & Oil" : [("SKUFWAO50",50,25000,150),("SKUFWA100",100,40000,150)],
    "Brightening" : [("SKUFWBR50",50,25000,150),("SKUFWBR100",100,40000,150)]},
#----------------------------------------------------------------------------------- 
    "Bodywash" : 
    {"Anti Bacterial" : [("SKUBWAB250",250,50000,150),("SKUBWAB500",500,80000,150)],
    "Fresh & Mint" : [("SKUBWFM250",250,50000,150),("SKUBWFM500",500,80000,150)]},
#----------------------------------------------------------------------------------- 
    "Shampoo" : 
    {"Anti Hairfall" : [("SKUSHAH300",300,45000,150),("SKUSHAH500",500,75000,150)],
     "Anti Dandruff" : [("SKUSHAD300",300,45000,150),("SKUSHAD500",500,75000,150)]}
    }

#Pilihan Menu
def tampilan_menu():
    print("\n\t.:::::GUDANG SABUN MENSCARE:::::.")
    print()
    print("Silahkan Pilih Menu Dengan Memasukan Angka Pada Menu")
    print()
    print("--> [1] Tampilkan Stok Gudang Menscare")
    print("-----------------------------------------------")
    print("--> [2] Masukan Produk Atau Varian Terbaru")
    print("-----------------------------------------------")
    print("--> [3] Perbarui Stok Dan Harga Pada SKU Produk")
    print("-----------------------------------------------")
    print("--> [4] Hapus Produk Atau Varian Dalam Gudang")
    print("-----------------------------------------------")
    print("--> [5] Keluar")
    print()

#Menampilkan Semua Stok dalam Table
def tampilan_stok():
    for jenisproduk, variant in gudang_sabun.items():
        print(f"\nJenis Produk: {jenisproduk}")
        for x_variant, produk in variant.items():
            print(f"Varian Produk: {x_variant}")
            headertabel = ["SKU", "Ukuran (ml)", "Harga", "Stok"]
            print(tabulate(produk, headers=headertabel, tablefmt="grid"))

#Menampilkan table berdasarkan jenis produk
def tampilan_stok_berdasarkan_produk(jenis):
    if jenis in gudang_sabun:
        print(f"\nStok produk {jenis}:")
        for x_variant, produk in gudang_sabun[jenis].items():
            print(f"Varian Produk: {x_variant}")
            headertabel = ["SKU", "Ukuran (ml)", "Harga", "Stok"]
            print(tabulate(produk, headers=headertabel, tablefmt="grid"))

#Menampilkan Sub Menu
def sub_menu():
    print("\n1. Tampilkan Semua Stok")
    print("2. Tampilkan Berdasarkan Jenis Produk")
    pilih_sub = input("Pilih opsi [1/2]: ")
    
    if pilih_sub == "1":
        print("\n.::::::::::TABLE STOK GUDANG MENSCARE::::::::::.")
        tampilan_stok()
    elif pilih_sub == "2":
        tampilan_tabel_nama()
        jenis = input("Masukkan jenis produk yang ingin ditampilkan: ").title()
        if jenis in gudang_sabun:
            tampilan_stok_berdasarkan_produk(jenis)
        else:
            print("Produk tidak ditemukan!")
    else:
        print("Pilihan tidak valid!")

#Menampilkan hanya nama produk dan varian
def tampilan_tabel_nama():
    data = []
    for jenisproduk, varian in gudang_sabun.items():
        for x_variant in varian.keys():
            data.append([jenisproduk, x_variant])
    
    headers = ["Jenis Produk", "Varian"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

#Menampilkan table berdasarkan jenis varian
def tampilan_stok_berdasarkan_varian(produk, varian):
    if produk in gudang_sabun and varian in gudang_sabun[produk]:
        print(f"\nStok untuk {produk} | {varian}:")
        headertabel = ["SKU", "Ukuran (ml)", "Harga", "Stok"]
        print(tabulate(gudang_sabun[produk][varian], headers=headertabel, tablefmt="grid"))

#Memasukan produk baru atau varian baru
def masukan_produk():
    print("\n    .:::STOCK PADA GUDANG SABUN MENSCARE:::.")
    tampilan_stok()
    print()
    
    pilihproduk = input("Apakah Anda ingin menambah produk baru? (y/n): ").lower()
    if pilihproduk == "y":
        produk_input = input("Masukkan jenis produk baru: ").title()
        if produk_input in gudang_sabun:
            print("Produk sudah tersedia!")
            return
        else:
            gudang_sabun[produk_input] = {}

    else:
        produk_input = input("Masukkan jenis produk yang tersedia: ").title()
        if produk_input not in gudang_sabun:
            print("Jenis Produk tidak ditemukan!")
            return
    
    varian_input = input("Masukkan nama varian baru atau varian yang sudah tersedia: ").title()
    if varian_input in gudang_sabun[produk_input]:
        print("Varian sudah ada! Masukkan detail SKU baru.")
        tampilan_stok_berdasarkan_varian(produk_input, varian_input)
    else:
        gudang_sabun[produk_input][varian_input] = []
    
    print("\nCARA PENULISKAN SKU:\nSKU.AB.CD.000 = SKUABCD000 \nAB --> Inisial Produk \nCD--> Inisial Varian \n000--> Jumlah Ml" )
    sku = input("\nMasukkan SKU baru: ").upper()
    for item in gudang_sabun[produk_input][varian_input]:
        if item[0] == sku:
            print("SKU sudah tersedia!")
            return

    while True:
        try:
            size = int(input("Masukan ukuran (ml): "))
            if size <= 0:
                print("Ukuran harus lebih dari 0")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    while True:
        try:
            harga = int(input("Masukan harga: "))
            if harga <= 0:
                print("Harga harus lebih dari 0")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    while True:
        try:
            stock = int(input("Masukan stok: "))
            if stock < 0:
                print("Stok tidak boleh kosong!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    
    gudang_sabun[produk_input][varian_input].append((sku, size, harga, stock))
    print("Produk berhasil ditambahkan!")
    tampilan_stok_berdasarkan_produk(produk_input)

#Meng-update harga dan stok produk
def perbarui_stok_harga():
    print('Berikut adalah stock gudang Menscare')
    tampilan_stok()
    print()

    while True:
        try:
            produk = input("Masukkan jenis produk yang ingin diperbarui: ").strip().title()
            if produk not in gudang_sabun:
                raise ValueError("Produk tidak ditemukan! Silakan coba lagi.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    tampilan_stok_berdasarkan_produk(produk)
    
    while True:
        try:
            varian = input("Masukkan nama varian yang ingin diperbarui: ").strip().title()
            if varian not in gudang_sabun[produk]:
                raise ValueError("Varian tidak ditemukan! Silakan coba lagi.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    print(f"Varian {varian} dari produk {produk} siap diperbarui.")

    
    tampilan_stok_berdasarkan_varian(produk, varian)
    
    print("\nCARA PENULISKAN SKU:\nSKU.AB.CD.000 = SKUABCD000 \nAB --> Inisial Produk \nCD--> Inisial Varian \n000--> Jumlah Ml" )
    print()
    skuinput = input("Masukkan Kode SKU yang ingin diperbarui: ").upper()
    for i, (sku, size, harga, stok) in enumerate(gudang_sabun[produk][varian]):
        if sku == skuinput:
                while True:
                    try:
                        new_harga = int(input("Masukkan harga baru: "))
                        if new_harga < 0:
                            raise ValueError("Harga harus angka dan tidak boleh 0!")
                        break
                    except ValueError:
                        print(f"Error!!!Silakan masukkan angka yang valid.")

                while True:
                    try:
                        new_stok = int(input("Masukkan stok baru: "))
                        if new_stok < 0:
                            raise ValueError("Stok harus angka dan tidak boleh 0!")
                        break
                    except ValueError:
                        print(f"Error!!! Silakan masukkan angka yang valid.")

                gudang_sabun[produk][varian][i] = (sku, size, new_harga, new_stok)
                print("Harga dan stok berhasil diperbarui!")
                tampilan_stok_berdasarkan_varian(produk, varian)
                return
        
    print("SKU tidak ditemukan!")

#Men-delete produk atau varian
def hapus_produk():
    print('Berikut adalah stock gudang Menscare')
    tampilan_stok()

    #Konfirmasi Admin
    admin_cek = input("\nApakah kamu adalah admin? (y/n): ").lower()
    if admin_cek != "y":
        print("Hanya admin yang bisa menghapus data")
        return
 
    #Konfirmasi Password
    password = input("Masukkan password admin: ")
    if password != "admin":
        print("PASSWORD SALAH!! AKSES DITOLAK!!!")
        return


    produk = input("Masukkan jenis produk yang ingin dihapus: ").title()
    if produk not in gudang_sabun:
        print("Produk tidak ditemukan!")
        return
    
    
    tampilan_stok_berdasarkan_produk(produk)
    varian = input(f"\n[ TEKAN >ENTER< UNTUK MENGHAPUS SELURUH [{produk}] ] atau \n[ Masukkan nama varian yang ingin dihapus ]: ").title()
    
    if varian == "":
        del gudang_sabun[produk]
        print(f"\n!!!Produk {produk} berhasil dihapus!!!")
    elif varian in gudang_sabun[produk]:
        tampilan_stok_berdasarkan_varian(produk, varian)
        sku = input(f"\n[ TEKAN >ENTER< UNTUK MENGHAPUS SELURUH [{varian}] ] atau \n[ Masukkan kode SKU yang ingin dihapus ]: ")
        
        if sku == "":
            del gudang_sabun[produk][varian]
            print(f"\n!!!Varian {varian} dari produk {produk} berhasil dihapus!!!")
        else:
            gudang_sabun[produk][varian] = [item for item in gudang_sabun[produk][varian] if item[0] != sku]
            print(f"\n!!!{sku} dari varian {varian} berhasil dihapus!!!")
            tampilan_stok_berdasarkan_varian(produk, varian)
    else:
        print("Varian tidak ditemukan!")

#Running Menu
def menu():
    while True:
        tampilan_menu()
        pilih = input("[ MASUKAN ANGKA PADA MENU YANG INGIN DIPILIH ]: ")
        
        if pilih == "1":
            clear_terminal()
            print("\n.::::::::::TABLE STOK GUDANG MENSCARE::::::::::.")
            sub_menu()
        elif pilih == "2":
            clear_terminal()
            masukan_produk()
        elif pilih == "3":
            clear_terminal()
            perbarui_stok_harga()
        elif pilih == "4":
            clear_terminal()
            hapus_produk()
        elif pilih == "5":
            clear_terminal()
            print("+----------------------------------------------+")
            print("|------ Terima kasih dan Periksa Kembali ------|")
            print("+----------------------------------------------+")
            tampilan_menu()
            pilih = input("[ MASUKAN ANGKA PADA MENU YANG INGIN DIPILIH ]: ")
            break
        else:
            print("Pilihan tidak valid!")

menu()
