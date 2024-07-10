import random

def sayiTahmin():
    sayi = random.randint(1, 100)
    hak = 5
    print(f"Sayı tahmin oyununa hoşgeldiniz."
          f"\n1 ile 100 arasındaki sayıyı tahmin ediniz."
          f"\n{hak} hakkınız var")
    print(sayi)

    while hak > 0:
        tahmin = int(input("Tahmininiz: "))
        hak -= 1
        if tahmin < sayi:
            print(f"Daha büyük bir sayı giriniz. Tahmin hakkınız: {hak}")
        elif tahmin > sayi:
            print(f"Daha küçük bir sayı giriniz. Tahmin hakkınız: {hak}")
        else:
            print(f"Tebrikler sayıyı doğru bildiniz!")
            return
    print(f"Maalesef sayıyı bulamadınız. Sayı {sayi} idi.")



sayiTahmin()