import sqlite3

con = sqlite3.connect("fitu.db")
cur = con.cursor()
daftarLatihan = cur.execute("SELECT * FROM daftar_latihan")

count = 1
for i in daftarLatihan.fetchall():
    print(f"{count}. {i[0]}")
    count+=1