#  BMI Calculator
#  Formula Bmi = kg/tinggi^2
#  Latihan Pengulangan Saya

import time
print("Kalkulator Bmi")

while True:
    try:
        berat = float(input("Sila masukkan berat: "))
        if berat <10:
            print("Ralat : Minimum 10 askara keatas, sahaja.")
        else:
            break
    except ValueError:
        print("Masukkan Nombor sahaja.")
    except ValueError:
        print("Masukkan Nombor sahaja.")
time.sleep(0.2)
print ("berat :")
time.sleep(0.3)
print(berat)
time.sleep(0.5)
while True:
    try:
        tinggi = float(input("Sila masukkan tinggi (dalam meter): "))
        break
    except ValueError:
        print("Masukkan Nombor sahaja.")
        
time.sleep(0.2)

print ("tinggi :")

time.sleep(0.3)
print(tinggi)
time.sleep(0.5)

bmi = berat / tinggi**2
print("BMI anda ialah " + str(round(bmi,2)))

if bmi <18.5:
    category = "Kekurangan Berat Badan"
elif bmi <24.9:
    category = "Normal"
elif bmi <29.9:
    category = "Berat"
elif bmi >29.9:
    category = "Obesiti"

time.sleep(0.5)
print("Kategori anda ialah: " + category)
