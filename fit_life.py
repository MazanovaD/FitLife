# Проект FitLife - MVP версия 1.0


WATER_PER_KG = 30
ML_TO_LITERS = 1000


def get_user_weight():
    """Возвращает вес (в кг)"""
    while True:
        try:
            return float(
                input("Какой у Вас вес? (в кг) ")
            )
        except ValueError:
            print("Введите вес в кг, например 60.5")


def get_user_height():
    """Возвращает рост (в м)"""
    while True:
        try:
            return float(
                input("Какой у Вас рост? (в метрах) ")
            )
        except ValueError:
            print("Введите рост в метрах, например 1.75")


# Знакомство
user_name = input("Как Вас зовут? ")
user_age_str = input("Сколько Вам лет? ")
user_age = int(user_age_str)


# Сбор данных
user_weight = get_user_weight()
user_height = get_user_height()


# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)


# Подсчет воды
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / ML_TO_LITERS, 1)


# Вывод результата
print("=========================================================")
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
