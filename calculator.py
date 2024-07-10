def calculator():
    x = float(input("ilk sayı: "))
    y = float(input("ikinci sayı: "))

    print("hangi işlemi yapmak istiyorsunuz \n1. Toplama \n2. Çıkarma \n3. Çarpma \n4. Bölme")
    islem = input("Seçiminizi yapınız: ")

    if islem == '1':
        print("Sonuç: ", x + y)
    elif islem == '2':
        print("Sonuç: ", x - y)
    elif islem == '3':
        print("Sonuç: ", x * y)
    elif islem == '4':
        if y == 0:
            print("Sayı 0'a bölünemez")
        else:
            print("Sonuç: ", x / y)
    else:
        print("Geçersiz seçim yaptınız!")

calculator()