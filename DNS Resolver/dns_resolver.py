#!/usr/bin/python3
import socket
import argparse

parser = argparse.ArgumentParser(description="This script scan all ports from a host.")
parser.add_argument("-a", "--address", help="Host IP Address", required=True)
args = parser.parse_args()

print(socket.gethostbyname(args.address))