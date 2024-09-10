from socket import *

DstIP = "192.168.15.0"
# Put your iphone IP here ^

# You can see the IP on iphone's wi-fi adjustments or on the router settings, it's
# easier if you reserve your IP in the settings to avoid having to change this value frequently

DstPort = 49983
DstAddr = (DstIP, DstPort)
udpClntSock = socket(AF_INET, SOCK_DGRAM)
data = "iFacialMocap_lookForward"
data = data.encode('utf-8')
udpClntSock.sendto(data, DstAddr)
server = socket(AF_INET, SOCK_DGRAM)
server.settimeout(0.05)

while (True):
    try:
        messages, address = server.recvfrom(8192)
        print(messages.decode('utf-8'))
    except:
        pass
