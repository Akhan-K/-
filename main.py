print("=== Expenses input ===")
name = input("Name: ")
amount = float(input("Amount (tg): "))
cat = input("Category: ")

print(f"\nName: {name}")
print(f"Amount: {amount} tg")
print(f"Category: {cat}")
print(f"Amount > 0? {amount > 0}")

print("\n=== Expenses list ===")
items = []
cats = []

n = int(input("How many expenses? "))
for i in range(n):
    t = input(f"{i+1} name: ")
    s = float(input(f"{i+1} amount: "))
    c = input(f"{i+1} category: ")
    items.append({"name": t, "sum": s, "cat": c})
    cats.append(c)

uniq_cats = set(cats)
print(f"\nAll: {cats}")
print(f"Unique: {list(uniq_cats)}")

budget = ("tg", 100000)
print(f"\nBudget: {budget}")

print("\n=== Search ===")
q = input("Search name: ").lower()
found = False

for x in items:
    if q in x["name"].lower():
        print(f"Found: {x['name']} — {x['sum']} tg ({x['cat']})")
        found = True
if not found:
    print("Not found")

print("\n=== Dict & menu ===")
exp = {}
for x in items:
    exp.setdefault(x["cat"], []).append(x["sum"])

print("\nDict:")
for c, lst in exp.items():
    print(f"{c}: {lst} -> total: {sum(lst)} tg")

while True:
    print("\nMenu:")
    print("1 Add")
    print("2 Show all")
    print("3 Total by category")
    print("4 Exit")

    ch = input("Choose: ")

    if ch == "1":
        t = input("Name: ")
        s = float(input("Amount: "))
        c = input("Category: ")
        items.append({"name": t, "sum": s, "cat": c})
        exp.setdefault(c, []).append(s)
        print("Added")

    elif ch == "2":
        if not items:
            print("Empty")
        else:
            for x in items:
                print(f"- {x['name']}: {x['sum']} tg ({x['cat']})")

    elif ch == "3":
        c = input("Category: ")
        if c in exp:
            print(f"{c} total: {sum(exp[c])} tg")
        else:
            print("No such category")

    elif ch == "4":
        print("Exit")
        break
    else:
        print("Wrong choice")
