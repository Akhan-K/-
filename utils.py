def add_user_to_list(users_list, login, name, budget):
    """Добавляет пользователя в список"""
    users_list.append({
        "login": login,
        "name": name,
        "bal": float(budget),
        "spent": 0,
        "income": 0
    })
    return f"{name} added with {budget}₸"

def find_user_by_name(users_list, name):
    """Находит пользователя по имени"""
    for user in users_list:
        if user['name'].lower() == name.lower():
            return user
    return None

def remove_user_by_name(users_list, name):
    """Удаляет пользователя по имени"""
    for i, user in enumerate(users_list):
        if user['name'].lower() == name.lower():
            return users_list.pop(i)
    return None

def validate_input(value, input_type=float):
    """Проверяет валидность ввода"""
    try:
        return input_type(value)
    except (ValueError, TypeError):
        return None

def calculate_total_balance(users_list):
    """Рассчитывает общий баланс всех пользователей"""
    return sum(user['bal'] for user in users_list)
