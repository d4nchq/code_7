#початкові дані про багаж пасажирів.
baggage = {
    1: {"items": 3, "total_weight": 15},
    2: {"items": 1, "total_weight": 10},
    3: {"items": 5, "total_weight": 30},
    4: {"items": 2, "total_weight": 8},
    5: {"items": 3, "total_weight": 25},
    6: {"items": 1, "total_weight": 20},
    7: {"items": 4, "total_weight": 18},
    8: {"items": 2, "total_weight": 28},
    9: {"items": 1, "total_weight": 24},
    10: {"items": 3, "total_weight": 12}
}

#функція для виведення всіх значень словника.
def print_baggage(baggage):
    for passenger, info in baggage.items():
        print(f"Пасажир {passenger}: Речі - {info['items']}, Загальна вага - {info['total_weight']} кг")

#функція для додавання нового запису.
def add_baggage(baggage, passenger, items, total_weight):
    baggage[passenger] = {"items": items, "total_weight": total_weight}
    print(f"Додано багаж для пасажира {passenger}.")

#функція для видалення запису зі словника.
def delete_baggage(baggage, passenger):
    try:
        del baggage[passenger]
        print(f"Видалено багаж для пасажира {passenger}.")
    except KeyError:
        print("Помилка: Пасажира не знайдено у списку багажу.")

#функція для перегляду вмісту словника за відсортованими ключами.
def print_sorted_baggage(baggage):
    sorted_baggage = {k: baggage[k] for k in sorted(baggage)}
    print("Інформація про багаж за сортуванням:")
    print_baggage(sorted_baggage)

#функція для виконання завдань за умовою.
def analyze_baggage(baggage):
    #а)кількість пасажирів з більше ніж двома речами.
    more_than_two_items = sum(1 for info in baggage.values() if info['items'] > 2)
    print("Кількість пасажирів з більше ніж двома речами:", more_than_two_items)
    
    #б)чи є пасажир з однією річчю вагою менше 25 кг.
    one_item_under_25kg = any(info['items'] == 1 and info['total_weight'] < 25 for info in baggage.values())
    print("Чи є пасажир з однією річчю вагою менше 25 кг:", one_item_under_25kg)
    
    #в)номер багажу, де вага однієї речі відрізняється від середньої не більше, ніж на 0,5 кг.
    avg_weight_per_item = sum(info['total_weight'] / info['items'] for info in baggage.values()) / len(baggage)
    close_to_avg = [passenger for passenger, info in baggage.items()
                    if abs((info['total_weight'] / info['items']) - avg_weight_per_item) <= 0.5]
    print("Номери пасажирів, чия середня вага речей близька до загальної середньої (±0,5 кг):", close_to_avg)

#головна функція для роботи з меню.
def main():
    while True:
        print("\nМеню:")
        print("1 - Показати всю інформацію про багаж")
        print("2 - Додати новий багаж")
        print("3 - Видалити багаж")
        print("4 - Показати відсортовану інформацію про багаж")
        print("5 - Аналізувати дані багажу")
        print("0 - Вийти")
        
        choice = input("Введіть ваш вибір: ")
        
        if choice == '1':
            print_baggage(baggage)
        elif choice == '2':
            passenger = int(input("Введіть номер пасажира: "))
            items = int(input("Введіть кількість речей: "))
            total_weight = float(input("Введіть загальну вагу багажу: "))
            add_baggage(baggage, passenger, items, total_weight)
        elif choice == '3':
            passenger = int(input("Введіть номер пасажира для видалення: "))
            delete_baggage(baggage, passenger)
        elif choice == '4':
            print_sorted_baggage(baggage)
        elif choice == '5':
            analyze_baggage(baggage)
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

#запуск програми.
main()
