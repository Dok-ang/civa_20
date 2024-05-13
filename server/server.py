import mysql.connector
# З'єднання з базою даних
connection = mysql.connector.connect(
    host='localhost',  # або 'ip' для локального сервера
    user='root',
    password='admin',
    port=9090,  # порт, на якому працює MySQL
    database="civilization3"
)
all_resource=["people","tree","stone","food","iron","gold","oil"]
all_buildings=["sawmill","mine","farm","smithy","bank","oil_rig","barrack","shooting_gallery","polygon","post_office","tank_factory","airfield"]
all_army=["knight","assault_infantry","shooter","postman","tank","plane"]
# Створення об'єкта курсора
cursor = connection.cursor()
import socket
import json
import time
import random
import asyncio
#obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#obj.bind(("192.168.50.111",2024))
#obj.listen(100)

with open("file/start_resource.txt","r") as f:
    start_resource=json.loads(f.read())
resource_mining_time={}
cursor.execute("SELECT * FROM resource")
content = cursor.fetchall()
#print(content)
for i in range(len(all_resource)):
    resource_mining_time.setdefault(all_resource[i],content[i][2])
async def new_connect(input_message,output_message):
    #connect,adress=obj.accept()
    data=await input_message.read(1024)
    data=data.decode("utf-8")
    command=json.loads(data)
    print(command)
    #command, param=date.split(" ")
    if command["action"]=="autorization":
        cursor.execute("SELECT * FROM users")
        content = cursor.fetchall()
        all_token=[]
        for i in content:
            all_token.append(i[1])
        #print(all_token[14],command["token"])
        #for i in range(1000):
        #    print(i)
        #    await asyncio.sleep(0.1)
        if command["token"] in all_token:
            print("Ok")
            info={"action":"update_resource"}
            time_now=int(time.time())

            # Виконання SQL-запиту для отримання вмісту таблиці
            cursor.execute(f"SELECT * FROM buildings")
            # Отримання результатів та виведення їх на екран
            table_content = cursor.fetchall()
            #print(table_content)

            info_builds={}
            for build_tuple in table_content:
                cursor.execute(f"SELECT * FROM {build_tuple[1]} WHERE id_user=%s",(command["id"],))
                content = cursor.fetchall()
                count=content[0][1]
                buildings_start_time=content[0][2]
                new_buildings_count=content[0][3]
                mining_time=build_tuple[2]
                application_of_resources=build_tuple[3]
                info_builds.setdefault(build_tuple[1],[count,buildings_start_time,new_buildings_count,mining_time,application_of_resources])
            #print(info_builds)
            for table_name in all_resource:
                cursor.execute(f"SELECT * FROM {table_name} WHERE id_user=%s",(command["id"],))
                content = cursor.fetchall()
                #time_now=int(time.time())
                last_update=content[0][2]
                count=content[0][1]
                #print(content)
                time_pas=time_now-last_update

                # час побудови останньої будівлі
                

                count+=time_pas//resource_mining_time[table_name] # new res
                info.setdefault(table_name,count)
                last_update=time_now-time_pas%resource_mining_time[table_name]
                cursor.execute(f"UPDATE {table_name} SET count=%s WHERE id_user=%s",(count,command["id"]))
                cursor.execute(f"UPDATE {table_name} SET last_update=%s WHERE id_user=%s",(last_update,command["id"]))
            print(json.dumps(info))
            output_message.write(json.dumps(info).encode("utf-8"))
        else:
            # Вставка даних в таблицю
            print("new user0")
            command = "INSERT INTO {0} (token, name, email) VALUES (%s, %s, %s)".format("users")
            user_number=str(len(all_token)+1)
            token=user_number
            for i in range(16-len(user_number)):
                token=token+chr(int(str(time.time())[-1::])+random.randint(97,113))
            data2 = (token, "user", "")
            cursor.execute(command, data2)
            user_id=cursor.lastrowid # отримаємо id щойноствореного користувача
            time_now=int(time.time())
            cursor.execute("INSERT INTO people (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["people"],time_now))
            cursor.execute("INSERT INTO tree (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["tree"],time_now))
            cursor.execute("INSERT INTO stone (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["stone"],time_now))
            cursor.execute("INSERT INTO food (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["food"],time_now))
            cursor.execute("INSERT INTO iron (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["iron"],time_now))
            cursor.execute("INSERT INTO gold (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["gold"],time_now))
            cursor.execute("INSERT INTO oil (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["oil"],time_now))
            
            for building in all_buildings:
                cursor.execute(f"INSERT INTO {building} (id_user, count, buildings_start_time, new_buildings_count) VALUES (%s, %s, %s, %s)", (user_id,0,time_now,0))
            for army in all_army:
                cursor.execute(f"INSERT INTO {army} (id_user, count, army_start_time, new_army_count) VALUES (%s, %s, %s, %s)", (user_id,0,time_now,0))  
            connection.commit()
            info={"token":token,"id":int(user_number)}
            info.update(start_resource)
            info["action"]="init"
            print(json.dumps(info))
            output_message.write(json.dumps(info).encode("utf-8"))
            print("New user1")
    elif command["action"]=="mining_resource":
        date=json.dumps(resource_mining_time)
        output_message.write(date.encode("utf-8"))
    await output_message.drain()
    output_message.close()
    #connect.sendall(date)
async def main():
    server = await asyncio.start_server(new_connect,"192.168.0.120",8080)
    async with server:
        await server.serve_forever()
if __name__=="__main__":
    asyncio.run(main())