import sqlite3


def init_db():
    with sqlite3.connect("ilovedrink.db") as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            strength REAL,
            stock INTEGER
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            stock INTEGER
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS cocktails (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS cocktail_ingredients (
            cocktail_id INTEGER,
            ingredient_id INTEGER,
            amount INTEGER,
            FOREIGN KEY (cocktail_id) REFERENCES cocktails(id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
        )""")


def add_drink():
    name = input("Название напитка: ")
    strength = float(input("Крепость (%): "))
    stock = int(input("Остаток: "))
    with sqlite3.connect("ilovedrink.db") as conn:
        conn.execute("INSERT INTO drinks (name, strength, stock) VALUES (?, ?, ?)", (name, strength, stock))
        print("Напиток добавлен")


def view_drinks():
    with sqlite3.connect("ilovedrink.db") as conn:
        for row in conn.execute("SELECT * FROM drinks"):
            print(row)


def add_ingredient():
    name = input("Ингредиент: ")
    stock = int(input("Остаток: "))
    with sqlite3.connect("ilovedrink.db") as conn:
        conn.execute("INSERT INTO ingredients (name, stock) VALUES (?, ?)", (name, stock))
        print("Ингредиент добавлен")


def view_ingredients():
    with sqlite3.connect("ilovedrink.db") as conn:
        for row in conn.execute("SELECT * FROM ingredients"):
            print(row)


def create_cocktail():
    name = input("Название коктейля: ")
    price = float(input("Цена: "))
    with sqlite3.connect("ilovedrink.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO cocktails (name, price) VALUES (?, ?)", (name, price))
        cocktail_id = cur.lastrowid
        print("Добавьте ингредиенты (id и количество, 0 для выхода):")
        while True:
            ing_id = int(input("ID ингредиента: "))
            if ing_id == 0:
                break
            amount = int(input("Количество: "))
            cur.execute("INSERT INTO cocktail_ingredients (cocktail_id, ingredient_id, amount) VALUES (?, ?, ?)",
                        (cocktail_id, ing_id, amount))
        print("Коктейль создан")


def sell_cocktail():
    id = int(input("ID коктейля: "))
    with sqlite3.connect("ilovedrink.db") as conn:
        cur = conn.cursor()
        ingredients = cur.execute("SELECT ingredient_id, amount FROM cocktail_ingredients WHERE cocktail_id=?", (id,)).fetchall()
        for ing_id, amt in ingredients:
            cur.execute("UPDATE ingredients SET stock = stock - ? WHERE id = ?", (amt, ing_id))
        print("Продажа завершена")


def restock():
    id = int(input("ID напитка или ингредиента: "))
    amount = int(input("Добавить сколько: "))
    table = input("Это drink или ingredient? ")
    if table not in ["drinks", "ingredients"]:
        print("Ошибка")
        return
    with sqlite3.connect("ilovedrink.db") as conn:
        conn.execute(f"UPDATE {table} SET stock = stock + ? WHERE id = ?", (amount, id))
        print("Запасы пополнены")


def menu():
    init_db()
    while True:
        print("\nМеню:"
              "\n1. Добавить напиток"
              "\n2. Добавить ингредиент"
              "\n3. Просмотр напитков"
              "\n4. Просмотр ингредиентов"
              "\n5. Создать коктейль"
              "\n6. Продать коктейль"
              "\n7. Пополнить запасы"
              "\n0. Выход")
        cmd = input("> ")
        if cmd == "1": add_drink()
        elif cmd == "2": add_ingredient()
        elif cmd == "3": view_drinks()
        elif cmd == "4": view_ingredients()
        elif cmd == "5": create_cocktail()
        elif cmd == "6": sell_cocktail()
        elif cmd == "7": restock()
        elif cmd == "0": break
        else: print("Ошибка ввода")


menu()
