import socket
import JSON_Contractor as JSC
import os

targIP = str(socket.gethostbyname(socket.gethostname()))
JSC.SetData("SOCKET_IP", targIP)

os.system("python3 webserver.py")
os.system("python3 RunUI.py")