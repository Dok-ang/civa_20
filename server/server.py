import mysql.connector
# З'єднання з базою даних
connection = mysql.connector.connect(
    host = 'localhost',  # або 'localhost' для локального сервера
    user = 'root',
    password = 'root',
    port = 2023,  # порт, на якому працює MySQL
    database = "civilization"
)
# Створення об'єкта курсора
cursor = connection.cursor()
list_resource = ["people","food","tree","stone","oil","iron","gold"]
list_army = ["infantryman","bowman","berserker"]
buildings_resource = ["farm","sawmill","mine_stone","oil_well","mine_iron","mine_gold"]
buildings_army = ["barrack_infantryman","shooting_range","barrack_berserker"]


import time
import random
import socket
import json
import asyncio
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind(("localhost",2458))
#s.listen(100)

with open("file/atile.json","r") as f:
    start_resource = json.loads(f.read())
#start_resource_dict=json.load(start_resource)

async def new_connect(input_message, output_message):
    #connect,adress=obj.accept()
    data = await input_message.read(1024)
    data = data.decode("utf-8")
    command = json.loads(data)
    #command, param=date.split(" ")
    if command["action"] == "autorization":
        with open("file/options.json", "r") as f:
            all_token = f.readlines()
        #print(all_token[0],command["token"]+"\n")
        if command["token"] + "\n" in all_token:
            #print(command)
            #print("Ok")
            inf = {"action":"update_resource"}
            cursor.execute(f"SELECT * FROM resource")
            content = cursor.fetchall()
            inf.setdefault("all_resource",content)
            resource_mining_speed = {}
            for i in range(len(list_resource)):
                resource_mining_speed.setdefault(list_resource[i],content[i][2])
            #print(content)
            cursor.execute(f"SELECT * FROM buildings")
            content_build = cursor.fetchall()
            all_build = {}
            
            for index in range(len(buildings_resource)):
                print(index)
                all_build.setdefault(buildings_resource[index], content_build[index][2::])
            
            for index in range(1, len(list_resource)):
                cursor.execute(f"SELECT * FROM {list_resource[index]} WHERE id_user=%s",(command["id"],))
                cursor.execute(f"SELECT * FROM {buildings_resource[index-1]} WHERE id_user=%s",(command["id"],))
                build_info = cursor.fetchall()
                #print(content)
                content2 = cursor.fetchall()
                #print(content)
                count = content2[0][1]
                last_update = content2[0][2]
                time_now = int(time.time())
                time_pas = time_now - last_update
                building_speed = all_build[buildings_resource[index-1]][0]
                could_build = time_pas//building_speed
                is_building = build_info[0][3]
                already_built = is_building[1]

                if could_build >= is_building:
                    have_built = is_building
                    
                else:
                    have_built = could_build

                building_process_time = have_built * is_building
                min = already_built * building_process_time // time_pas // resource_mining_speed[list_resource[index]]
                max = (already_built + have_built) * building_process_time // time_pas // resource_mining_speed[list_resource[index]]
                average_resource_count = (min+max)/2
                last_update = content2[0][2] + building_process_time
                time_pas = time_now - last_update
                count += time_pas // resource_mining_speed[list_resource[index]] + average_resource_count
                last_update = time_now - time_pas % resource_mining_speed[list_resource[index]]
                inf.setdefault(index, count)
                cursor.execute(f"UPDATE {list_resource[index]} SET count=%s WHERE id_user=%s",(count,command["id"]))
                cursor.execute(f"UPDATE {list_resource[index]} SET last_update=%s WHERE id_user=%s",(last_update,command["id"]))
            #print(inf)
            output_message.write(json.dumps(inf).encode("utf-8"))
        else:
            with open("file/user_number.txt", "r") as f:
                number_user = f.read()
            # Вставка даних в таблицю
            command = "INSERT INTO {0} (token, name, email) VALUES (%s, %s, %s)".format("users")
            token = number_user
            for i in range(16 - len(number_user)):
                token = token + chr(int(str(time.time())[-1::]) + random.randint(97, 113))
            data2 = (token, "user", "")
            cursor.execute(command, data2)
            user_id = cursor.lastrowid # отримаэмо id щойноствореного користувача
            time_now = int(time.time())
            cursor.execute("INSERT INTO people (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["people"],time_now))
            cursor.execute("INSERT INTO tree (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["tree"],time_now))
            cursor.execute("INSERT INTO stone (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["stone"],time_now))
            cursor.execute("INSERT INTO food (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["food"],time_now))
            cursor.execute("INSERT INTO iron (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["iron"],time_now))
            cursor.execute("INSERT INTO gold (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["gold"],time_now))
            cursor.execute("INSERT INTO oil (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["oil"],time_now))
            
            
            for building in buildings_resource:
                cursor.execute(f"INSERT INTO {building} (id_user, count, buildings_time, new_buildings_count) VALUES (%s, %s, %s, %s)", (user_id, 0, time_now, 0))
            for building in buildings_army:
                cursor.execute(f"INSERT INTO {building} (id_user, count, buildings_time, new_buildings_count) VALUES (%s, %s, %s, %s)", (user_id,0,time_now,0))
            for army in list_army:
                cursor.execute(f"INSERT INTO {army} (id_user, count, army_time, new_army_count) VALUES (%s, %s, %s, %s)", (user_id,0,time_now,0))
            
            connection.commit()
            #for i in range(1000):
            #    print(i)
            #    await asyncio.sleep(0.1)
            with open("file/user_number.txt", "w") as f:
                f.write(str(int(number_user) + 1))
            with open("file/token.txt", "a") as f:
                f.write(token + "\n")
            start_resource["action"] = "reboot"
            start_resource["token"] = token
            start_resource["id"] = int(number_user)

            cursor.execute(f"SELECT * FROM resource")
            content = cursor.fetchall()
            start_resource.setdefault("all_resource", content)

            output_message.write(json.dumps(start_resource).encode("utf-8"))
            print("New user")
    elif command["action"] == "resource_mining":
        cursor.execute(f"SELECT * FROM resource")
        content = cursor.fetchall()
        resource_mining_speed = {}
        for i in range(len(list_resource)):
            resource_mining_speed.setdefault(list_resource[i], content[i][2])
        output_message.write(json.dumps(resource_mining_speed).encode("utf-8"))
    await output_message.drain()
    output_message.close()
    #connect.sendall(date)
async def main():
    server = await asyncio.start_server(new_connect, '192.168.1.103', 2024)
    async with server:
        await server.serve_forever()
if __name__ == '__main__':
    asyncio.run(main())
