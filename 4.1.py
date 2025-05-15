import sqlite3


def init_db():
    with sqlite3.connect("students.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            first TEXT, last TEXT, middle TEXT,
            group_name TEXT, g1 INT, g2 INT, g3 INT, g4 INT)''')


def add():
    f = input("Имя: "); l = input("Фамилия: "); m = input("Отчество: ")
    g = input("Группа: "); marks = list(map(int, input("4 оценки: ").split()))
    with sqlite3.connect("students.db") as conn:
        conn.execute("INSERT INTO students (first, last, middle, group_name, g1, g2, g3, g4) VALUES (?,?,?,?,?,?,?,?)",
                     (f, l, m, g, *marks))


def view_all():
    with sqlite3.connect("students.db") as conn:
        for row in conn.execute("SELECT * FROM students"):
            print(row)


def view_one():
    id = input("ID: ")
    with sqlite3.connect("students.db") as conn:
        cur = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
        if cur:
            print(cur)
            avg = sum(cur[5:]) / 4
            print("Средний балл:", round(avg, 2))
        else:
            print("Не найден")


def edit():
    id = input("ID: ")
    f = input("Имя: "); l = input("Фамилия: "); m = input("Отчество: ")
    g = input("Группа: "); marks = list(map(int, input("4 оценки: ").split()))
    with sqlite3.connect("students.db") as conn:
        conn.execute("""
            UPDATE students SET first=?, last=?, middle=?, group_name=?,
            g1=?, g2=?, g3=?, g4=? WHERE id=?
        """, (f, l, m, g, *marks, id))


def delete():
    id = input("ID: ")
    with sqlite3.connect("students.db") as conn:
        conn.execute("DELETE FROM students WHERE id=?", (id,))


def group_avg():
    g = input("Группа: ")
    with sqlite3.connect("students.db") as conn:
        rows = conn.execute("SELECT g1, g2, g3, g4 FROM students WHERE group_name=?", (g,)).fetchall()
        if rows:
            grades = [n for row in rows for n in row]
            print("Средний:", round(sum(grades)/len(grades), 2))
        else:
            print("Нет данных")


def menu():
    init_db()
    while True:
        print("\n"
              "\n1. Добавить "
              "\n2. Все "
              "\n3. Один "
              "\n4. Редактировать "
              "\n5. Удалить "
              "\n6. Средний "
              "\n0. Выход")
        cmd = input("> ")
        if cmd == "1": add()
        elif cmd == "2": view_all()
        elif cmd == "3": view_one()
        elif cmd == "4": edit()
        elif cmd == "5": delete()
        elif cmd == "6": group_avg()
        elif cmd == "0": break
        else: print("Ошибка ввода")


menu()
