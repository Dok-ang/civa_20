import mysql.connector
# З'єднання з базою даних
connection = mysql.connector.connect(
    host='localhost',  # або 'localhost' для локального сервера
    user='root',
    password='root',
    port=2023  # порт, на якому працює MySQL
)
# Створення об'єкта курсора
cursor = connection.cursor()
# Створення бази даних (якщо її ще не існує)
name_base="civilization"
cursor.execute('DROP DATABASE IF EXISTS civilization')
connection.commit()
create_database_query = "CREATE DATABASE IF NOT EXISTS {0}".format(name_base)
cursor.execute(create_database_query)
# Вибір бази даних
cursor.execute("USE {0}".format(name_base))
users="users"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(16) NOT NULL,
    name VARCHAR(32) NOT NULL,
    email VARCHAR(50)
)""".format(users))

resource="resource"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_resource INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    mining_speed BIGINT
)""".format(resource))


# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_speed) VALUES (%s, %s)".format(resource)
data = ("people", 500)
cursor.execute(command, data)
data = ("food", 10)
cursor.execute(command, data)
data = ("tree", 60)
cursor.execute(command, data)
data = ("stone", 90)
cursor.execute(command, data)
data = ("oil", 450)
cursor.execute(command, data)
data = ("iron", 150)
cursor.execute(command, data)
data = ("gold", 300)
cursor.execute(command, data)

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_people INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("people",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_food INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("food",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tree INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("tree",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_stone INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("stone",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_oil INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("oil",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_iron INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("iron",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_gold INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("gold",users))


buildings="buildings"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_building INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    mining_speed INT NOT NULL,   
    resource_multiplier INT NOT NULL,   
    people INT NOT NULL,
    food INT NOT NULL,
    tree INT NOT NULL,
    stone INT NOT NULL,
    oil INT NOT NULL,
    iron INT NOT NULL,
    gold INT NOT NULL  )""".format(buildings))
# mining_speed - швидкість побудови
# resource_multiplier - доданок за кожен ресурс

# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_speed, resource_multiplier, people, food, tree, stone, oil, iron, gold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(buildings)
data = ("farm", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("sawmill", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("mine_stone", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("oil_well", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("mine_iron", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("mine_gold", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)

data = ("barrack_infantryman", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("shooting_range", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("barrack_berserker", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_farm INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("farm",users)) # ферма

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_sawmill INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("sawmill",users)) # лісопилка

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_mine_stone INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("mine_stone",users)) # шахтя камня

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_oil_well INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("oil_well",users)) # нафта

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_mine_iron INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("mine_iron",users)) # шахтя заліза

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_mine_gold INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("mine_gold",users)) # шахтя золота





cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_barrack_infantryman INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("barrack_infantryman",users)) # казарма

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_shooting_range INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("shooting_range",users)) # 


cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_barrack_berserker INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    buildings_time FLOAT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("barrack_berserker",users)) # 


army="army"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_army INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    mining_speed BIGINT NOT NULL,
    strength INT NOT NULL,
    hp INT NOT NULL,
    protection INT NOT NULL,
    theft INT NOT NULL,
    attack_defense_ratio FLOAT NOT NULL,
    service INT NOT NULL,
    people INT NOT NULL,
    food INT NOT NULL,
    tree INT NOT NULL,
    stone INT NOT NULL,
    oil INT NOT NULL,
    iron INT NOT NULL,
    gold INT NOT NULL
)""".format(army))
# protection у відсотках

# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_speed, strength, hp, protection, theft, attack_defense_ratio, service, people, food, tree, stone, oil, iron, gold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(army)
data = ("infantryman", 600, 60, 200, 20, 2, 1, 1, 1, 2, 2, 0, 0, 0, 50)
cursor.execute(command, data)
data = ("bowman", 600, 60, 200, 20, 2, 1, 1, 0.8, 2, 2, 0, 0, 0, 50)
cursor.execute(command, data)
data = ("berserker", 600, 60, 200, 20, 2, 1, 1, 1.2, 2, 2, 0, 0, 0, 50)
cursor.execute(command, data)

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_infantryman INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    army_time FLOAT,   
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("infantryman",users)) # піхотинець

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_bowman INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    army_time FLOAT,   
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("bowman",users)) # лучник

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_berserker INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    army_time FLOAT,   
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("berserker",users)) # berserker


cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_penny_pincher INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    army_time FLOAT,   
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("penny_pincher",users)) # penny_pincher


#cursor.execute('DELETE FROM people WHERE user_id = %s',('admin'))


# Підтвердження змін
connection.commit()

# Закриття курсора та з'єднання
cursor.close()
connection.close()
