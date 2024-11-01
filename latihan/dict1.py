daftar = {
    "001":"Budi",
    "002": "Ayu",
    "003": "Yuda",
    "004": "Robert",
    "005": "Arya",
    "006": "Gunawan Santoro",
    "007": "Joan"}

# cara 1
for nim in daftar:
    print(nim, daftar[nim])

# cara 2
for nim, data in daftar.items():
    print(nim, data)