print ("Belajar live cooding tugas 1")
print()

#kelas A dan B
print ("No 1A dan 1B")
print()
import datetime
waktu =datetime.datetime.now()
print("Hari ini :", waktu)
jam = waktu.hour
menit = waktu.minute

nama = str(input("Masukkan nama anda :"))

if menit==0 :
    if jam > 0 and jam <= 10 :
        print ("Selamat pagi", nama)
    elif jam > 10 and jam <= 15 :
        print ("Selamat siang", nama)
    elif jam > 15 and jam <= 18 :
        print ("Selamat sore", nama)
    elif jam > 18 and jam <= 24:
        print ("Selamat malam", nama)

elif menit > 0 :
    if jam >= 12 and jam < 10 :
        print ("Selamat pagi", nama)
    elif jam >= 10 and jam < 15 :
        print ("Selamat siang", nama)
    elif jam >= 15 and jam <18 :
        print ("Selamat sore", nama)
    elif jam >= 18 and jam < 24 :
        print ("Selamat malam", nama)

print ("No 2A")
print()

bil1 = int(input("Bil ke-1:"))
bil2 = int(input("Bil ke-2:"))
for i in range(bil2):
    print(bil1, end="")
print()

print ("No 3A")
print()
siji = int(input("Bil ke-1:"))
loro = int(input("Bil ke-2:"))
telu = int(input("Bil ke-3:"))

liss = [siji,loro]
for i in range(telu-2):
    siji = liss[i+1] * liss[i]
    liss.append(siji)

for i in range(len(liss)):
    if (i+1) % telu:
        print("%d,"%liss[i], end="")
    elif (i+1) == telu:
        print(liss[i])
print()

print ("No 2B")
print()

a = int (input ("Nilai Variabel a ="))
b = int (input ("Nilai Variabel b ="))
c = int (input ("Nilai Variabel c ="))

hasil = a
done = False
while not done:
    for i in range(c-1):
        print(hasil, end="")
    print(hasil)
    hasil += 1
    
    if hasil == b+1:
        done = True
print()

print ("No 3B")
print()

a = int (input ("Nilai Variabel a ="))
b = int (input ("Nilai Variabel b ="))

if a%2 == 0:
    a+=1
if b%2== 0:
    b-=1
done = False
while not done:
    if a%2 == 1 and a!=b:
        print("%d,"%a,end="")
    elif a == b:
        print(a)
        done = True
    a+=1
