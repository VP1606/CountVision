import socket
import JSON_Contractor as JSC

targIP = str(socket.gethostbyname(socket.gethostname()))
JSC.SetData("SOCKET_IP", targIP)