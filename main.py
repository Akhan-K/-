# 1.1. Ввод и расчёт расходов
print("=== Финансовое приложение ===")
name = input("Введите ваше имя: ")
month = input("Введите месяц: ")
salary = float(input("Введите ваш доход за месяц: "))
spendings = float(input("Введите ваши расходы за месяц: "))
balance = salary - spendings
print(f"{name}, ваш баланс за {month}: {balance} руб.")

# 1.2. Работа со списками, множествами, кортежами
categories = input("Введите категории расходов через запятую: ").lower().replace(' ', '').split(',')
categories_set = set(categories)
categories_tuple = tuple(categories_set)
print("Категории расходов (без повторов):", categories_set)
print("Категории расходов (tuple):", categories_tuple)

# 1.3. Работа со строкой и условиями
search = input("Введите категорию для поиска: ").lower()
if search in categories_set:
    print(f"Категория '{search}' есть в списке расходов.")
else:
    print(f"Категории '{search}' нет в списке расходов.")

# 1.4. Словарь и меню
expenses = {}  # {"категория": сумма}

while True:
    print("\nМеню:")
    print("1. Добавить расход")
    print("2. Посмотреть все расходы")
    print("3. Выйти")
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        cat = input("Категория расхода: ").lower()
        amount = float(input("Сумма расхода: "))
        expenses[cat] = expenses.get(cat, 0) + amount
        print("Расход добавлен!")
    elif choice == "2":
        print("Текущие расходы:")
        for cat, amount in expenses.items():
            print(f"{cat}: {amount} руб.")
    elif choice == "3":
        print("До свидания!")
        break
    else:
        print("Некорректный ввод, попробуйте снова.")
