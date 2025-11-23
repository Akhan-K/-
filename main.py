import json
from utils import (
    add_user_to_list,
    find_user_by_name,
    remove_user_by_name,
    validate_input,
    calculate_total_balance
)
from finance_classes import FinanceManager, User, FamilyAccount

print("=== All Finance ===")

fm = FinanceManager()
deps = ("еда", "транспорт", "развлечения", "одежда")

# === ФАЙЛОВЫЕ ОПЕРАЦИИ ===
def save_data():
    data = {}

    data["users"] = []
    for u in fm.users:
        data["users"].append({
            "login": u.login,
            "name": u.name,
            "bal": u.bal,
            "spent": u.spent,
            "income": u.income
        })

    if fm.family_account:
        data["family"] = {
            "exists": True,
            "deposit": fm.family_account.deposit,
            "members": [m.name for m in fm.family_account.members]
        }
    else:
        data["family"] = {
            "exists": False,
            "deposit": 0,
            "members": []
        }
    with open("finance_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✅ Data saved")


def load_data():
    try:
        with open("finance_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            fm.users = []
            # загружаем пользователей
            for ud in data.get("users", []):
                user = User(ud["login"], ud["name"], ud["bal"])
                user.spent, user.income = ud.get("spent", 0), ud.get("income", 0)
                fm.users.append(user)

            fam_data = data.get("family", {})
            if isinstance(fam_data, dict) and fam_data.get("exists"):
                fm.family_account = FamilyAccount()
                fm.family_account.deposit = fam_data.get("deposit", 0)
                for name in fam_data.get("members", []):
                    member = fm.find_user(name)
                    if member:
                        fm.family_account.add_member(member)
        print("Data loaded.")
    except FileNotFoundError:
        print("No saved data found.")
    except json.JSONDecodeError:
        print("Error reading saved data.")

# === ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ ===
def add_user():
    login = input("login: ").strip()
    name = input("name: ").strip()
    budget = validate_input(input("your budget: ").strip(), float)
    if not login or not name or budget is None or budget < 0:
        print("❌ Invalid input")
        return
    fm.add_user(login, name, budget)
    print(f"{name} added with {budget}₸")

# === ПОКАЗАТЬ ВСЕХ ===
def show_all():
    fm.show_all_users()
    if fm.family_account:  # проверяем, создан ли депозит
        print(f"family deposit: {fm.family_account.get_total()}₸")
    else:
        print("family deposit: not created yet")

    total = calculate_total_balance([{"bal": u.bal} for u in fm.users])
    print(f"total balance of all users: {total}₸")

# === ДОБАВИТЬ РАСХОД ===
def add_expense():
    if not fm.users:
        print("no users")
        return
    fm.show_all_users()
    num = validate_input(input("user num: "), int)
    if num is None or num < 1 or num > len(fm.users):
        print("invalid user number")
        return
    amount = validate_input(input("spent: "), float)
    if amount is None or amount <= 0:
        print("invalid amount")
        return
    user = fm.users[num-1]
    if user.add_expense(amount):
        print(f"spent {amount}₸, left {user.bal}₸")
    else:
        print("not enough balance")

# === ДОБАВИТЬ ДОХОД ===
def add_income():
    if not fm.users:
        print("no users")
        return
    fm.show_all_users()
    num = validate_input(input("user num: "), int)
    if num is None or num < 1 or num > len(fm.users):
        print("invalid user number")
        return
    amount = validate_input(input("income: "), float)
    if amount is None or amount <= 0:
        print("invalid amount")
        return
    user = fm.users[num-1]
    user.add_income(amount)
    print(f"added {amount}₸, now {user.bal}₸")

# === СЕМЕЙНЫЙ ВКЛАД ===
def open_family_account():
    if fm.family_account:
        print("Family account already exists.")
        return
    fm.family_account = FamilyAccount()
    print("Family account opened!")
def show_users():
    fm.show_all_users()
def add_family_member():
    if not fm.family_account:
        print("Family account not opened yet.")
        return
    if not fm.users:
        print("No users available.")
        return
    show_users()
    user_num = validate_input(input("Choose user to add: "), int)
    if user_num is None or user_num < 1 or user_num > len(fm.users):
        print("Invalid number.")
        return
    member = fm.users[user_num - 1]
    fm.family_account.add_member(member)
    print(f"{member.name} added to family.")

def add_family_funds():

    if not fm.family_account:
        print("Family account not opened yet.")
        return
    if not fm.family_account.members:
        print("No family members yet.")
        return
    print("\nFamily members:")
    for i, m in enumerate(fm.family_account.members, 1):
        print(f"{i}. {m.name} ({m.bal}₸)")
    num = validate_input(input("Choose member: "), int)
    if num is None or num < 1 or num > len(fm.family_account.members):
        print("Invalid number.")
        return
    member = fm.family_account.members[num - 1]
    amount = validate_input(input("Amount: "), float)
    if amount is None or amount <= 0:
        print("Invalid amount.")
        return
    if fm.family_account.add_funds(amount, member):
        print(f"{member.name} added {amount}₸ to family. Total: {fm.family_account.get_total()}₸")
    else:
        print("Not enough balance.")

# === ПОИСК И УДАЛЕНИЕ ===
def search_user():
    name = input("name to search: ").strip()
    if not name:
        print("empty name")
        return
    user = fm.find_user(name)
    print(user if user else "not found")

def delete_user():
    name = input("name to delete: ").strip()
    if not name:
        print("empty name")
        return
    if fm.delete_user(name):
        print(f"{name} deleted")
    else:
        print("user not found")

# === ПЕРЕВОДЫ МЕЖДУ ПОЛЬЗЫВАТЕЛЯМИ ===
def transfer_between_users():
    show_users()
    s = int(input("Sender number: "))
    r = int(input("Receiver number: "))
    amt = float(input("Amount: "))

    sender = fm.users[s - 1]
    receiver = fm.users[r - 1]

    if sender == receiver:
        print("You can't translate to yourself")
        return
    if amt < 100:
        print("The minimum transfer amount is 100₸")
        return
    if amt > sender.bal:
        print("insufficient amount")
        return

    sender.bal -= amt
    receiver.bal += amt
    print(f"{amt}₸ translated from {sender.name} to {receiver.name}")

# === ГРАФИК ЭКОНОМИКИ ===
import numpy as np
import matplotlib.pyplot as plt

def plot_user_economy(fm):
    if not fm.users:
        print("Пользователи отсутствуют.")
        return


    max_months = max(len(u.monthly_incomes) for u in fm.users)

    months = np.array([
        "Қаңтар", "Ақпан", "Наурыз", "Сәуір",
        "Мамыр", "Маусым", "Шілде", "Тамыз",
        "Қыркүйек", "Қазан", "Қараша", "Желтоқсан"
    ])[:max_months]


    all_incomes = np.zeros(max_months)
    all_expenses = np.zeros(max_months)

    for user in fm.users:
        user_incomes = np.array(user.monthly_incomes + [0] * (max_months - len(user.monthly_incomes)))
        user_expenses = np.array(user.monthly_expenses + [0] * (max_months - len(user.monthly_expenses)))
        all_incomes += user_incomes
        all_expenses += user_expenses

    avg_income = np.mean(all_incomes)
    avg_expenses = np.mean(all_expenses)

    print(f"Орташа айлық пополнение: {avg_income:.2f} ₸")
    print(f"Орташа айлық шығын: {avg_expenses:.2f} ₸")

    plt.figure(figsize=(10, 5))
    plt.plot(months, all_incomes, marker='o', linewidth=2, label="Пополнение")
    plt.plot(months, all_expenses, marker='s', linewidth=2, label="Расходы")
    plt.title("Айлар бойынша барлық пайдаланушылардың финансы")
    plt.xlabel("Айлар")
    plt.ylabel("Сумма (₸)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


# === НАЧАЛО ===
load_data()

# === МЕНЮ ===
menu = True
while menu:
    print("\n1 add user\n2 add expense\n3 add income\n4 open family account\n5 add family member\n6 add family funds\n7 transfer between users\n8 show all\n9 search\n10 delete\n11 save\n12 load\n13 economic graph\n14 exit")
    c = input("-> ").strip()
    if c == "1":
        add_user()
    elif c == "2":
        add_expense()
    elif c == "3":
        add_income()
    elif c == "4":
        open_family_account()
    elif c == "5":
        add_family_member()
    elif c == "6":
        add_family_funds()
    elif c == "7":
        transfer_between_users()
    elif c == "8":
        show_all()
    elif c == "9":
        search_user()
    elif c == "10":
        delete_user()
    elif c == "11":
        save_data()
    elif c == "12":
        load_data()
     elif c == "13":
        plot_user_economy(fm)
    elif c == "14":
        save_data()
        menu = False
    else:
        print("err")
