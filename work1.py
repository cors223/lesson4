def sal():
    try:
        time = float(input(f"Выработка в часах: "))
        salary = int(input(f"Ставка: "))
        bonus = int(input(f"Премия: "))
        res = time * salary + bonus
        print(f"заработная плата: {res}")
    except ValueError:
        return print(f"Not a number")
sal()
