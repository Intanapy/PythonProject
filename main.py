# PERSONAL EXPENSE TRACKER
# Dashboard
def dashboard():
    print("DASHBOARD PERSONAL EXPENSE TRACKER")
    print("1. Catat Transaksi")
    print("2. Riwayat Transaksi")
    print("3. Edit Transaksi")
    print("4. Lihat Saldo")
    print("5. Keluar")

def catat_transaksi():
    print("==== TAMBAH TRANSAKSI ====")
    print("Pilih jenis transaksi: ")
    print("1. Pemasukan")
    print("2. Pengeluaran")

    catat = int(input("Pilihan: "))
    return catat

def pemasukan():
    print("==== PEMASUKAN ====")
    deskripsi = input("Deskripsi pemasukan: ")
    nominal = int(input("Nominal pemasukan: "))
    kategori = input("Kategori pemasukan: ")
    tipe = "Pemasukan"

    trx = {
        "deskripsi": deskripsi,
        "nominal": nominal,
        "kategori": kategori,
        "tipe": tipe
    }
    return trx

def pengeluaran():
    print("==== PENGELUARAN ====")
    deskripsi = input("Deskripsi pengeluaran: ")
    nominal = int(input("Nominal pengeluaran: "))
    kategori = input("Kategori pengeluaran: ")
    tipe = "Pengeluaran"

    trx = {
        "deskripsi": deskripsi,
        "nominal": nominal,
        "kategori": kategori,
        "tipe": tipe
    }
    return trx

# Program Utama
def program_utama():
    while True:
        dashboard()
        pilihan_menu = int(input("Pilih Menu: "))
        if pilihan_menu == 1:
            while True:
                catat = catat_transaksi()
                if catat == 1:
                    transaksi = pemasukan()
                    deskripsi, nominal, kategori, tipe = transaksi.values()
                    print("Total pemasukan = ", nominal)
                    print("Kategori pemasukan = ", kategori)
                    print("Deskripsi: ", deskripsi)
                    print("Tipe: ", tipe)
                    break
                elif catat == 2:
                    transaksi = pengeluaran()
                    deskripsi, nominal, kategori, tipe = transaksi.values()
                    print("Total pengeluaran = ", nominal)
                    print("Kategori pengeluaran = ", kategori)
                    print("Deskripsi: ", deskripsi)
                    print("Tipe: ", tipe)
                    break
                else:
                    print("Pilihan tidak valid")
        elif pilihan_menu == 2:
            pass
        elif pilihan_menu == 3:
            pass
        elif pilihan_menu == 4:
            pass
        elif pilihan_menu == 5:
            break
        else:
            print("Pilihan Tidak Valid!")

# Start
if __name__ == "__main__":
    program_utama()