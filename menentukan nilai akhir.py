#!/usr/bin/python3
nama = input("masukan nama:")
uts = input("masukan nilai UTS:")
uas = input("masukan nilai UAS:")
tugas = input("masukan nilai Tugas:")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

print("\nNama   :",nama)
print("Nilai UTS :",uts)
print("Nilai UAS :",uas)
print("Nilai Tugas:",tugas)
print("Nilai Akhir:",akhir)
print("\nNilai Huruf :",huruf)
print("keterangan :",keterangan)