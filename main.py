import os
import click
import sqlite
# Добавь ему функцию сравнения для обучения по книгам и тд
# Создаёт код из словаря (команда запомни), пишет его в idle и выполняет
# Может обратную тоже добавить для нормального поиска и уровень вложенности зависимости
ai_path =
def db_search(key):
    # Возвращает словарь (key: (от него зависят), (зависит от: значит))
while True:
    quest = str(input())
    words = []
    while quest:
        pf = quest.find(' ')
        words.append(quest[0:pf - 1])
        quest.remove(0, pf)
    # Обращается к бд по ключевым словам, пытается построить цепь
    chain = [] # Список цепи
    key = db_search(words[0])
    chains.append([{key:}])
    del words[0]
    for word in words:
        key = db_search(key)
        