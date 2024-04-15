import socket
def start_game():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    with open("file/atile.json","r") as f:
        reg_options=f.read()
    s.connect(("80.77.36.110",2024))
    #print(text)
    s.sendall(reg_options.encode("utf-8"))
    #date=s.recv(1024)
    s.close()
def go():
    for i in range(100000):
        yield i
def go2():
    for i in range(100000):
        yield chr(i)
if __name__=="__main__":
    g=go()
    g2=go2()
    print(g)
    for i in g:
        print(i)
    for i in g2:
        print(i)