"""
    dict client
    function: send request and get result according to the input from users
    construction: first level --> registration, login, exit
                  second level --> search words, find history, logout
"""

from socket import *
from getpass import getpass # la

# server address
HOST = '127.0.0.1'
PORT = 8080
ADDR = (HOST, PORT)

def main():
    s = socket()
    s.connect(ADDR)
    while True:
        print("""
        ==================Welcome================
        1. Registration   2. Login         3.exit
        =========================================
        """)
        cmd = input("Select an option")
        if cmd == '1':
            s.send(cmd.encode())
        elif cmd == '2':
            s.send(cmd.encode())
        elif cmd == '3':
            s.send(cmd.encode())
        else:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()