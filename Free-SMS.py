import requests
from os import system as s

import os
os.system("clear")

banner = """
Anlo'X Free SMS

Kodlayan: Anlo'X
Instagram: @kerimakcan_
GitHub: kerimakcan41
WebSite: https://anloks.glitch.me



Anlo'X Free SMS Nedir

Anlo'X Free SMS Günde 1 Kere Kullanabileceğiniz Ücretsiz SMS
Gönderme Aracıdır Zor Durumda Kaldığınızda İnternete Bağlı Olarak
Kullanabilirsiniz Yasa Dışı Kullanım Sorumluluğu Kullanıcıya Aittir
Anlo'X Saygılarla Sunar
Not: Mesaja Max 100 Karakter Girebilirsiniz
"""

print(banner)

tel_no = input("""
Telefon Numarası Giriniz
Örnek: +90**********
Anlo'X@Root: """)

mesaj = input("""
Mesajınızı Yazınız
Örnek: Merhaba
Anlo'X@Root: """)

mesaj0 = mesaj[0:100]

print("\n \n \n Mesajınız Aşağıdaki Gibi Gönderilecektir \n"+mesaj0)

soru = input("\n Mesajınız Gönderilsinmi? [E / H]: ")

if soru == "e" or soru == "E":
    print("\n"+tel_no+"\n"+mesaj0+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': tel_no,
  'message': mesaj0,
  'key': 'textbelt',
    })
    print(resp.json())

elif soru == "h" or soru == "H":
    quit()
else:
    print("\n Mesaj Gönderme İşlemi Başarısız")