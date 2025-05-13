class Student:
    def __init__(self, surname, birth, group, grades):
        self.surname = surname
        self.birth = birth
        self.group = group
        self.grades = grades

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_birth(self, new_birth):
        self.birth = new_birth

    def change_group(self, new_group):
        self.group = new_group

    def show_info(self):
        print("Фамилия: ", self.surname)
        print("Дата рождения: ", self.birth)
        print("Группа: ", self.group)
        print("Оценки: ", self.grades)


students = []


def add_student():
    surname = input("Фамилия: ")
    birth = input("Дата рождения (гггг-мм-дд): ")
    group = input("Номер группы: ")
    grades = input("Введите 5 оценок через пробел: ").split()
    grades = list(map(int, grades))
    student = Student(surname, birth, group, grades)
    students.append(student)
    print("Студент добавлен\n")


def list_students():
    if not students:
        print("Список пуст\n")
        return
    for i, s in enumerate(students):
        print(f"\nСтудент #{i + 1}")
        s.show_info()
    print()


def edit_student():
    num = int(input("Введите номер студента для изменения: ")) - 1
    if 0 <= num < len(students):
        s = students[num]
        print("1. Изменить фамилию")
        print("2. Изменить дату рождения")
        print("3. Изменить номер группы")
        choice = input("Выбор: ")
        if choice == "1":
            s.change_surname(input("Новая фамилия: "))
        elif choice == "2":
            s.change_birth(input("Новая дата рождения: "))
        elif choice == "3":
            s.change_group(input("Новый номер группы: "))
        else:
            print("Неверный выбор")
    else:
        print("Нет такого студента\n")


def find_student():
    surname = input("Введите фамилию: ")
    birth = input("Введите дату рождения: ")
    found = False
    for s in students:
        if s.surname == surname and s.birth == birth:
            print("\nНайден студент: ")
            s.show_info()
            found = True
    if not found:
        print("Студент не найден\n")


def main():
    while True:
        print("\n(◕‿◕)")
        print("1. Добавить студента")
        print("2. Список студентов")
        print("3. Изменить данные")
        print("4. Найти")
        print("0. Выход")
        cmd = input("Выберите действие: ")

        if cmd == "1":
            add_student()
        elif cmd == "2":
            list_students()
        elif cmd == "3":
            edit_student()
        elif cmd == "4":
            find_student()
        elif cmd == "0":
            print("Выход из программы")
            break
        else:
            print("Неверная команда")


main()
