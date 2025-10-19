print("=== All Finance ===")

users = []
family = {"deposit": 0}
deps = ("еда", "транспорт", "развлечения", "одежда")

def add_user():
    login = input("login: ").strip()
    name = input("name: ").strip()
    budget = float(input("your budget: "))
    users.append({"login": login, "name": name, "bal": budget, "spent": 0, "income": 0})
    print(f"{name} added with {budget}₸")

def show_users():
    for i, u in enumerate(users):
        print(f"{i+1}. {u['name']} | balance:{u['bal']}₸ | spent:{u['spent']}₸ | income:{u.get('income', 0)}₸")

add_user()

dep = input("deposit name: ").lower().strip()
if dep not in deps:
    print("new deposit added")
else:
    print("deposit found:", dep)

menu = True
while menu:
    print("\n1 add user\n2 add expense\n3 add income\n4 family add\n5 show all\n6 exit")
    c = input("-> ").strip()
    if c == "1":
        add_user()
    elif c == "2":
        if not users:
            print("no users")
            continue
        show_users()
        i = int(input("user num: ")) - 1
        amt = float(input("spent: "))
        users[i]["spent"] += amt
        users[i]["bal"] -= amt
        print(f"spent {amt}₸, left {users[i]['bal']}₸")
    elif c == "3":
        show_users()
        i = int(input("user num: ")) - 1
        inc = float(input("income: "))
        users[i]["bal"] += inc
        users[i]["income"] += inc
        print(f"added {inc}₸, now {users[i]['bal']}₸")
    elif c == "4":
        show_users()
        i = int(input("user num: ")) - 1
        fam = float(input("add to family: "))
        family["deposit"] += fam
        users[i]["bal"] -= fam
        print(f"family +{fam}₸ by {users[i]['name']}, total {family['deposit']}₸")
    elif c == "5":
        show_users()
        print(f"family deposit: {family['deposit']}₸")
    elif c == "6":
        menu = False
    else:
        print("err")
