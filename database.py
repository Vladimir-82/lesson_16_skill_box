import sqlite3

# Сперва создадим соединение с нашей базой данных.
# В нашем примере БД - файл расположенный на компьютере, он так же может быть расположен и на сервере.
# Важно помнить что в реальных задачах нельзя коммитить базу данных в репозиторий!
conn = sqlite3.connect('Northwind.sl3')
# Укажем тип получаемых данных
conn.text_factory = bytes
# Создадим курсор - специальный объект, с помощью которого мы сможем делать запросы к БД на языке запросов
cursor = conn.cursor()

# Отбор данных из БД:
# SELECT <список-полей> FROM <имя-таблицы>[ WHERE <условие>]
# Пример:
# Требуется отобрать список заказов,
# для которых значение поля Freight (плата за груз) больше значения 100,
# а регион доставки (ShipRegion) -- 'RJ'
cursor.execute("SELECT * FROM Orders WHERE (Freight > 100) AND (ShipRegion = 'RJ')")

# Получение отобранных значений:
results = cursor.fetchall()
print(f'Здесь выведется список значений, подходящих под заданные условия: {results}')

# results_one_more_time = cursor.fetchall()
# print(f'А здесь пустой список: {results_one_more_time}')
# Это происходит из-за того, что для повторного получения результата из курсора, необходимо создать новый запрос.
#
# # Попробуем получить именя всех клиентов, фамилии которых начинаются на C:
cursor.execute("SELECT ContactName FROM Customers WHERE ContactName LIKE '% C%'")
another_results = cursor.fetchall()
print(f'Список клиентов: {another_results}')

# # Удаление записи
# cursor.execute("DELETE FROM Orders WHERE OrderID='10'")
# # Изменения необходимо подтвердить:
# conn.commit()

cursor.execute("SELECT ContactName FROM Customers WHERE ContactName LIKE '% C%'")
another_results = cursor.fetchall()
print(f'Список клиентов: {another_results}')

# cursor.execute("INSERT INTO Orders (OrderID, CustomerID) VALUES ('1000', 'Kostukevich')")
# conn.commit()

cursor.execute("UPDATE Orders SET CustomerID='Vracataka' WHERE CustomerID='Kostukevich'")
conn.commit()


