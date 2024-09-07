#!/usr/bin/python3
import socket
import argparse

parser = argparse.ArgumentParser(description="This script scan all ports from a host.")
parser.add_argument("-a", "--address", help="Host IP Address", required=True)
args = parser.parse_args()

for port in range(1, 65536):
	address_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	address_socket.settimeout(1)
	
	res = address_socket.connect_ex((args.address, port))

	if (res == 0):
		print("Port", port, "is open")

	address_socket.close()