# contoh function dengan return value
def periksa(angka):
    try:
        bebas = int(angka)
        
        if bebas > 5 :
            return "angka besar"
        else:
            return "angka kecil"
    except ValueError:
        return "salah"

# contoh function tanpa return value
def tanya():
    try:
        bebas = int(input("Masukan?"))
        
        if bebas > 5 :
            print("angka besar")
        else:
            print("angka kecil")
    except ValueError:
        print("Masukkan angka yang valid!")