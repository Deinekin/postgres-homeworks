"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os


def write_csv_to_sql_table(filename: str, table_name: str) -> None:
    """
    Функция для записи данных из .csv в postgresql

    :param filename: путь до .csv файла, откуда берем данные
    :param table_name: название таблицы в базе данных
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='wtf5959ololo')
        cur = conn.cursor()
        number_of_columns = len(next(reader)) * '%s, '
        cur.executemany(f"INSERT INTO {table_name} VALUES ({number_of_columns[:-2]})", reader)
        conn.commit()

        cur.close()
        conn.close()


def main() -> None:
    """Главная функция, получаем пути до каждого .csv файла и выгружаем из них данные в таблицу"""
    customer_path = os.path.abspath("north_data/customers_data.csv")
    employees_path = os.path.abspath("north_data/employees_data.csv")
    orders_path = os.path.abspath("north_data/orders_data.csv")

    write_csv_to_sql_table(customer_path, "customers")
    write_csv_to_sql_table(employees_path, "employees")
    write_csv_to_sql_table(orders_path, "orders")


if __name__ == '__main__':
    main()
