def periksa(angka):
    try:
        bebas = int(angka)
        
        if bebas > 5 :
            return "angka besar"
        else:
            return "angka kecil"
    except ValueError:
        return "salah"

print("Program tanya")
nilai1 = input("Masukan pertama:")
print(periksa(nilai1))
tulisan = periksa(nilai1)

nilai2 = input("Masukan kedua:")
print(periksa(nilai2))
