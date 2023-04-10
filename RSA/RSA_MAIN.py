from RSA import *
from sys import exit
if __name__ =='__main__':
    display()
    while True:
        c = input(">>>")
        if c=='1':
            encrypt_file()
        if c=='2':
            decrypt_file()
        display()

















