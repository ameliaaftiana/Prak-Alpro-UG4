#proses
def ratarata(n1,n2,n3,n4,n5,n6,n7,n8):
    list=[n1,n2,n3,n4,n5,n6,n7,n8]
    list.sort()
    t1=list[-1]
    t2=list[-2]
    t3=list[-3]
    t4=list[-4]
    t5=list[-5]
    t6=list[-6]
    nilai=(int(t1)+int(t2)+int(t3)+int(t4)+int(t5)+int(t6))/6
    print("rata-ratanya adalah = ", round(nilai)) #output
    
    
#input
n1=int(input("Nilai 1 = "))
n2=int(input("Nilai 2 = " ))
n3=int(input("Nilai 3 = "))
n4=int(input("Nilai 4 = "))
n5=int(input("Nilai 5 = "))
n6=int(input("Nilai 6 = "))
n7=int(input("Nilai 7 = "))
n8=int(input("Nilai 8 = "))

ratarata(n1,n2,n3,n4,n5,n6,n7,n8)