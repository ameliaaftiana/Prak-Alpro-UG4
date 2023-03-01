#proses
def jumlah_hari(nama_bulan):
    if nama_bulan=="januari" or nama_bulan=="maret" or nama_bulan=="mei" or nama_bulan=="juli" or nama_bulan=="agustus" or nama_bulan=="oktober" or nama_bulan=="desember":
        print ("31") #output
    elif nama_bulan=="februari":
        print("28") #output
    elif nama_bulan=="april" or nama_bulan=="juni" or nama_bulan=="september" or nama_bulan=="november":
        print ("30") #output
    else:
        print ("Tidak valid") #output

#input
nama_bulan=input("Masukkan Nama Bulan = ")

jumlah_hari(nama_bulan)