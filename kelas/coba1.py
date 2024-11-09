daftar = [
    {   "nim":"001",
        "nama":"Budi",
        "nilai":80
    },
    {   "nim":"002",
        "nama": "Ayu",
        "nilai":92
    },
    {   "nim":"003",
        "nama": "Yuda",
        "nilai":77
    }
]

n = 0

while n<3:
    print(n+1,". ", daftar[n]["nama"], sep="")
    n += 1