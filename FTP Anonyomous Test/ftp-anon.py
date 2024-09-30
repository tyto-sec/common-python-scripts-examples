#!/usr/bin/python3

import sys
import socket
import argparse
import os

parser = argparse.ArgumentParser(description="This script will try to log in as anonymous or ftp user on a list of FTP servers.")
parser.add_argument("-l", "--list", help="Host IP Addresses List", required=True)
args = parser.parse_args()

try:
    with open(args.list, 'r') as file:
        hosts = [line.strip() for line in file.readlines()]

    for host in hosts:
        # Cria um novo socket TCP para cada host
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(5)
        try:
            tcp.connect((host, 21))
            banner = tcp.recv(1024).decode('utf-8')
            print(f"Banner do servidor {host}: {banner}")

            # Tentativa de login como ftp
            tcp.send(b"USER ftp\r\n")
            user_response = tcp.recv(1024).decode('utf-8')

            tcp.send(b"PASS ftp\r\n")
            pw_response = tcp.recv(1024).decode('utf-8')

            if "logged in" in pw_response.lower():
                print(f"Login como ftp no servidor {host} foi bem-sucedido.")
                tcp.close()
                continue

            tcp.send(b"USER anonymous\r\n")
            user_response = tcp.recv(1024).decode('utf-8')

            tcp.send(b"PASS anonymous\r\n")
            pw_response = tcp.recv(1024).decode('utf-8')

            if "logged in" in pw_response.lower():
                print(f"Login como anonymous no servidor {host} foi bem-sucedido.")
        except socket.error as e:
            print(f"Erro ao conectar ao servidor {host}: {e}")
        finally:
            tcp.close()

except Exception as e:
    print(f"Erro: {e}")
    sys.exit(os.EX_SOFTWARE)

sys.exit(os.EX_OK)
