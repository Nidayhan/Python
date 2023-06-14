print("hello")


# girilen 2 sayıyı toplayan python kodu
# sayi1=input("1.sayıyı girinz")
# sayi2=input("2.sayıyı giriniz")
# toplam=int(sayi1)+int(sayi2)
# print("toplam: ", toplam)


# girilen 3 sayının ortalamasını bulan python kodu
# sayi1=input("ilk sayıyı giriniz: ")
# sayi2=input("ikinci sayıyı giriniz: ")
# sayi3=input("üçüncü ssayıyı griniz: ")
# ort=(float(sayi1)+float(sayi2)+float(sayi3))/3
# print("girilen 3 sayının toplamı: ", ort)


# yazılı ortalaması girilen ogrencinin sınıfı gecme durumu
# ort=input("ortalamanızı giriniz: ")
# if(int(ort)>=50):
    # print("sınıfı gectiniz. ")
# else:
    # print("kaldınız. ")


# girilen sayının tek mi cift mi oldugunu bulan kod
# sayi=input("sayı giriniz: ")
# if(int(sayi)%2==0):
    # print("sayı cift.")
# else:
    # print("sayi tek.")


# kullanıcının girdiği değerlere göre vucut kitle endeksini hesaplayan kod
# boy=int(input("boyunuzu giriniz: "))
# kilo=int(input("kilonuzu giriniz: "))
# endex=kilo/(boy*boy)
# if(endex<=18):
    # print("zayıf.")
# elif(endex>18 and endex<=25):
    # print("kilolu.")
# elif(endex>25 and endex<=30):
  #  print("obez.")
# elif(endex>30):
    # print("ciddi obez.")



# 1 ile 100 arası sayıları listeleyen kod
# for i in range(1,100):
    # print(i)



# 1 ile 100 arası cift sayıları listeleyen kod
# for i in range(1,100):
    # if(i%2==0):
        # print(i)


# 3e ve 5e tam bölünen sayıları yazdıran kod
# for i in range(1,100):
    # if i%3==0 and i%5==0:
        # print(i)


# 1den kullanıcının girdiği sayıya kadar olan cift sayıları listeleyen kod
# sayi=int(input("bir sayı giriniz:"))
# for i in range(1,sayi+1):
    # if(i%2==0):
        # print(i)



# girilen metnin harflerini alt alta yazdıran kod
# metin=input("metni girin:")
# sayac=0
# while(sayac<len(metin )):
    # print(metin[sayac])
    # sayac+=1
# else:
    # print("girdiğin kelimenin harflerini listeledim.")


# klavyeden girilen sayıya kadar olan cift ve tek sayıları ayrı ayrı toplayan kod
# sayi = input('Sayıyı Girin : ')
# tekToplam=0
# ciftToplam=0
# for i in range(1,int(sayi)):
#   if(i%2==0):
    # ciftToplam+=i
#   else:
    # tekToplam+=i
# print("Tek Sayıların Toplamı : {0}".format(tekToplam))
# print("Çift Sayıların Toplamı : {0}".format(ciftToplam))
 

# fonksiyon kullanarak yarıcapı girilen dairenin alanını hesaplayan kod
"""def daireAlan(yaricap):
    alan=float(yaricap)*float(yaricap)*3.14
    print("alan: ",alan)
    return alan

r=input("yarıcapı gir:")
daireAlan(r)"""


# fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan kod
"""def dikdörtgenAlan(uzunluk,genişlik):
    alan=float(uzunluk)*float(genişlik)
    print("alan: ", alan)
    return alan

gen=input("genişlik degerini giriniz:")
uzun=input("yuksekliği giriniz: ")

dikdörtgenAlan(uzun,gen)"""


# tkinter kullanımı
"""import tkinter 
nesne= tkinter.Tk()
nesne.mainloop()"""


# hafta_ici isimli bir liste oluşturarak haftanın günlerini ekleyiniz. Daha sonra sırasıyla cuma ve cumartesi günlerinin listede olup olmadığını kontrol ediniz.

"""haftaİçi=["pazartesi","salı","carsamba","persembe","cuma"]

print("cuma" in haftaİçi)
print("salı" in haftaİçi)
print("cumartesi" in haftaİçi)"""


# kullanıcının girdiği sayının rakamlarını toplayan kod
"""sayi=input("bir sayı giriniz: ")
toplam=0
for rakam in sayi:
    toplam+=int(rakam)

print("sayının rakamları toplami: ",toplam)"""


# girilen metni * kullanarak ekrana yazdırma 
"""metin = input("metin giriniz: ")
print((metin+"\n")*10)"""


# for döngüsü kullanarak ekrana yazma
"""isim=input("isim giriniz: ")
for i in range(10):
    print(isim)"""


