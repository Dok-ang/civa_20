import socket
import asyncio
async def start_game():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    with open("file/atile.json","r") as f:
        reg_options=f.read()
    await s.connect(("80.77.36.110",2024))
    #print(text)
    s.sendall(reg_options.encode("utf-8"))
    #date=s.recv(1024)
    s.close()
async def go():
    for i in range(100000):
        print(i)
        await asyncio.sleep(0.01)
async def go2():
    for i in range(-100000,0):
        print(i)
        await asyncio.sleep(0.01)
async def main():
    t0=asyncio.create_task(start_game())
    t1=asyncio.create_task(go())
    t2=asyncio.create_task(go2())
    await asyncio.gather(t0,t1,t2)
if __name__=="__main__":
    asyncio.run(main())