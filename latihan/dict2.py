daftar ={
        "001" : {"nama": "Budi", "nilai": {"IPA": 32, "IPS": 75, "Bahasa Indonesia": 32}},
        "002" : {"nama": "Ayu", "nilai": {"IPA": 42, "IPS": 65, "Bahasa Indonesia": 23}},
        "003" : {"nama": "Yuda", "nilai": {"IPA": 45, "IPS": 34, "Bahasa Indonesia": 53}},
        "004" : {"nama": "Robert", "nilai": {"IPA": 77, "IPS": 54, "Bahasa Indonesia": 32}},
        "005" : {"nama": "Arya", "nilai": {"IPA": 21, "IPS": 43, "Bahasa Indonesia": 76}},
        "006" : {"nama": "Gunawan Santoro", "nilai": {"IPA": 45, "IPS": 1, "Bahasa Indonesia": 87}},
        "007" : {"nama": "Joan", "nilai": {"IPA": 43, "IPS": 65, "Bahasa Indonesia": 76}} 
    }

for nim in daftar:
    print("NIM:", nim)
    print("Nama:", daftar[nim]['nama'])
    print("Nilai IPA", daftar[nim]['nilai']['IPA'])
    print("Nilai IPS", daftar[nim]['nilai']['IPS'])
    print("Nilai Bahasa Indonesia", daftar[nim]['nilai']['Bahasa Indonesia'])
    print()