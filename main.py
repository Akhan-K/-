print("=== F1nance ===")

user = input("Name: ").strip()
budget = float(input("Budget: "))
cat = input("Category: ").lower()
spent = float(input("Spent: "))

left = budget - spent
over = spent > budget

print(f"\n{user}, spent {spent} on {cat}")
print(f"Left: {left:.2f}")
print("Over budget!" if over else "OK")

exp = [
    {"u": "Anna", "c": "food", "a": 1200},
    {"u": "Boris", "c": "transport", "a": 800},
    {"u": user, "c": cat, "a": spent}
]

cats = {x["c"] for x in exp}
print("\nCats:", ", ".join(cats))

fixed = ("food", "transport", "fun", "clothes", "health")

find = input("\nSearch cat: ").lower().strip()
print("Found" if find in cats else "No such cat")

note = input("Note: ").replace(",", ";").strip()
print("Words:", note.split())

pts = {"Anna": 150, "Boris": 90, user: 0}
if not over:
    pts[user] += 10
    print("Got +10 pts")

print("\nLeaders:")
for u, p in pts.items():
    print(f"{u}: {p}")

while True:
    print("\n1 Add  2 Cats  3 Leaders  4 Exit")
    ch = input("Choice: ").strip()

    if ch == "1":
        c = input("Cat: ").lower()
        a = float(input("Amt: "))
        exp.append({"u": user, "c": c, "a": a})
        print("Added")
    elif ch == "2":
        print(", ".join({x["c"] for x in exp}))
    elif ch == "3":
        for u, p in pts.items():
            print(f"{u}: {p}")
    elif ch == "4":
        print("Bye")
        break
    else:
        print("Err")
