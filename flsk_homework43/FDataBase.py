import sqlite3
import time
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_post(self, title, price, text):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM posts WHERE title LIKE ?", (title,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Такой товар уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, price, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления товара в БД " + str(e))
            return False
        return True

    def get_post(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, price, description FROM posts WHERE id={post_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения товара из базы данных " + str(e))

        return False, False, False

    def get_posts_anonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, price, description FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения товара из базы данных " + str(e))

        return []

