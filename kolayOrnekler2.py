# liste içinde 5in katları olan sayıları listeleme

"""sayilar=[12,23,22,35,44,70,88,78,40,38,4,0,93]

for sayi in sayilar:
    if sayi%5==0:
        print(str(sayi))
print("döngü bitti.")"""

# fonksiyon kullanarak bir string içinde belirlenen bir karakterin olup olmadıgını kontrol eden kod

"""def kontrol(str):
    for ch in str:
        if ch == 'ğ':
            return True 
            break

metin=input('metin: ')
if(kontrol(metin)==True):
    print("ğ karakteri metin içinde var.")
else:
    print("ğ karakteri metin içinde yok.")"""


# Kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulan kod

"""def ciftMi(x):
    x%2==0
    return x
toplam=0
sayac=0
sayi=input("ilk sayıyı giriniz: ")
sayi2=input("ikinci sayıyı giriniz: ")

for i in range(int(sayi),int(sayi2)+1):
    if(ciftMi(int(i))):
        toplam=toplam+i
        sayac=sayac+1

print('ortalama: ',(toplam/sayac))"""