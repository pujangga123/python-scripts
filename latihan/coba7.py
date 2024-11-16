

def tanya():
    try:
        bebas = int(input("Masukan?"))
        
        if bebas > 5 :
            print("angka besar")
        else:
            print("angka kecil")
    except ValueError:
        print("Masukkan angka yang valid!")


print("Program tanya")
tanya()
