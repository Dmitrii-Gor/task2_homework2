import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        # cur.execute("""
        #               DROP TABLE phone;
        #               DROP TABLE email;
        #               DROP TABLE clients;
        #                   """)
        cur.execute("""
                   CREATE TABLE IF NOT EXISTS clients(
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(80) NOT NULL,
                       surname VARCHAR(80) NOT NULL
                   );
                   """)
        cur.execute("""
                   CREATE TABLE IF NOT EXISTS email(
                       id SERIAL PRIMARY KEY,
                       email TEXT NOT NULL,
                       clients_id INTEGER NOT NULL REFERENCES clients(id)
                   );
                   """)
        cur.execute("""
                   CREATE TABLE IF NOT EXISTS phone(
                       id SERIAL PRIMARY KEY,
                       number VARCHAR(15) NOT NULL,
                       clients_id INTEGER NOT NULL REFERENCES clients(id)
                   );
                   """)
        conn.commit()


def add_client(conn, name, surname):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO clients(name, surname) VALUES(%s, %s);""", (name, surname))
        conn.commit()
        cur.execute("""SELECT * FROM clients WHERE name=%s AND surname=%s;""", (name, surname))
        print(cur.fetchone())  # извлечь все строки


def add_phone(conn, clients_id, number):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO phone(number, clients_id) VALUES(%s, %s);""", (number, clients_id))
        conn.commit()
        cur.execute("""SELECT * FROM phone WHERE clients_id=%s AND number=%s;""", (clients_id, number))
        print(cur.fetchone())


def add_email(conn, clients_id, email):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO email(email, clients_id) VALUES(%s, %s);""", (email, clients_id))
        conn.commit()
        cur.execute("""SELECT * FROM email WHERE clients_id=%s AND email=%s;""", (clients_id, email))
        print(cur.fetchone())


def change_data_client(conn, old_name, old_surname, new_name, new_surname):
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM clients WHERE name=%s AND surname=%s;""", (old_name, old_surname))
        clients_id = cur.fetchone()[0]
    if new_name != '0' and new_surname == '0':
        with conn.cursor() as cur:
            cur.execute("""UPDATE clients SET name=%s WHERE id=%s;""", (new_name, clients_id))
            cur.execute("""SELECT * FROM clients;""")
            print(cur.fetchone())
            conn.commit()
    elif new_name == '0' and new_surname != '0':
        with conn.cursor() as cur:
            cur.execute("""UPDATE clients SET surname=%s WHERE id=%s;""", (new_surname, clients_id))
            cur.execute("""SELECT * FROM clients;""")
            print(cur.fetchone())
            conn.commit()
    else:
        with conn.cursor() as cur:
            cur.execute("""UPDATE clients SET name=%s WHERE id=%s;""", (new_name, clients_id))
            cur.execute("""SELECT * FROM clients;""")
            cur.execute("""UPDATE clients SET surname=%s WHERE id=%s;""", (new_surname, clients_id))
            cur.execute("""SELECT * FROM clients;""")
            print(cur.fetchone())
            conn.commit()


def change_client_number(conn,old_number, new_number):
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM phone WHERE number=%s;""", (old_number,))
        phone_id = cur.fetchone()[0]
        cur.execute("""UPDATE phone SET number=%s WHERE id=%s;""", (new_number, phone_id))
        cur.execute("""SELECT * FROM phone;""")
        print(cur.fetchone())
        conn.commit()


def change_client_email(conn,old_email, new_email):
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM email WHERE email=%s;""", (old_email,))
        email_id = cur.fetchone()[0]
        cur.execute("""UPDATE email SET email=%s WHERE id=%s;""", (new_email, email_id))
        cur.execute("""SELECT * FROM email;""")
        print(cur.fetchone())
        conn.commit()


def delete_number(conn,name,surname):
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM clients WHERE name=%s AND surname=%s;""", (name,surname))
        clients_id = cur.fetchone()[0]
        cur.execute("""DELETE FROM phone WHERE clients_id=%s;""", (clients_id,))
        cur.execute("""SELECT * FROM phone;""")
        print(cur.fetchone())
        conn.commit()


def delete_clients_data(conn,name,surname):
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM clients WHERE name=%s AND surname=%s;""", (name,surname))
        clients_id = cur.fetchone()[0]
        cur.execute("""DELETE FROM phone WHERE clients_id=%s;""", (clients_id,))
        cur.execute("""SELECT * FROM phone;""")
        print(cur.fetchone())
        cur.execute("""DELETE FROM email WHERE clients_id=%s;""", (clients_id,))
        cur.execute("""SELECT * FROM email;""")
        print(cur.fetchone())
        cur.execute("""DELETE FROM clients WHERE id=%s;""", (clients_id,))
        cur.execute("""SELECT * FROM clients;""")
        print(cur.fetchone())
        conn.commit()


def find_client_data(conn, name, surname, email, number):
    with conn.cursor() as cur:
        if email != '0':
            cur.execute("""SELECT clients_id FROM email WHERE email=%s;""", (email,))
            clients_id = cur.fetchone()[0]
            cur.execute("""SELECT number FROM phone WHERE clients_id=%s;""", (clients_id,))
            print(cur.fetchone())
            cur.execute("""SELECT name,surname FROM clients WHERE id=%s;""", (clients_id,))
            print(cur.fetchone())
            return
        elif number != '0':
            cur.execute("""SELECT clients_id FROM phone WHERE number=%s;""", (number,))
            clients_id = cur.fetchone()[0]
            cur.execute("""SELECT email FROM email WHERE clients_id=%s;""", (clients_id,))
            print(cur.fetcone())
            cur.execute("""SELECT number FROM phone WHERE clients_id=%s;""", (clients_id,))
            print(cur.fetchone())
            cur.execute("""SELECT name, surname FROM clients WHERE id=%s;""", (clients_id,))
            print(cur.fetchone())
            return
        else:
            cur.execute("""SELECT id FROM clients WHERE name=%s AND surname=%s;""", (name,surname))
            clients_id = cur.fetchone()[0]
            print('client_id - ', clients_id)
            cur.execute("""SELECT email FROM email WHERE clients_id=%s;""", (clients_id,))
            print('email - ', cur.fetchone())
            cur.execute("""SELECT number FROM phone WHERE clients_id=%s;""", (clients_id,))
            print('phone - ', cur.fetchone())


def show_all(password='0'):
    if password == 'ваш пароль':
        with conn.cursor() as cur:
            cur.execute("""
                    SELECT * FROM clients;
                    """)
            print(cur.fetchall())
            cur.execute("""
                   SELECT * FROM phone;
                   """)
            print(cur.fetchall())
            cur.execute("""
                           SELECT * FROM email;
                    """)
            print(cur.fetchall())


conn = psycopg2.connect(database='netology_db', user='ваш пользователь', password='ваш пароль')
create_db(conn)

while (True):

    status = input('Добавить-Add/Изменить-Ch/Удалить-del/Найти-find ')
    if status == 'Add':
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        add_client(conn, name, surname)
        status = input('Хотите добавить телефон/email? N/Y ')
        if status == 'Y':
            status = input ('Телефон - t, email - e')
            if 't' in status:
                clients_id = input('Введите id клиента: ')
                number = input('Введите номер: ')
                add_phone(conn, clients_id, number)
            if 'e' in status:
                clients_id = input('Введите id клиента: ')
                email = input('Введите email: ')
                add_email(conn, clients_id, email)

    if status == 'Ch':
        status = input('Что хотите поменять? Имя/фамилию - n, телефон-t, email - e ')
        if 'n' in status:
            old_name = input("Старое имя? ")
            old_surname = input("Старая фамилия? ")
            new_name = input("Новое имя?(Если нет - введите 0) ")
            new_surname = input("Новая фамилия? (Если нет - введите 0) ")
            change_data_client(conn, old_name, old_surname, new_name, new_surname)
        if 't' in status:
            old_number = input('Старый номер? ')
            new_number = input('Новый номер? ')
            change_client_number(conn, old_number, new_number)
        if 'e' in status:
            old_email = input('Старый email? ')
            new_email = input('Новый email? ')
            change_client_email(conn, old_email, new_email)

    if status == 'del':
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        status = input('Удалить пользователя(del_u) или удалить номер телефона(del_t)? ')
        if status == 'del_u':
            delete_clients_data(conn, name, surname)
        if status == 'del_t':
            delete_number(conn, name, surname)

    if status == 'find':
        number = input("Телефон? (Если нет - введите 0) ")
        email = input("Email? (Если нет - введите 0) ")
        name = input("Имя? (Если нет - введите 0) ")
        surname = input("Фамилия? (Если нет - введите 0) ")
        find_client_data(conn, name, surname, email, number)

    if status == 'show_all':
        __pass = input('Введите свой пароль - ')
        show_all(__pass)