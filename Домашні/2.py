attemts = 0 #лічильник_спроб
while attemts < 3:
    word = input ("Введіть промокод:")
    if word == "FS2025":
        print("Знижка активована")
    else:
        attemts += 1
        if attemts < 3:
            print("Невірно. Спробуйте ще раз.")
if attemts == 3:
    print("Невірно. Кількість спроб закінчилась.")