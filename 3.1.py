class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        print(f'Зарплата {self.name} {self.surname} -> {self.rate * self.days}')
        print(f'Ставка: {self.rate}, дней отработано: {self.days}\n')


workers = [
    Worker("Иван", "Денисов", 1100, 31),
    Worker("Евгений", "Понасенков", 650, 16),
    Worker("Иоанн", "Пресвитер", 8888, 999)
]

for worker in workers:
    worker.GetSalary()
