def parola_gucu_kontrol(parola):
    guc = 0

    if len(parola) >= 8:
        guc += 1

    ozel_karakterler = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    if any(char in ozel_karakterler for char in parola):
        guc += 1

    if any(char.isdigit() for char in parola):
        guc += 1

    if any(char.isupper() for char in parola):
        guc += 1

    if any(char.islower() for char in parola):
        guc += 1

    return guc

parola = input("Lütfen bir parola girin: ")

guc = parola_gucu_kontrol(parola)

if guc == 5:
    print("Parolanız çok güçlü!")
elif guc >= 3:
    print("Parolanız güçlü.")
elif guc >= 2:
   print("Parolanız orta düzeyde güçlü.")
elif guc >= 1:
    print("Parolanız zayıf. Daha güçlü bir parola seçmenizi öneririz.")
else:
    print("Parolanız çok zayıf. Güvenlik riski taşıyor. Lütfen daha güçlü bir parola seçin.")

