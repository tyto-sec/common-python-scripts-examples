#!/usr/bin/python3
import socket
import argparse

parser = argparse.ArgumentParser(description="This script retrieves the banner of a service")
parser.add_argument("-a", "--address", help="Host IP Address", required=True)
parser.add_argument("-p", "--port", help="Host Port", required=True, type=int)
args = parser.parse_args()

address_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

res = address_socket.connect_ex((args.address, args.port))

if (res == 0):
	banner = address_socket.recv(1024)
	print(banner)
