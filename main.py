print('Ortalama Hesaplama Uygulamasına Hoşgeldiniz')
vize = int(input('Vizenizi Girin:'))
final = int(input('Finalinizi Girin:'))
ort= vize * 0.4 + final * 0.6
if ort >= 90 or ort ==100:
 harfnot='AA'
elif ort >= 80 or ort <90:
 harfnot='BA'
elif ort >= 70 or ort <80:
 harfnot = 'BB'
elif ort >= 60 or ort <70:
 harfnot = 'CB'
elif ort >=55 or ort <60:
 harfnot = 'CC'
elif ort >=50 or ort<55:
 harfnot = 'CD'
elif ort >= 45 or ort <50:
 harfnot='DD'
elif ort<45:
 harfnot='FF'
print(f'Ortalamanız:{ort} Harf Notunuz:{harfnot}')