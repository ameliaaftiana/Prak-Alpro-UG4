#proses
def selisih_hari(tanggal1, bulan1, tanggal2, bulan2):
    if bulan1==1 or bulan1==3 or bulan1==5 or bulan1==7 or bulan1==8 or bulan1==10 or bulan1==12:
        hari=31-tanggal1
        
    elif bulan1==4 or bulan1==6 or bulan1==9 or bulan1==11:
        hari=30-tanggal1 
        
    elif bulan1==2:
        hari=28-tanggal1
        
    
    harii=hari+tanggal2
    print(harii,"hari") #output
    
#input
bulan1=int(input("Masukkan Bulan 1 = "))
tanggal1=int(input("Masukkan Tanggal 1 = "))
bulan2=int(input("Masukkan Bulan 2 = " ))
tanggal2=int(input("Masukkan Tanggal 2 = "))

selisih_hari(tanggal1, bulan1, tanggal2, bulan2)