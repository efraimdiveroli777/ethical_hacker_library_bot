import sqlite3

def start_create(tg_id, user_name):
    try:
        with sqlite3.connect('request/hacker.db') as db:
            cursor = db.cursor()

            cursor.execute(f"""SELECT tg_id FROM users WHERE {tg_id} = tg_id""")
            result = cursor.fetchone()

            if result is None:
                cursor.execute(
                    f"""INSERT INTO users (tg_id, user_name) VALUES ({tg_id}, '{user_name}')""")

                id = cursor.execute(f"""SELECT id FROM users WHERE {tg_id} = tg_id""").fetchone()[0]

                cursor.execute(
                    f"""INSERT INTO user_subscriptions (user_id) VALUES ({id})""")


    except sqlite3.Error as e:
        print("Ошибка")

def get_user_profile(tg_id):
    try:
        with sqlite3.connect('request/hacker.db') as db:
            cursor = db.cursor()

            return cursor.execute(f"""SELECT id, tg_id, date, user_name, money FROM users WHERE tg_id = {tg_id}""").fetchone()

    except sqlite3.Error as e:
        print("Ошибка")

def get_sub_user(tg_id):
    try:
        with sqlite3.connect('request/hacker.db') as db:
            cursor = db.cursor()

            id = cursor.execute(f"""SELECT id FROM users WHERE {tg_id} = tg_id""").fetchone()[0]

            return cursor.execute(f"""SELECT ncrack, sqlmap, msfconsole, searchsploit, hydra, nmap FROM user_subscriptions WHERE {id} = user_id""").fetchone()

    except sqlite3.Error as e:
            print("Ошибка")


def up_sub_user(tg_id, mon):
    try:
        with sqlite3.connect('request/hacker.db') as db:
            cursor = db.cursor()

            money = cursor.execute(f"""SELECT money FROM users WHERE tg_id = {tg_id}""").fetchone()

            money = money[0] - mon
            cursor.execute("""
                UPDATE users
                SET money = ?
                WHERE tg_id = ?
            """, (money, tg_id))

    except sqlite3.Error as e:
        print("Ошибка")

def buy_balance(tg_id, money):
    try:
        with sqlite3.connect('request/hacker.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT money FROM users WHERE tg_id = ?", (tg_id,))
            result = cursor.fetchone()
            if result[0] > 0:
                cursor.execute(f"""UPDATE users SET `money` = {money + result[0]} WHERE tg_id = {tg_id}""")
            else:
                cursor.execute(f"""UPDATE users SET `money` = {money} WHERE tg_id = {tg_id}""")


    except sqlite3.Error as e:
        print("Ошибка")

def update_program(tg_id, program):
    try:
        with sqlite3.connect('request/hacker.db') as db:
            cursor = db.cursor()

            id = cursor.execute(f"""SELECT id FROM users WHERE {tg_id} = tg_id""").fetchone()[0]

            cursor.execute(f"""UPDATE user_subscriptions SET `{program}` = True WHERE user_id = {id}""")


    except sqlite3.Error as e:
        print("Ошибка")

def get_program(tg_id, program):
    try:
        with sqlite3.connect('request/hacker.db') as db:
            cursor = db.cursor()

            id = cursor.execute(f"""SELECT id FROM users WHERE {tg_id} = tg_id""").fetchone()[0]

            return cursor.execute(f"""SELECT {program} FROM user_subscriptions WHERE user_id = {id}""").fetchone()

    except sqlite3.Error as e:
        print("Ошибка")
