print("pandas")

# pandas bir veri bilimi projesindeki veri okuma, veri ön işleme ve veri temizleme işlemleri yapmak için kullanılır

import pandas as pd
import numpy as np

"""pd.Series([10,20,30,40,50]) #serieslerde index yapısı bulunur

data = np.array([10,20,30,40,50])
seri=pd.Series(data)
print(seri)

x=np.array([0,1,2,3,4,5])
y=pd.Series(x, index=[10,11,12,13,14,15]) #index parametresiyle indexleri degiştirdik.dikkat: data ve index uzunlugu aynı olmalı.
print(y)

data={'a':0, 'b':1, 'c':2}
seri=pd.Series(data) #indexe a,b,c atadık
print(seri)

print(seri[0]) #sıfırıncı elemana ulastık

print(seri[0:2]) #sıfırdan 2ye kadar olna elemana ulastık

print(seri['b']) #indexten elemana ulasma

print(seri[['a','b','c']])

print(seri['a':'d'])

seri['a']=90 #deger degiştirme
print(seri)

print(seri.sum())

print(seri.max())

print(seri.mean())

print(seri.median())

isimler=["ali","veli","ayse","fatma","ceren"]

df=pd.DataFrame(isimler, columns=["isimler"])
print(df)

data={'sehirler': ['ankara','bursa','denizli','eskisehir'],
      'plakalar': [6,16,20,26]}

print(data)

df=pd.DataFrame(data,index=['a','b','c','d'])
print(df)


df["hava durumu"]=pd.Series([33,26,40,36],index=['a','b','c','d']) #yeni kolon ekleme
print(df)

df.drop("hava durumu", axis=1, inplace = True) #sütun silme #incplace = true kodu yaptıgımız değişikliği kaydeder bnu yapmazsak df kodunu tekrar print ettiğimizde tablo eski haline döner.
print(df)

df.drop('a', axis=0,inplace = True) #satır silme
print(df)

print(df.loc["b":"d"]) #sectiğimiz indexleri gösterir"""

data={'isimler': ["ali","buse","ceren","deniz","emre","furkan","gizem","hakan"],
      'ogr_no': pd.Series([100,101,102,103,104,105,106,107]),
      'fizik':pd.Series([90,45,67,88,79,84,65,76]),
      'matematik': pd.Series([100,98,67,77,80,59,78,84])}

df=pd.DataFrame(data)
print(df)

print(df['fizik'].sum())
print(df['matematik'].mean())
print(df['fizik'].min())
print(df["matematik"].max())

print(df.describe()) #yukarıdaki işlemleri tek kodla yazdırmak istersek describe kullanırız

print(df[df.matematik>70]["isimler"]) #matematik notu 70ten büyük olanları yazdırır