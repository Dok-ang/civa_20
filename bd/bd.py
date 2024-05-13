import mysql.connector
# З'єднання з базою даних
connection = mysql.connector.connect(
    host='localhost',  # або 'ip' для локального сервера
    user='root',
    password='admin',
    port=9090  # порт, на якому працює MySQL
)
# Створення об'єкта курсора
cursor = connection.cursor()

name_base="civilization3"
cursor.execute("DROP DATABASE IF EXISTS {0}".format(name_base))
connection.commit()

cursor.execute("CREATE DATABASE IF NOT EXISTS {0}".format(name_base))

# оберем базу
cursor.execute("USE {0}".format(name_base))

# створимо таблиці
users="users"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    token VARCHAR(16) NOT NULL,
    name VARCHAR(32) NOT NULL,
    email VARCHAR(32) NOT NULL
)""".format(users))

resource="resource"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_resource INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(16) NOT NULL,
    mining_time BIGINT NOT NULL
)""".format(resource))

# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_time) VALUES (%s, %s)".format(resource)
data = ("people", 500)
cursor.execute(command, data)
data = ("tree", 60)
cursor.execute(command, data)
data = ("stone", 90)
cursor.execute(command, data)
data = ("food", 5)
cursor.execute(command, data)
data = ("iron", 150)
cursor.execute(command, data)
data = ("gold", 300)
cursor.execute(command, data)
data = ("oil", 450)
cursor.execute(command, data)

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_people INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    last_update INT,           
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("people"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tree INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    last_update INT, 
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("tree"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_food INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    last_update INT, 
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("food"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_iron INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    last_update INT, 
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("iron"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_stone INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    last_update INT, 
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("stone"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_gold INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    last_update INT, 
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("gold"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_oil INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    last_update INT, 
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("oil"))




buildings="buildings"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_buildings INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(16) NOT NULL,
    mining_time BIGINT NOT NULL,
    application_of_resources INT NOT NULL,
    people INT NOT NULL,
    tree INT NOT NULL,
    stone INT NOT NULL,
    food INT NOT NULL,
    iron INT NOT NULL,
    gold INT NOT NULL,
    oil INT NOT NULL           
)""".format(buildings))
# mining_time - час побудови будинку
# application_of_resources - на скільки збільшуємо видобудок ресурсів за вказану будівлю

# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_time, application_of_resources, people, tree, stone, food, iron, gold, oil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(buildings)
data = ("sawmill", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("mine", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("farm", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("smithy", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("bank", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("oil_rig", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("barrack", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("shooting_gallery", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("polygon", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("post_office", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("tank_factory", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)
data = ("airfield", 1000, 2, 4, 20, 2, 0, 2, 50, 0)
cursor.execute(command, data)

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_sawmill INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("sawmill")) # лісопилка


cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_mine INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("mine")) # шахта камня

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_farm INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("farm")) # ферма

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_smithy INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("smithy")) # кузня заліза

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_bank INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("bank")) # банк

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_oil_rig INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("oil_rig")) # нафтовишка

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_barrack INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("barrack")) # казарма

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_airfield INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("airfield"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tank_factory INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("tank_factory"))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_polygon INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("polygon")) # полігон

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_post_office INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("post_office")) # офіс перевозчиків

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_shooting_gallery INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("shooting_gallery")) # тир

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tank_factory INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("tank_factory")) # завод танків

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_airfield INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    buildings_start_time FLOAT,
    new_buildings_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("airfield")) # аеродром

army="army"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_army INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(16) NOT NULL,
    mining_time BIGINT NOT NULL,
    hp INT NOT NULL,
    armor INT NOT NULL,
    power INT NOT NULL,
    capacity INT NOT NULL,
    coefficient FLOAT NOT NULL,
    maintenance INT NOT NULL,
    people INT NOT NULL,
    tree INT NOT NULL,
    stone INT NOT NULL,
    food INT NOT NULL,
    iron INT NOT NULL,
    gold INT NOT NULL,
    oil INT NOT NULL
)""".format(army))
# capacity - місткість
# coefficient 0.5 - +50% до захисту та -50% до атаки, 1.5 - -50% до захисту та +50% до атаки
# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_time, hp, armor, power, capacity, coefficient, maintenance, people, tree, stone, food, iron, gold, oil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(army)
data = ("knight", 1000, 100, 20, 60, 2, 1, 1, 1, 1, 1, 2, 0, 50, 0)
cursor.execute(command, data)
data = ("assault_infantry", 1000, 100, 20, 60, 2, 1, 1, 1, 1, 1, 2, 0, 50, 0)
cursor.execute(command, data)
data = ("shooter", 1000, 100, 20, 60, 2, 1, 1, 1, 1, 1, 2, 0, 50, 0)
cursor.execute(command, data)
data = ("postman", 1000, 100, 20, 60, 2, 1, 1, 1, 1, 1, 2, 0, 50, 0)
cursor.execute(command, data)
data = ("tank", 1000, 100, 20, 60, 2, 1, 1, 1, 1, 1, 2, 0, 50, 0)
cursor.execute(command, data)
data = ("plane", 1000, 100, 20, 60, 2, 1, 1, 1, 1, 1, 2, 0, 50, 0)
cursor.execute(command, data)

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_knight INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    army_start_time FLOAT,
    new_army_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("knight")) # лицар


cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_assault_infantry INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    army_start_time FLOAT,
    new_army_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("assault_infantry")) # штурмова піхота

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_shooter INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    army_start_time FLOAT,
    new_army_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("shooter")) # стрелок

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_postman INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    army_start_time FLOAT,
    new_army_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("postman")) # стрелок

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tank INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    army_start_time FLOAT,
    new_army_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("tank")) # танк

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_plane INT PRIMARY KEY AUTO_INCREMENT,
    count INT,
    army_start_time FLOAT,
    new_army_count INT,      
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE ON UPDATE CASCADE         
)""".format("plane")) # літак

connection.commit()
cursor.close()
connection.close()