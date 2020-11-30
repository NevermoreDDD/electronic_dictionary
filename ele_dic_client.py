"""
    dict client
    function: send request and get result according to the input from users
    construction: first level --> registration, login, exit
                  second level --> search words, find history, logout
"""

from socket import *
from getpass import getpass # launched in cmd
import hashlib
# server address
HOST = '127.0.0.1'
PORT = 8080
ADDR = (HOST, PORT)
s = socket()
s.connect(ADDR)

def registration():
    """
        get registration information from users
    :return:
    """
    while True:
        user_name = input("Please enter your user name: ")
        passwd = getpass()
        passwd1 = getpass("Input your password again:")
        if passwd1 != passwd:
            print("Your password is not the same")
            continue
        if ' ' in user_name or ' ' in passwd:
            print("Space is not permitted")
            continue


        msg = "R %s %s"%(user_name, passwd)
        s.send(msg.encode()) # send to server
        data = s.recv(128).decode()
        if data == 'OK':
            print(data)
            print("Register OK")
        else:
            print(data)
            print("User name existing")
        return

def login():
    name = input("Username:")
    passwd = getpass()
    msg = 'L %s %s'%(name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        print("Login successfully!")
    else:
        print("Please check your username or password!")
def main():
    while True:
        print("""
        ==================Welcome================
        1. Registration   2. Login         3.exit
        =========================================
        """)
        cmd = input("Select an option")
        if cmd == '1':
            registration()
        elif cmd == '2':
            login()
        elif cmd == '3':
            s.send(cmd.encode())
        else:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()