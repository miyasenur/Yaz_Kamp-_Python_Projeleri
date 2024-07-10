import random
def kelime_tahmin_oyunu():
    # Gizli kelime havuzu
    kelimeler = ["python", "yapay", "zeka", "yazılım", "kamp"]
    gizli_kelime = random.choice(kelimeler)
    tahmin_edilen = ["_"] * len(gizli_kelime)
    yanlis_tahminler = []
    can = 5

    print("Kelime Tahmin Oyunu'na Hoşgeldiniz!")
    print("Gizli kelimeyi harf harf tahmin edin.")
    print("Yanlış tahmin ettiğinizde bir can kaybedersiniz.")
    print("Toplamda 5 canınız var.")

    while can > 0 and "_" in tahmin_edilen:
        print(f"Mevcut durum: {' '.join(tahmin_edilen)}")
        print(f"Yanlış tahminler: {', '.join(yanlis_tahminler)}")
        print(f"Kalan can: {can}")

        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen sadece bir harf girin.")
            continue

        if tahmin in tahmin_edilen or tahmin in yanlis_tahminler:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        if tahmin in gizli_kelime:
            for i in range(len(gizli_kelime)):
                if gizli_kelime[i] == tahmin:
                    tahmin_edilen[i] = tahmin
            print("Doğru tahmin!")
        else:
            yanlis_tahminler.append(tahmin)
            can -= 1
            print("Yanlış tahmin!")

    if "_" not in tahmin_edilen:
        print(f"Tebrikler! Gizli kelimeyi doğru tahmin ettiniz: {gizli_kelime}")
    else:
        print(f"Maalesef, kaybettiniz. Gizli kelime: {gizli_kelime}")

kelime_tahmin_oyunu()
