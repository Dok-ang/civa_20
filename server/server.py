import mysql.connector
# З'єднання з базою даних
connection = mysql.connector.connect(
    host='localhost',  # або 'localhost' для локального сервера
    user='root',
    password='root',
    port=2023,  # порт, на якому працює MySQL
    database="civilization"
)
# Створення об'єкта курсора
cursor = connection.cursor()
list_resource=["people","food","tree","stone","oil","iron","gold"]
import time
import random
import socket
import json
import asyncio
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind(("localhost",2458))
#s.listen(100)

with open("file/resource_start.txt","r") as f:
    start_resource=json.loads(f.read())
#start_resource_dict=json.load(start_resource)
with open("file/user_number.txt","r") as f:
    number_user=f.read()
async def new_connect(input_message,output_message):
    #connect,adress=obj.accept()
    data=await input_message.read(1024)
    data=data.decode("utf-8")
    command=json.loads(data)
    #command, param=date.split(" ")
    if command["action"]=="autorization":
        with open("file/token.txt","r") as f:
            all_token=f.readlines()
        #print(all_token[0],command["token"]+"\n")
        if command["token"]+"\n" in all_token:
            #print(command)
            #print("Ok")
            inf={"action":"update_resource"}
            cursor.execute(f"SELECT * FROM resource")
            content = cursor.fetchall()
            resource_mining_speed={}
            for i in range(len(list_resource)):
                resource_mining_speed.setdefault(list_resource[i],content[i][2])
            #print(content)
            for table_name in list_resource:
                cursor.execute(f"SELECT * FROM {table_name} WHERE id_user=%s",(command["id"],))
                #print(content)
                content = cursor.fetchall()
                count=content[0][1]
                last_update=content[0][2]
                time_now=int(time.time())
                time_pas=time_now-last_update
                count+=time_pas//resource_mining_speed[table_name]
                last_update=time_now-time_pas%resource_mining_speed[table_name]
                inf.setdefault(table_name,count)
                cursor.execute(f"UPDATE {table_name} SET count=%s WHERE id_user=%s",(count,command["id"]))
                cursor.execute(f"UPDATE {table_name} SET last_update=%s WHERE id_user=%s",(last_update,command["id"]))
            output_message.write(json.dumps(inf).encode("utf-8"))
        else:
            # Вставка даних в таблицю
            command = "INSERT INTO {0} (token, name, email) VALUES (%s, %s, %s)".format("users")
            token=number_user
            for i in range(16-len(number_user)):
                token=token+chr(int(str(time.time())[-1::])+random.randint(97,113))
            data2 = (token, "user", "")
            cursor.execute(command, data2)
            user_id=cursor.lastrowid # отримаэмо id щойноствореного користувача
            time_now=int(time.time())
            cursor.execute("INSERT INTO people (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["people"],time_now))
            cursor.execute("INSERT INTO tree (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["tree"],time_now))
            cursor.execute("INSERT INTO stone (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["stone"],time_now))
            cursor.execute("INSERT INTO food (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["food"],time_now))
            cursor.execute("INSERT INTO iron (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["iron"],time_now))
            cursor.execute("INSERT INTO gold (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["gold"],time_now))
            cursor.execute("INSERT INTO oil (id_user, count, last_update) VALUES (%s, %s, %s)", (user_id,start_resource["oil"],time_now))
            connection.commit()
            #for i in range(1000):
            #    print(i)
            #    await asyncio.sleep(0.1)
            with open("file/user_number.txt","w") as f:
                f.write(str(int(number_user)+1))
            with open("file/token.txt","a") as f:
                f.write(token+"\n")
            start_resource["action"]="reboot"
            start_resource["token"]=token
            start_resource["id"]=int(number_user)
            output_message.write(json.dumps(start_resource).encode("utf-8"))
            print("New user")
    elif command["action"]=="resource_mining":
        cursor.execute(f"SELECT * FROM resource")
        content = cursor.fetchall()
        resource_mining_speed={}
        for i in range(len(list_resource)):
            resource_mining_speed.setdefault(list_resource[i],content[i][2])
        output_message.write(json.dumps(resource_mining_speed).encode("utf-8"))
    await output_message.drain()
    output_message.close()
    #connect.sendall(date)
async def main():
    server = await asyncio.start_server(new_connect, '192.168.50.111',2024)
    async with server:
        await server.serve_forever()
if __name__=='__main__':
    asyncio.run(main())
