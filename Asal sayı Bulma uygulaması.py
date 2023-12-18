def asal_sayı(x:int):
    flag = True
    if x == 2:
        return flag
    elif x % 2 == 0:
        flag = False #Eğer Sayı çift ise asal olmayacağından direkt olarak False bir değer oluşturuyor.
    if flag: #Değer yukarıda False olmadıysa kontrol yapılıyor.
        for i in range(3, int(x/2)): #Burada kurduğumuz algoritma kontrolün daha hızlı gerçekleşmesini sağlar
            if x % i == 0:
                print(x, "sayısının" , i , "sayısına bölümü:" , x/i , "kalan ise 0'dır.")
                flag = False
                break
    return flag
x = asal_sayı(4)
print(x)
