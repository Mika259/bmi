import time
print("Uji Markah Peperiksaan anda")

markah = int(input("Masukkan Markah Peperiksaan : "))
time.sleep(1)

print("markah anda " + str(markah))
time.sleep(1)

if markah <= 39:
    output = "E Gagal(Rasib)"
    print("Usaha lagi")
elif markah <=49:
    output = "D Lulus(Maqbul)"

elif markah <=64:
    output = "C Memuaskan(Jaid)"

elif markah <=74:
    output = "B Bagus(Jaid-Jiddan)"
    
else:
    output = "A Sangat Bagus(Mumtaz)"

print("Gred Markah :" + output)