# Проект FitLife - MVP версия 1.0


def check_age(user_age):
    """Проверка возраста"""
    last_number = str(user_age)[-1]
    if last_number in "056789":
        age_word = "лет"
    if last_number in "234":
        age_word = "года"
    if last_number in "1":
        age_word = "год"
    if user_age < 18:
        print("Извините, мы не предоставляем услуги лицам меньше 18 лет")
        exit()
    elif 18 < user_age <= 90:
        return True, age_word
    else:
        print("Неккоректный возраст")
        return False


def check_weight(user_weight):
    """Проверка веса"""
    if user_weight < 40:
        print("Нижняя граница веса 40 килограмм")
        return False
    elif user_weight > 120:
        print("Вверхняя граница весна 120 килограмм")
        return False
    else:
        return True


def check_height(user_height):
    """Проверка роста"""
    if user_height < 1.4:
        print("Нижняя граница роста 1.4 м.")
        return False
    elif user_height > 2.1:
        print("Вверхняя граница роста 2.1 м.")
        return False
    else:
        return True


# 1. Знакомство
while True:
    user_name = str(input("Как тебя зовут?\n").title().strip())
    if user_name != "":
        break
    else:
        print("Давайте попробуем снова.")

while True:
    user_age = int(input(f"Какой у тебя возраст, {user_name}?\n"))
    check, age_word = check_age(user_age)
    if check:
        break

# 2. Сбор данных
while True:
    user_weight = float(input(f"{user_name}, какой у тебя вес?\n"))
    if check_weight(user_weight):
        break

while True:
    user_height = float(
        input(f"""{user_name}, какой у тебя рост?(например 1.75)\n"""))
    if check_height(user_height):
        break

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height**2), 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_l = water_ml / 1000


# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} {age_word}.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л в день")
print("Расчет окончен. Будьте здоровы!")
