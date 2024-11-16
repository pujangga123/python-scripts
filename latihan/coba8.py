import random

jawaban = random.randint(1, 100)

print("Program dibuat oleh Sylvia HAHAHA")

print("Hay Hay Hay Selamat Datang di Permainan Tebak Angka!")
print("Aku udah pilihin angka dari 1 sampai 100.")
print("Coba tebak angka tersebut.")

percobaan = 0

while True:
    try:
        tebakan = int(input("Masukkan tebakan kamu: "))
        percobaan += 1 
        
        if tebakan < jawaban:
            print("Angkanya terlalu kecil. Coba lagi ya.")
        elif tebakan > jawaban:
            print("Angkanya terlalu besar. Ayo dongg.")
        else:
            print(f"Ciee selamat ya! Kamu menebak dengan benar pada percobaan ke-{percobaan}.")
            break
    except ValueError:
        print("Kamu gimana sih? Masukin angka dong.")