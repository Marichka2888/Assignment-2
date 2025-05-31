height=float(input("Введіть свій зріст в метрах:"))
weight=float(input("Введіть свою вагу в кілограмах:"))
bmi=weight/height**2
print(f"При вазі {weight}кг та рості {height} метрів Ваш BMI складає {bmi}")

#task7

start_money=float(input("Введіть початкову сумуггрошей:"))
rate=float(input("Введіть річну відсоткову ставку:"))
month=float(input("Введіть кількість місяців протягом яких ви будете тримати депозит:"))
suma=(start_money*(1+(rate/100)*(month/12)))
print(f"Ви отриамєте {suma} грн.")

