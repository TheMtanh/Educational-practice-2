import sqlite3
import psutil
from datetime import datetime
import time


def init_db():
    with sqlite3.connect("system_monitor.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            cpu REAL,
            memory REAL,
            disk REAL)''')


def record_stats():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect("system_monitor.db") as conn:
        conn.execute("INSERT INTO stats (timestamp, cpu, memory, disk) VALUES (?,?,?,?)",
                     (now, cpu, mem, disk))
    print(f"[{now}] CPU: {cpu}%, RAM: {mem}%, Disk: {disk}%")


def view_stats():
    with sqlite3.connect("system_monitor.db") as conn:
        for row in conn.execute("SELECT * FROM stats"):
            print(row)


def menu():
    init_db()
    while True:
        print("\n1. Записать данные 2. Показать все записи 0. Выход")
        cmd = input("> ")
        if cmd == "1":
            record_stats()
        elif cmd == "2":
            view_stats()
        elif cmd == "0":
            break
        else:
            print("Неверная команда")

menu()
