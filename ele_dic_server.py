"""
    dict server
    function: application logic
    model: tcp multiprocess based on fork
"""
from operation_db import Database
from socket import *
from multiprocessing import Process
import signal, sys

# global variable

HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST,PORT)
db = Database()

def register(c, data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name, passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')

def login(c, data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name, passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')
def request(c):
    """
        receive
    :param c:
    :return:
    """
    db.create_cursor()
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ":", data)
        if data[0] == 'R':
            register(c, data)
        elif data[0] == 'L':
            login(c, data)
        elif data == 'Q':
            pass
        elif data == 'H':
            pass
        elif data == 'E':
            sys.exit("Process connect to %s exit." % (c.getpeername()))
def main():
    """
        establish connection
    :return:
    """
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    # deal with zombie process
    # signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # wait for connection
    print("Listen the port 8080")
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("Server End")
        except Exception as e:
            print(e)
            continue

        p = Process(target=request, args = (c, ))
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()